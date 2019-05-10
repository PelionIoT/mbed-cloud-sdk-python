"""Custom methods for device updae entities."""

from mbed_cloud import ApiFilter
from mbed_cloud.foundation import Device


def device_filter_helper_setter(self, value):
    """Create a campaign device filter from an API Filter

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.UpdateCampaign
    :param value: Device filter for campaign
    :type value: mbed_cloud.client.api_filter.ApiFilter
    """
    if isinstance(value, dict):
        value = ApiFilter(filter_definition=value, field_renames=Device._renames_to_api)
    elif isinstance(value, ApiFilter):
        value.field_renames = Device._renames_to_api
    elif value is not None:
        raise TypeError("This field may be either 'dict' or 'ApiFilter'.")
    # Store the filter as a dictionary for later retrieval if needed
    self._device_filter_helper.set(value.filter_definition)
    # Render the filter as a string for serialisation to the API
    self.device_filter = value.to_query_string()


def device_filter_helper_getter(self):
    """Return the configured campaign device filter.

    :param self: Instance of the entity for which this is a custom method.
    :type self: mbed_cloud.foundation.UpdateCampaign

    :rtype: mbed_cloud.client.api_filter.ApiFilter
    """
    return ApiFilter(filter_definition=self._device_filter_helper.value, field_renames=Device._renames_to_api)
