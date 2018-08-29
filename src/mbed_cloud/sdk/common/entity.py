import inspect
import json

from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.sdk import SDK
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk.common import util
from mbed_cloud.sdk.common.sdk import get_or_create_global_sdk_instance
from mbed_cloud.sdk.common.logs import LOGGER


class Entity(object):
    _fieldnames = []
    _renames = {}

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
        return {
            field: getattr(self, "_" + field).to_literal() for field in self._fieldnames
        }

    def _from_api(self, **kwargs):
        for k, v in kwargs.items():
            field = getattr(self, "_" + self._renames.get(k, k), None)
            if field:
                if isinstance(field, fields.Field):
                    field.from_api(v)
                else:
                    print(repr(field))
                    print(v)

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
        unpack=None,
        **kwargs
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
            **kwargs
        )
        if unpack is None:
            unpack = self

        if response.status_code // 100 == 2:
            if unpack:
                if inspect.isclass(unpack):
                    unpack = unpack()  # noqa - we're going to instantiate it
                return unpack._from_api(**response.json())
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
                % util.pretty_literal(path_params)
            )
        hints = "\n".join(hints)
        try:
            content = json.loads(response.content)
        except Exception:
            self._logger.warning("Failed to unpack error body as json")
            content = {"response": content}
        else:
            # remap error response fields too!
            try:
                util.remap_error_fields(self._renames, content.get("fields", []))
            except Exception as e:
                self._logger.exception("Failed to remap fields")
        api_feedback = util.pretty_literal(content)

        # build and raise an Exception
        error = ApiErrorResponse(
            "Error response from API (HTTP %s):\n%s\n%s"
            % (response.status_code, api_feedback, hints)
        )
        error.content = content
        error.status_code = response.status_code
        error.raw = all_params.pop("response")
        error.all_parameters = all_params
        raise error
