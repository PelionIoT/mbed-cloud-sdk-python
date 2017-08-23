# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LoginHistory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, date=None, user_agent=None, ip_address=None, success=None):
        """
        LoginHistory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date': 'str',
            'user_agent': 'str',
            'ip_address': 'str',
            'success': 'bool'
        }

        self.attribute_map = {
            'date': 'date',
            'user_agent': 'userAgent',
            'ip_address': 'ipAddress',
            'success': 'success'
        }

        self._date = date
        self._user_agent = user_agent
        self._ip_address = ip_address
        self._success = success

    @property
    def date(self):
        """
        Gets the date of this LoginHistory.

        :return: The date of this LoginHistory.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this LoginHistory.

        :param date: The date of this LoginHistory.
        :type: str
        """

        self._date = date

    @property
    def user_agent(self):
        """
        Gets the user_agent of this LoginHistory.

        :return: The user_agent of this LoginHistory.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this LoginHistory.

        :param user_agent: The user_agent of this LoginHistory.
        :type: str
        """

        self._user_agent = user_agent

    @property
    def ip_address(self):
        """
        Gets the ip_address of this LoginHistory.

        :return: The ip_address of this LoginHistory.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this LoginHistory.

        :param ip_address: The ip_address of this LoginHistory.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def success(self):
        """
        Gets the success of this LoginHistory.

        :return: The success of this LoginHistory.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this LoginHistory.

        :param success: The success of this LoginHistory.
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, LoginHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
