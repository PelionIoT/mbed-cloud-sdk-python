from mbed_cloud import BaseObject


class Presubscription(BaseObject):
    """Presubscription data object"""

    @staticmethod
    def _get_attributes_map():
        return {
            'device_id': 'endpoint-name',
            'device_type': 'endpoint-type',
            'resource_paths': 'resource-path',
        }

    @property
    def device_id(self):
        """The Device ID

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._device_id

    @property
    def device_type(self):
        """Device type of this Presubscription.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._device_type

    @property
    def resource_paths(self):
        """Resource paths of this Presubscription.

        :return: The url of this Webhook.
        :rtype: list[str]
        """
        return self._resource_paths