"""Type hints"""
from mbed_cloud.subscribe.subscribe import ResourceValueCurrent

class SubscriptionsManagerBase:
    ResourceValueCurrent = None  # type: ResourceValueCurrent
    ResourceValueChanges = None  # type: ResourceValueChanges
    DeviceStateChanges = None  # type: DeviceStateChanges
