# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoginHistory(object):
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
        'date': 'datetime',
        'ip_address': 'str',
        'user_agent': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'date': 'date',
        'ip_address': 'ip_address',
        'user_agent': 'user_agent',
        'success': 'success'
    }

    def __init__(self, date=None, ip_address=None, user_agent=None, success=None):  # noqa: E501
        """LoginHistory - a model defined in Swagger"""  # noqa: E501

        self._date = date
        self._ip_address = ip_address
        self._user_agent = user_agent
        self._success = success
        self.discriminator = None


    @property
    def date(self):
        """Gets the date of this LoginHistory.  # noqa: E501

        UTC time RFC3339 for this login attempt.  # noqa: E501

        :return: The date of this LoginHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this LoginHistory.

        UTC time RFC3339 for this login attempt.  # noqa: E501

        :param date: The date of this LoginHistory.  # noqa: E501
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def ip_address(self):
        """Gets the ip_address of this LoginHistory.  # noqa: E501

        IP address of the client.  # noqa: E501

        :return: The ip_address of this LoginHistory.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this LoginHistory.

        IP address of the client.  # noqa: E501

        :param ip_address: The ip_address of this LoginHistory.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def user_agent(self):
        """Gets the user_agent of this LoginHistory.  # noqa: E501

        User Agent header from the login request.  # noqa: E501

        :return: The user_agent of this LoginHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this LoginHistory.

        User Agent header from the login request.  # noqa: E501

        :param user_agent: The user_agent of this LoginHistory.  # noqa: E501
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")  # noqa: E501

        self._user_agent = user_agent

    @property
    def success(self):
        """Gets the success of this LoginHistory.  # noqa: E501

        Flag indicating whether login attempt was successful or not.  # noqa: E501

        :return: The success of this LoginHistory.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this LoginHistory.

        Flag indicating whether login attempt was successful or not.  # noqa: E501

        :param success: The success of this LoginHistory.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

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
        if not isinstance(other, LoginHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
