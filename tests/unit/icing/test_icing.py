from tests.common import BaseCase


class TestIcing(BaseCase):
    """
    Samples
    """

    '''
    namespaced by class nesting
    '''
    def test_client_root(self):
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = sdk.models.User
        p = u.phone_number # dynamic replacement class not introspectable :(

    def test_client_root_alt(self):
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = sdk.models2.User
        x = u() # functools.partial not introspectable :(
        p = x.phone_number

    def test_client_root_instances(self):
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = sdk.factory.user()
        p = u.phone_number  # instantiated object is introspectable

    def test_nested_instances(self):
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        r = sdk.factory.device().resource()
        v = r.kind

    '''
    namespaced by module
    '''
    def test_module_nested_instance(self):
        from mbed_cloud.sdk.api import Device
        d = Device()
        r = d.resource(device_id=d.id)
        v = r.kind

        # or

        from mbed_cloud.sdk.api import Resource
        r = Resource()
        v = r.kind

    def test_module_lazy(self):
        from mbed_cloud.sdk.api import User
        u = User()  # config loaded from global

    def test_module_explicit(self):
        from mbed_cloud.sdk.api import User
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = User(client=sdk)  # instantiated object is introspectable
        p = u.phone_number

    def test_module_lazy_explicit(self):
        from mbed_cloud.sdk.api import User
        from mbed_cloud.sdk.common import SDK
        sdk = SDK()
        u = User()  # instantiated object is introspectable
        u.client = sdk
        p = u.phone_number
