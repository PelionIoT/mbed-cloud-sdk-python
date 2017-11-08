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


class ResourcesData(object):
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
        'path': 'str',
        'rf': 'str',
        'ct': 'str',
        'obs': 'bool',
        '_if': 'str'
    }

    attribute_map = {
        'path': 'path',
        'rf': 'rf',
        'ct': 'ct',
        'obs': 'obs',
        '_if': 'if'
    }

    def __init__(self, path=None, rf=None, ct=None, obs=None, _if=None):  # noqa: E501
        """ResourcesData - a model defined in Swagger"""  # noqa: E501

        self._path = path
        self._rf = rf
        self._ct = ct
        self._obs = obs
        self.__if = _if
        self.discriminator = None


    @property
    def path(self):
        """Gets the path of this ResourcesData.  # noqa: E501

        Resource's URI path.  # noqa: E501

        :return: The path of this ResourcesData.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ResourcesData.

        Resource's URI path.  # noqa: E501

        :param path: The path of this ResourcesData.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def rf(self):
        """Gets the rf of this ResourcesData.  # noqa: E501

        Resource type [created by the client side application](/docs/v1.2/collecting/resource-setup-in-mbed-cloud-client.html). For example \"speed_sensor\"  # noqa: E501

        :return: The rf of this ResourcesData.  # noqa: E501
        :rtype: str
        """
        return self._rf

    @rf.setter
    def rf(self, rf):
        """Sets the rf of this ResourcesData.

        Resource type [created by the client side application](/docs/v1.2/collecting/resource-setup-in-mbed-cloud-client.html). For example \"speed_sensor\"  # noqa: E501

        :param rf: The rf of this ResourcesData.  # noqa: E501
        :type: str
        """

        self._rf = rf

    @property
    def ct(self):
        """Gets the ct of this ResourcesData.  # noqa: E501

        Content type.  # noqa: E501

        :return: The ct of this ResourcesData.  # noqa: E501
        :rtype: str
        """
        return self._ct

    @ct.setter
    def ct(self, ct):
        """Sets the ct of this ResourcesData.

        Content type.  # noqa: E501

        :param ct: The ct of this ResourcesData.  # noqa: E501
        :type: str
        """

        self._ct = ct

    @property
    def obs(self):
        """Gets the obs of this ResourcesData.  # noqa: E501

        Whether the resource is observable or not (true/false).  # noqa: E501

        :return: The obs of this ResourcesData.  # noqa: E501
        :rtype: bool
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this ResourcesData.

        Whether the resource is observable or not (true/false).  # noqa: E501

        :param obs: The obs of this ResourcesData.  # noqa: E501
        :type: bool
        """

        self._obs = obs

    @property
    def _if(self):
        """Gets the _if of this ResourcesData.  # noqa: E501

        Interface description.  # noqa: E501

        :return: The _if of this ResourcesData.  # noqa: E501
        :rtype: str
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this ResourcesData.

        Interface description.  # noqa: E501

        :param _if: The _if of this ResourcesData.  # noqa: E501
        :type: str
        """

        self.__if = _if

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
        if not isinstance(other, ResourcesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
