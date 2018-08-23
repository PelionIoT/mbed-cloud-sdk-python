import functools
import inspect
import requests
import dotenv
import os
import json
import functools
import textwrap

from mbed_cloud import utils
from mbed_cloud import pagination

from mbed_cloud.sdk.logs import LOGGER


def pluck_if_not_none(source, *pluck):
    return {k: source[k] for k in pluck if source[k] is not None}


def strip_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


DEFAULT_HOST = "https://api.us-east-1.mbedcloud.com"
DEFAULT_API_KEY = None

global_sdk = None


class ApiErrorResponse(IOError):
    raw = None
    status_code = None
    all_parameters = None


def paginate(unpack):
    """Decorator that wraps listable_call

    In a way that allows it to be paginated
    """

    def decorator(listable_call):
        @functools.wraps(listable_call)
        def wrapper(**kwargs):
            return pagination.PaginatedResponse(
                func=listable_call, lwrap_type=unpack, unpack=False, **kwargs
            )

        return wrapper

    return decorator


class Config:
    _tried_dotenv = False
    api_key = None
    host = None

    def __init__(self, **kwargs):
        self._set_defaults(**kwargs)
        if not self.api_key and not Config._tried_dotenv:
            dotenv.load_dotenv(
                dotenv.find_dotenv(usecwd=True, raise_error_if_not_found=True)
            )
            self._set_defaults()
            # mark dotenv load complete, so we don't have to do it again
            Config._tried_dotenv = True

    def _set_defaults(self, **updates):
        self.update(updates)
        self.api_key = (
            self.api_key or os.getenv("MBED_CLOUD_SDK_API_KEY") or DEFAULT_API_KEY
        )
        self.host = self.host or os.getenv("MBED_CLOUD_SDK_HOST") or DEFAULT_HOST
        self.user_agent = utils.get_user_agent()

    def update(self, *updates, **kwargs):
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def items(self):
        return ((k, v) for k, v in vars(self).items() if not k.startswith("_"))


class SDK:
    def __init__(self, config=None, **config_overrides):
        self._config = Config()
        self._config.update({"user_agent": utils.get_user_agent()})
        self._config.update(config or {})
        self._config.update(config_overrides)

        self._client = Client(self._config)

        from mbed_cloud.sdk import api

        self.entities = api.InstanceFactory(self)

    @property
    def client(self):
        return self._client


class Client:
    def __init__(self, config):
        """

        :param config:
        :type config: Config
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": "Bearer %s" % self.config.api_key,
                "UserAgent": utils.get_user_agent(),
            }
        )


def get_or_create_global_sdk_instance():
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


def pretty_literal(content, indent=2, replace_null=True):
    """Given content comprised of literals, render them line-by-line

    json lib is used instead of pretty print because it looks better
    """
    content = textwrap.indent(
        json.dumps(content, indent=2, default=lambda x: str(type(x))), " " * indent
    )
    return content.replace(" null", " None") if replace_null else content


class Entity:
    _fieldnames = []

    def __init__(self, client, **kwargs):
        """

        :param client:
        :type client: Client or SDK
        :param kwargs:
        """
        if client is None:
            client = get_or_create_global_sdk_instance()
        if isinstance(client, SDK):
            client = client.client
        self._client = client
        self._logger = LOGGER.getChild(self.__class__.__name__)

    def __str__(self):
        friendly = "?"
        for name in (
            getattr(self, f, None)
            for f in ["full_name", "name", "id"] + self._fieldnames
        ):
            if name is not None:
                friendly = name
                break
        return "<%s %s>" % (self.__class__.__name__, friendly)

    def __repr__(self):
        return repr({field: getattr(self, field) for field in self._fieldnames})

    def to_literal(self):
        return {field: getattr(self, field).to_literal() for field in self._fieldnames}

    def _from_api(self, inbound_renames, **kwargs):
        for k, v in kwargs.items():
            field = getattr(self, "_" + inbound_renames.get(k, k), None)
            if field:
                field.from_api(v)
        return self

    def _call_api(
        self,
        method,
        path,
        headers=None,
        path_params=None,
        query_params=None,
        body_params=None,
        stream_params=None,
        inbound_renames=None,
        unpack=None,
        **kwargs,
    ):
        """Uses an http request handling mechanism to fetch and return results from the network"""
        url = self._client.config.host + path
        if path_params:
            url = url.format(**path_params)
        response = self._client.session.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body_params,
            files=stream_params,
            stream=bool(stream_params),
            **kwargs,
        )
        if unpack is None:
            unpack = self

        inbound_renames = inbound_renames or {}

        if response.status_code // 100 == 2:
            if unpack:
                if inspect.isclass(unpack):
                    unpack = unpack()  # noqa - we're going to instantiate it
                return unpack._from_api(inbound_renames, **response.json())
            else:
                return response

        # else the response indicates an error

        # check if we didn't have an api key set
        all_params = locals()
        api_key = self._client.config.api_key or ""
        host = self._client.config.host
        hints = [
            "Request parameters:",
            "URL: %s" % url,
            "HTTP method: %s, api_key: '%s%s%s'"
            % (method.upper(), api_key[:2], "***" if api_key else "", api_key[-3:]),
            "Any additional parameters are attached to this %s instance."
            % ApiErrorResponse.__name__,
        ]
        if not api_key:
            hints.append(
                "There was no API key detected. You need to set one to interact with the cloud."
            )
        if not host.startswith("https"):
            hints.append(
                "The host scheme should start with 'https' for a secure connection to the cloud."
            )
        if path_params and not all(path_params.values()):
            hints.append(
                "Some parameters required in the URL appear to be missing:\n%s"
                % pretty_literal(path_params)
            )
        hints = "\n".join(hints)
        try:
            content = json.loads(response.content)
        except Exception:
            content = {"response": content}
        else:
            # remap error response fields too!
            fields = content.get("fields", [])
            fields[:] = [inbound_renames.get(f, f) for f in fields]
        api_feedback = pretty_literal(content)
        error = ApiErrorResponse(
            "Error response from API (HTTP %s):\n%s\n%s"
            % (response.status_code, api_feedback, hints)
        )
        error.content = content
        error.status_code = response.status_code
        error.raw = all_params.pop("response")
        error.all_parameters = all_params
        raise error
