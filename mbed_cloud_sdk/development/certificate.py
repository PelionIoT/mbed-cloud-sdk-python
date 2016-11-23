import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI, config
from mbed_cloud_sdk.decorators import catch_exceptions

# Import backend API
import mbed_cloud_sdk._backends.developer_certificate as cert
import mbed_cloud_sdk._backends.developer_certificate.rest as ApiException

logger = logging.getLogger(__name__)

class CertificateAPI(BaseAPI):
    def __init__(self, params = {}):
        super(CertificateAPI, self).__init__(params)

        # Set the api_key for the requests
        cert.configuration.api_key['Authorization'] = config.get("api_key")
        cert.configuration.api_key_prefix['Authorization'] = 'Bearer'

        # Override host, if defined
        if config.get("host"):
            cert.configuration.host = config.get("host")

        # This API is a bit weird, so create the "authorization" string
        self.auth = "Bearer %s" % (config.get("api_key"),)

    @catch_exceptions(ApiException)
    def get_certificate(self):
        api = cert.DefaultApi()
        resp = api.v3_developer_certificate_get(self.auth)

        # Return None if the cert object is empty
        if resp.id:
            return resp
        return None

    @catch_exceptions(ApiException)
    def revoke_certificate(self):
        api = cert.DefaultApi()
        return api.v3_developer_certificate_delete(self.auth)

    @catch_exceptions(ApiException)
    def create_certificate(self, public_key):
        api = cert.DefaultApi()

        body = cert.Body()
        body.pub_key = public_key

        return api.v3_developer_certificate_post(self.auth, body)
