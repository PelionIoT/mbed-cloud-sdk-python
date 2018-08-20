import functools
import requests
import dotenv
import os
import functools
import textwrap

from mbed_cloud import utils
from mbed_cloud import pagination


def pluck_if_not_none(source, *pluck):
    return {k: source[k] for k in pluck if source[k] is not None}


def strip_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))
DEFAULT_HOST = "https://api.us-east-1.mbedcloud.com"
DEFAULT_API_KEY = None

global global_sdk


class ApiErrorResponse(requests.HTTPError):
    pass


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
    def __init__(self, api_key=None, host=None):
        self.api_key = api_key or os.getenv("MBED_CLOUD_SDK_HOST") or DEFAULT_API_KEY
        self.host = host or os.getenv("MBED_CLOUD_SDK_HOST", DEFAULT_HOST)
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

        self.models = api.EntityManager(self)
        self.models2 = api.InstanceFactory(self)
        self.factory = api.InstanceFactory(self)

    @property
    def client(self):
        return self._client

    def get_entity(self, klass, **kwargs):
        from mbed_cloud.sdk import api

        return getattr(api, kl)


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
                "Authorization": "Bearer %s" % self._config.api_key,
                "UserAgent": utils.get_user_agent(),
            }
        )


def manage(sdk, entity):
    # @functools.wraps(entity)
    class WrappedEntity(entity):
        _sdk = sdk

    return WrappedEntity


def get_or_create_global_sdk_instance():
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


class Entity:
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

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

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
        """Plugs in to some http request handling mechanism"""
        url = (self._client.config.host + path).format(**path_params)
        response = self._client.session.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body_params,
            files=stream_params,
            stream=any(stream_params),
            **kwargs,
        )
        if unpack is None:
            unpack = self

        if response.status_code // 100 == 2:
            if unpack:
                for k, v in response.json().items():
                    setattr(unpack, inbound_renames.get(k, k), v)
                return unpack
            else:
                return response
        else:
            raise ApiErrorResponse(
                "Error response from API (HTTP %s):\n%s"
                % textwrap.indent(response.content, "  ")
            )
