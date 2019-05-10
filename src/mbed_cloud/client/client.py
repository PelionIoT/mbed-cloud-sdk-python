"""Client Interface
================

This provides direct access the Pelion Device Management API.

.. warning::
    It is not recommended that this is used directly, instead please use this class from an SDK instance
    (:mod:`mbed_cloud.sdk.sdk`).

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    response = pelion_dm_sdk.client.call_api(method="GET", path="/...")

------------
"""
import inspect
import json

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud import utils
from mbed_cloud.sdk import ApiErrorResponse
from mbed_cloud.client import util

import requests


class Client(object):
    """Client Interface to give direct access to the Pelion Device Management API."""

    def __init__(self, config):
        """An http client container

        :param config: An SDK configuration object.
        :type config: mbed_cloud.sdk.config.Config
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": "Bearer %s" % self.config.api_key,
                "User-Agent": utils.get_user_agent(),
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
        binary_data=None,
        content_type=None,
        unpack=None,
        **kwargs
    ):
        """Make an HTTP request handling to the Pelion Device Management REST API.

        This method uses the `Requests HTTP Library <http://docs.python-requests.org/en/master/>`_. to interact with the
        Pelion Device Management REST API. For more information on request and response objects please the third party
        documentation.

        .. code-block:: python

            from mbed_cloud import SDK
            pelion_dm_sdk = SDK()
            api_client = pelion_dm_sdk.client()

            response = api_client.call_api(
                method="put",
                path="/v3/path-to-resource/{an_id}",
                path_params={
                    "an_id": "0123456789"
                },
                body_params={
                    "a_field": "field value",
                },
                query_params={
                    "a_query_param": "query_param_value",
                }
             )

        :param method: HTTP Method
        :type method: str
        :param path: Path relative to the configured host (with variable substitution using `{format}` syntax)
        :type path: str
        :param headers: (optional) HTTP Headers (Auth is not required, Content-Type can be provided via content_type)
        :type headers: dict
        :param path_params: (optional) Path parameters (substituted into the `path` parameter)
        :type path_params: dict
        :param query_params: (optional) Query Parameters
        :type query_params: dict
        :param body_params: (optional) JSON-compatible Message Body
        :type body_params: dict
        :param stream_params: (optional) Files for multipart encoding uploading, see 'requests.request.files` for more
            information.
        :type stream_params: dict
        :param binary_data: (optional) Binary data suitable for binary/octet-stream content type.
        :type binary_data: str/byte
        :param content_type: (optional) Content-Type of the request, if defined this will be added to the HTTP Headers.
        :type content_type: str
        :param unpack: (optional) Unpack the response into this Entity
        :type unpack: mbed_cloud.foundation.common.entity_base.Entity
        :param kwargs: (optional) Addition parameters to be passed to `requests.Session().request`
        :return: Either a response object or an Entity instance
        :rtype: mbed_cloud.foundation.common.entity_base.Entity requests.Response
        """
        url = self.config.host + path

        if path_params:
            url = url.format(**path_params)

        if binary_data and not content_type:
            content_type = "application/octet-stream"

        if content_type:
            if headers is None:
                headers = {}
            headers.update({"Content-Type": content_type})

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body_params,
            data=binary_data,
            files=stream_params,
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
                if isinstance(unpack, Entity):
                    # If nothing is returned from the API but the response should be unpacked into an Entity, then
                    # return the original entity instance. Some endpoints do not return a created or modified instance
                    # on POST or PUT, which is out of spec but handle it.
                    return unpack
                else:
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
