import inspect
import json

from mbed_cloud import utils
from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.sdk.common.config import Config
from mbed_cloud.sdk.common import util

import requests


class Client(object):
    def __init__(self, config):
        """An http client container

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

    def call_api(
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
        """Uses an http request handling mechanism to fetch and return results from the network

        :param method: http method
        :param path: the fully qualified path
            (with variable substitution defined in single brace `{format}` syntax)
        :param headers:
        :param path_params:
        :param query_params:
        :param body_params:
        :param stream_params:
        :param unpack: unpack response into this Entity
        :type unpack: mbed_cloud.sdk.common._entities.Entity
        :param kwargs: extras passed into the http client
        :return:
        """
        url = self.config.host + path

        if path_params:
            url = url.format(**path_params)

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body_params,
            files=stream_params,
            stream=bool(stream_params),
            **kwargs
        )

        # happy path - we successfully connect and receive a 2XX response:

        if response.status_code // 100 == 2:
            if not unpack:
                return response
            if inspect.isclass(unpack):
                unpack = unpack()  # noqa - we're going to instantiate it
            try:
                decoded = (response.content or {}) and response.json()
            except Exception as e:
                # TODO: support other content types here
                self.config.logger.error(
                    "Failed to unpack response body:\n%r", response.content
                )
                e.response = response
                raise e
            else:
                return unpack.from_api(**decoded)

        # else the response indicates an error, so the rest of this is error handling:

        # check for common failure causes
        all_params = locals()
        api_key = self.config.api_key or ""
        host = self.config.host
        hints = [
            "Request parameters:",
            "URL: %s" % url,
            "HTTP method: %s, api_key: '%s%s%s'"
            % (method.upper(), api_key[:6], "***" if api_key else "", api_key[-3:]),
            "Any additional parameters are attached to this %s instance."
            % ApiErrorResponse.__name__,
        ]
        if not api_key:
            hints.append(
                "There was no API key detected. You need to set one to interact with the cloud "
                "(See: https://cloud.mbed.com/docs/current/integrate-web-app/api-keys.html)."
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

        try:
            content = json.loads(response.content)
        except Exception:  # noqa
            # we don't care why loading the error content fails. maybe the API changed? log it.
            self.config.logger.warning("Failed to unpack error body as json")
            content = {"response": response.content}
        else:
            # remap error response fields too!
            try:
                if unpack:
                    fields = content.get("fields", [])
                    util.remap_error_fields(unpack._renames, fields)
                    for field in fields:
                        fieldname = (
                            field.get("name", "") if isinstance(field, dict) else field
                        )
                        hints.append(
                            "Docs for %r field:\n\t%s"
                            % (
                                fieldname,
                                getattr(unpack.__class__, fieldname, None).__doc__,
                            )
                        )
            except Exception:  # noqa
                # we don't care why remapping the field fails. we gave it a go! log it.
                self.config.logger.exception("Failed to remap fields")
        api_feedback = util.pretty_literal(content)

        hints = "\n".join(hints)

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
