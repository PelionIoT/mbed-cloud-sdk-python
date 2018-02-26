from mbed_cloud.subscribe.subscribe import ChannelSubscription as _ChannelSubscription
from mbed_cloud.subscribe.subscribe import dict_to_frozen as _dict_to_frozen


class _API_CHANNELS:
    """API channels"""
    notifications = 'notifications'
    async_responses = 'async_responses'
    registrations = 'registrations'
    de_registrations = 'de_registrations'
    reg_updates = 'reg_updates'
    registrations_expired = 'registrations_expired'


class ResourceValueCurrent(_ChannelSubscription):
    def __init__(self, device_id, resource_path, **extra_filters):
        self._route_keys = _dict_to_frozen(dict(
            channel=_API_CHANNELS.async_responses,
        ))

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(ResourceValueCurrent, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(ResourceValueCurrent, self).ensure_stopped()


class ResourceValueChanges(_ChannelSubscription):
    def __init__(self, device_id, resource_path, **extra_filters):
        self._route_keys = _dict_to_frozen(dict(
            channel=_API_CHANNELS.notifications,
        ))

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(ResourceValueChanges, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(ResourceValueChanges, self).ensure_stopped()


class DeviceStateChanges(_ChannelSubscription):
    def __init__(self, device_id=None, **extra_filters):
        self._route_keys = _dict_to_frozen(dict(
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

    def ensure_started(self):
        """Start the channel (Idempotent)"""
        super(DeviceStateChanges, self).ensure_started()
        self.connect_api_instance._add_subscription(
            device_id,
            resource
        )

    def ensure_stopped(self):
        """Stop the channel (Idempotent)"""
        self.connect_api_instance._delete_subscription(
            device_id,
            resource
        )
        super(DeviceStateChanges, self).ensure_stopped()
