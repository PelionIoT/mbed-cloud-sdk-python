"""Tests for the Client Interface of the SDK Instance."""

import httpretty
import six

from tests.common import BaseCase
from mbed_cloud import SDK


MOCK_PATH = "/foo/bar"

@httpretty.activate
class TestClient(BaseCase):
    """Test creation of API filters."""

    @classmethod
    def setUpClass(cls):
        cls.client = SDK().client

    def setUp(self):
        httpretty.register_uri(
            httpretty.GET,
            self.client.config.host + MOCK_PATH,
            body='{"origin": "127.0.0.1"}'
        )

    def test_standard_headers(self):
        self.client.call_api("GET", MOCK_PATH, content_type="application/pelion")
        last_request = httpretty.last_request()

        self.assertEqual("Bearer " + self.client.config.api_key, last_request.headers["Authorization"])
        self.assertIn("mbed-cloud-sdk-python", last_request.headers["User-Agent"])
        self.assertEqual("application/pelion", last_request.headers["Content-Type"])

    def test_path_params(self):
        self.client.call_api("GET", "/foo/{variable}", path_params={"variable": "bar"})
        last_request = httpretty.last_request()

        self.assertEqual(last_request.path, MOCK_PATH)

    def test_json_message(self):
        self.client.call_api("GET", MOCK_PATH, body_params={"badger": "gopher"})

        last_request = httpretty.last_request()
        self.assertEqual(last_request.body, six.b('{"badger": "gopher"}'))
        self.assertEqual("application/json", last_request.headers["Content-Type"])

    def test_binary_message(self):
        binary_data = six.b('Badger Gopher Squirrel Ferret')
        self.client.call_api("GET", MOCK_PATH, binary_data=binary_data)

        last_request = httpretty.last_request()
        self.assertEqual(last_request.body, binary_data)
        self.assertEqual("binary/octet-stream", last_request.headers["Content-Type"])

    def test_multipart_message(self):
        file_stream = six.StringIO("Badger Gopher Squirrel Ferret")
        self.client.call_api("GET", MOCK_PATH, stream_params={"datafile": file_stream})

        last_request = httpretty.last_request()
        self.assertIn("Badger Gopher Squirrel Ferret", last_request.parsed_body)
        self.assertIn("multipart/form-data", last_request.headers["Content-Type"])
