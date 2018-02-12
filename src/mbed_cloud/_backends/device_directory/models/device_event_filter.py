# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Mbed Device Directory service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceEventFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'date_time': 'datetime',
        'state_change': 'bool',
        'description': 'str',
        'device_id': 'str',
        'id': 'str',
        'event_type': 'str'
    }

    attribute_map = {
        'date_time': 'date_time',
        'state_change': 'state_change',
        'description': 'description',
        'device_id': 'device_id',
        'id': 'id',
        'event_type': 'event_type'
    }

    def __init__(self, date_time=None, state_change=None, description=None, device_id=None, id=None, event_type=None):
        """
        DeviceEventFilter - a model defined in Swagger
        """

        self._date_time = date_time
        self._state_change = state_change
        self._description = description
        self._device_id = device_id
        self._id = id
        self._event_type = event_type
        self.discriminator = None

    @property
    def date_time(self):
        """
        Gets the date_time of this DeviceEventFilter.

        :return: The date_time of this DeviceEventFilter.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this DeviceEventFilter.

        :param date_time: The date_time of this DeviceEventFilter.
        :type: datetime
        """

        self._date_time = date_time

    @property
    def state_change(self):
        """
        Gets the state_change of this DeviceEventFilter.

        :return: The state_change of this DeviceEventFilter.
        :rtype: bool
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        """
        Sets the state_change of this DeviceEventFilter.

        :param state_change: The state_change of this DeviceEventFilter.
        :type: bool
        """

        self._state_change = state_change

    @property
    def description(self):
        """
        Gets the description of this DeviceEventFilter.

        :return: The description of this DeviceEventFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceEventFilter.

        :param description: The description of this DeviceEventFilter.
        :type: str
        """

        self._description = description

    @property
    def device_id(self):
        """
        Gets the device_id of this DeviceEventFilter.

        :return: The device_id of this DeviceEventFilter.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this DeviceEventFilter.

        :param device_id: The device_id of this DeviceEventFilter.
        :type: str
        """

        self._device_id = device_id

    @property
    def id(self):
        """
        Gets the id of this DeviceEventFilter.

        :return: The id of this DeviceEventFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceEventFilter.

        :param id: The id of this DeviceEventFilter.
        :type: str
        """

        self._id = id

    @property
    def event_type(self):
        """
        Gets the event_type of this DeviceEventFilter.

        :return: The event_type of this DeviceEventFilter.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this DeviceEventFilter.

        :param event_type: The event_type of this DeviceEventFilter.
        :type: str
        """

        self._event_type = event_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DeviceEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
