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


class Config(dict):
    pass


class SDK:
    def __init__(self, config=None, **config_overrides):
        self.config = {}
        self.config.update({
            'host': DEFAULT_HOST,
        })
        self.config.update(config)
        self.config.update(config_overrides)


class Entity:
    def __init__(self):
        self._host = DEFAULT_HOST
        self._session = requests.Session()
        self._auth_api_key = os.getenv("MBED_CLOUD_SDK_API_KEY")
        self._session.headers.update(
            {
                "Authorization": "Bearer %s" % self._auth_api_key,
                "UserAgent": utils.get_user_agent(),
            }
        )

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
        url = (self._host + path).format(**path_params)
        response = self._session.request(
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
