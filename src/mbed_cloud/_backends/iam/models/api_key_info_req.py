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


class ApiKeyInfoReq(object):
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
        'owner': 'str',
        'status': 'str',
        'name': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'owner': 'owner',
        'status': 'status',
        'name': 'name',
        'groups': 'groups'
    }

    def __init__(self, owner=None, status=None, name=None, groups=None):  # noqa: E501
        """ApiKeyInfoReq - a model defined in Swagger"""  # noqa: E501

        self._owner = owner
        self._status = status
        self._name = name
        self._groups = groups
        self.discriminator = None


    @property
    def owner(self):
        """Gets the owner of this ApiKeyInfoReq.  # noqa: E501

        The owner of this API key.  # noqa: E501

        :return: The owner of this ApiKeyInfoReq.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ApiKeyInfoReq.

        The owner of this API key.  # noqa: E501

        :param owner: The owner of this ApiKeyInfoReq.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def status(self):
        """Gets the status of this ApiKeyInfoReq.  # noqa: E501

        The status of the API key.  # noqa: E501

        :return: The status of this ApiKeyInfoReq.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiKeyInfoReq.

        The status of the API key.  # noqa: E501

        :param status: The status of this ApiKeyInfoReq.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def name(self):
        """Gets the name of this ApiKeyInfoReq.  # noqa: E501

        The display name for the API key, not longer than 100 characters.  # noqa: E501

        :return: The name of this ApiKeyInfoReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiKeyInfoReq.

        The display name for the API key, not longer than 100 characters.  # noqa: E501

        :param name: The name of this ApiKeyInfoReq.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def groups(self):
        """Gets the groups of this ApiKeyInfoReq.  # noqa: E501

        A list of group IDs this API key belongs to.  # noqa: E501

        :return: The groups of this ApiKeyInfoReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ApiKeyInfoReq.

        A list of group IDs this API key belongs to.  # noqa: E501

        :param groups: The groups of this ApiKeyInfoReq.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

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
        if not isinstance(other, ApiKeyInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
