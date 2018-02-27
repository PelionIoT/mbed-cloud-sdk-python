from mbed_cloud.subscribe.subscribe import expand_dict_as_keys as _expand_dict_as_keys
from mbed_cloud.subscribe.channels.channel import ChannelSubscription as _ChannelSubscription, _API_CHANNELS


class ResourceValueCurrent(_ChannelSubscription):
    def __init__(self, device_id, resource_path, **extra_filters):
        self.device_id = device_id
        self.resource_path = resource_path

        self._route_keys = _expand_dict_as_keys(dict(
            device_id=device_id,
            resource_path=resource_path,
            channel=_API_CHANNELS.async_responses,
        ))
        self._optional_filters = {}
        self._optional_filters.update(extra_filters)
        self._optional_filter_keys = _expand_dict_as_keys(self._optional_filters)

    def start(self):
        """Start the channel"""
        super(ResourceValueCurrent, self).start()
        self._api.ensure_notifications_thread()
        self._api._mds_rpc_post(
            device_id=self.device_id,
            method='GET',
            uri=self.resource_path,
        )
