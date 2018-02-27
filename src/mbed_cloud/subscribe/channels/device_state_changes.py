from mbed_cloud.subscribe.channels.channel import ChannelSubscription, _API_CHANNELS
from mbed_cloud.subscribe.subscribe import expand_dict_as_keys


class DeviceStateChanges(ChannelSubscription):
    def __init__(self, device_id=None, **extra_filters):
        self._route_keys = expand_dict_as_keys(dict(
            channel=[
                _API_CHANNELS.de_registrations,
                _API_CHANNELS.reg_updates,
                _API_CHANNELS.registrations_expired,
                _API_CHANNELS.registrations,
            ],
        ))
        self._optional_filters = {}
        if device_id is not None:
            self._optional_filters['device_id'] = device_id
        self._optional_filters.update(extra_filters)
        self._optional_filter_keys = expand_dict_as_keys(self._optional_filters)

    def start(self):
        """Start the channel"""
        super(DeviceStateChanges, self).start()
        # n.b. No true start/stop implementation as DeviceState is permanently subscribed
        self._api.ensure_notifications_thread()
