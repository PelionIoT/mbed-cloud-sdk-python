import json

from tests.common import BaseCase
from mbed_cloud.connect import ConnectAPI
from mbed_cloud.notifications import AsyncConsumer


class Test(BaseCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ConnectAPI()

    def test(self):
        asyncid = 'w349yw4ti7y34ti7eghiey54t'

        # make a fake listener
        result = AsyncConsumer(asyncid, self.api._db)
        self.assertFalse(result.is_done)

        # fake a response coming from a webhook receiver
        json_payload = json.dumps({
            'async-responses': [{
                'id': asyncid,
                'status': 1,
                'ct': "tlv",
                'payload': "Q2hhbmdlIG1lIQ=="
            }]
        })
        self.api.notify_webhook_received(payload=json_payload)
        self.assertTrue(result.is_done)
        self.assertEqual(result.value, {'8301': 'e!', '104': 'ang'})
        self.assertEqual(result.async_id, asyncid)
