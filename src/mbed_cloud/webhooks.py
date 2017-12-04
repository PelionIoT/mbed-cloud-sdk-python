from mbed_cloud import BaseObject


class Webhook(BaseObject):
    """Describes webhook object."""

    @staticmethod
    def _get_attributes_map():
        return {
            "url": "url",
            "headers": "headers",
        }

    @property
    def url(self):
        """Get the url of this Webhook.

        The URL to which the notifications are sent.
        We recommend that you serve this URL over HTTPS.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @property
    def headers(self):
        """Get the headers of this Webhook.

        Headers (key/value) that are sent with the notification. Optional.

        :return: The headers of this Webhook.
        :rtype: dict(str, str)
        """
        return self._headers