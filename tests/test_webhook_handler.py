import json
import time

import mock

from tests.common import BaseCase
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.notifications import AsyncConsumer


class Test(BaseCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ConnectAPI()

    def test_async_response(self):
        asyncid = 'w349yw4ti7y34ti7eghiey54t'

        # make a fake listener
        result = AsyncConsumer(asyncid, self.api._db)
        self.assertFalse(result.is_done)

        # fake a response coming from a webhook receiver
        json_payload = json.dumps({
            'async-responses': [{
                'id': asyncid,
                'status': 1,
                'ct': 'tlv',
                'payload': "Q2hhbmdlIG1lIQ=="
            }]
        })
        self.api.notify_webhook_received(payload=json_payload)
        self.assertTrue(result.is_done)
        # FIXME: heh, looks like TLV comes out funny. Raw b64 would be 'Change me!?'
        self.assertEqual(result.value, {'104': 'ang', '8301': 'e!'})
        self.assertEqual(result.async_id, asyncid)

    def test_subscription_response(self):
        """Checks the behaviour of notification system when used with subscriptions

        They're different to get_resource_value, and use callbacks for some reason
        We patch the API call as we don't care about actually making a request
        Our callback is serviced by the random thread made in `add_resource_subscription_async`
        So we have to wait a bit for that to occur
        """
        path = '3200/0/5500'
        device_id = '015bb66a92a30000000000010010006d'

        mutable = []

        def some_callback(device_id, path, value, status=mutable):
            mutable.extend((device_id, path, value))

        with mock.patch('mbed_cloud._backends.mds.SubscriptionsApi.v2_subscriptions_device_id_resource_path_put'):
            self.api.add_resource_subscription_async(
                device_id=device_id,
                resource_path=path,
                callback_fn=some_callback
            )

        json_payload = json.dumps({
            'notifications': [{
                'ep': device_id,
                'path': path,
                'ct': 'tlv',
                'payload': "Q2hhbmdlIG1lIQ=="
            }]
        })
        self.api.notify_webhook_received(payload=json_payload)

        # FIXME: what a terrible api.
        timeout_seconds = 0.5
        delay = 0.02

        for i in range(int(timeout_seconds/delay)):
            if mutable:
                break
            time.sleep(delay)
        else:
            raise Exception('didnt see subscription after %s seconds' % timeout_seconds)

        self.assertEqual(mutable, [device_id, path, {'8301': 'e!', '104': 'ang'}])
