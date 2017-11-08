# coding: utf-8

"""
    Connect API

    Mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

mds/models.AsyncIDResponse  # noqa: F401,E501
mds/models.EndpointData  # noqa: F401,E501
mds/models.NotificationData  # noqa: F401,E501


class NotificationMessage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'async_responses': 'list[AsyncIDResponse]',
        'de_registrations': 'list[str]',
        'reg_updates': 'list[EndpointData]',
        'registrations': 'list[EndpointData]',
        'notifications': 'list[NotificationData]',
        'registrations_expired': 'list[str]'
    }

    attribute_map = {
        'async_responses': 'async-responses',
        'de_registrations': 'de-registrations',
        'reg_updates': 'reg-updates',
        'registrations': 'registrations',
        'notifications': 'notifications',
        'registrations_expired': 'registrations-expired'
    }

    def __init__(self, async_responses=None, de_registrations=None, reg_updates=None, registrations=None, notifications=None, registrations_expired=None):  # noqa: E501
        """NotificationMessage - a model defined in Swagger"""  # noqa: E501

        self._async_responses = async_responses
        self._de_registrations = de_registrations
        self._reg_updates = reg_updates
        self._registrations = registrations
        self._notifications = notifications
        self._registrations_expired = registrations_expired
        self.discriminator = None


    @property
    def async_responses(self):
        """Gets the async_responses of this NotificationMessage.  # noqa: E501


        :return: The async_responses of this NotificationMessage.  # noqa: E501
        :rtype: list[AsyncIDResponse]
        """
        return self._async_responses

    @async_responses.setter
    def async_responses(self, async_responses):
        """Sets the async_responses of this NotificationMessage.


        :param async_responses: The async_responses of this NotificationMessage.  # noqa: E501
        :type: list[AsyncIDResponse]
        """

        self._async_responses = async_responses

    @property
    def de_registrations(self):
        """Gets the de_registrations of this NotificationMessage.  # noqa: E501


        :return: The de_registrations of this NotificationMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._de_registrations

    @de_registrations.setter
    def de_registrations(self, de_registrations):
        """Sets the de_registrations of this NotificationMessage.


        :param de_registrations: The de_registrations of this NotificationMessage.  # noqa: E501
        :type: list[str]
        """

        self._de_registrations = de_registrations

    @property
    def reg_updates(self):
        """Gets the reg_updates of this NotificationMessage.  # noqa: E501


        :return: The reg_updates of this NotificationMessage.  # noqa: E501
        :rtype: list[EndpointData]
        """
        return self._reg_updates

    @reg_updates.setter
    def reg_updates(self, reg_updates):
        """Sets the reg_updates of this NotificationMessage.


        :param reg_updates: The reg_updates of this NotificationMessage.  # noqa: E501
        :type: list[EndpointData]
        """

        self._reg_updates = reg_updates

    @property
    def registrations(self):
        """Gets the registrations of this NotificationMessage.  # noqa: E501


        :return: The registrations of this NotificationMessage.  # noqa: E501
        :rtype: list[EndpointData]
        """
        return self._registrations

    @registrations.setter
    def registrations(self, registrations):
        """Sets the registrations of this NotificationMessage.


        :param registrations: The registrations of this NotificationMessage.  # noqa: E501
        :type: list[EndpointData]
        """

        self._registrations = registrations

    @property
    def notifications(self):
        """Gets the notifications of this NotificationMessage.  # noqa: E501


        :return: The notifications of this NotificationMessage.  # noqa: E501
        :rtype: list[NotificationData]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this NotificationMessage.


        :param notifications: The notifications of this NotificationMessage.  # noqa: E501
        :type: list[NotificationData]
        """

        self._notifications = notifications

    @property
    def registrations_expired(self):
        """Gets the registrations_expired of this NotificationMessage.  # noqa: E501


        :return: The registrations_expired of this NotificationMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._registrations_expired

    @registrations_expired.setter
    def registrations_expired(self, registrations_expired):
        """Sets the registrations_expired of this NotificationMessage.


        :param registrations_expired: The registrations_expired of this NotificationMessage.  # noqa: E501
        :type: list[str]
        """

        self._registrations_expired = registrations_expired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
