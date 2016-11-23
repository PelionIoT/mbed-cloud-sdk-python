import logging
from collections import defaultdict

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI, config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk._backends.device_catalog as dc
from mbed_cloud_sdk._backends.device_catalog.rest import ApiException

logger = logging.getLogger(__name__)

class CatalogAPI(BaseAPI):
    def __init__(self, params = {}):
        super(CatalogAPI, self).__init__(params)

        # Set the api_key for the requests
        dc.configuration.api_key['Authorization'] = config.get("api_key")
        dc.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            dc.configuration.host = config.get("host")

    @catch_exceptions(ApiException)
    def list_devices(self):
        api = dc.DefaultApi()
        return api.device_list()
