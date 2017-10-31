# coding: utf-8

"""
    Connect API

    mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ResourcesData(object):
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

    def __init__(self, path=None, rf=None, ct=None, obs=None, _if=None):
        """
        ResourcesData - a model defined in Swagger
        """

        self._path = None
        self._rf = None
        self._ct = None
        self._obs = None
        self.__if = None

        if path is not None:
          self.path = path
        if rf is not None:
          self.rf = rf
        if ct is not None:
          self.ct = ct
        if obs is not None:
          self.obs = obs
        if _if is not None:
          self._if = _if

    @property
    def path(self):
        """
        Gets the path of this ResourcesData.
        Resource's URI path.

        :return: The path of this ResourcesData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ResourcesData.
        Resource's URI path.

        :param path: The path of this ResourcesData.
        :type: str
        """

        self._path = path

    @property
    def rf(self):
        """
        Gets the rf of this ResourcesData.
        Resource type [created by Client side application](/docs/v1.2/collecting/resource-setup-in-mbed-cloud-client.html). For example \"speed_sensor\"

        :return: The rf of this ResourcesData.
        :rtype: str
        """
        return self._rf

    @rf.setter
    def rf(self, rf):
        """
        Sets the rf of this ResourcesData.
        Resource type [created by Client side application](/docs/v1.2/collecting/resource-setup-in-mbed-cloud-client.html). For example \"speed_sensor\"

        :param rf: The rf of this ResourcesData.
        :type: str
        """

        self._rf = rf

    @property
    def ct(self):
        """
        Gets the ct of this ResourcesData.
        Content type.

        :return: The ct of this ResourcesData.
        :rtype: str
        """
        return self._ct

    @ct.setter
    def ct(self, ct):
        """
        Sets the ct of this ResourcesData.
        Content type.

        :param ct: The ct of this ResourcesData.
        :type: str
        """

        self._ct = ct

    @property
    def obs(self):
        """
        Gets the obs of this ResourcesData.
        Whether the resource is observable or not (true/false).

        :return: The obs of this ResourcesData.
        :rtype: bool
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """
        Sets the obs of this ResourcesData.
        Whether the resource is observable or not (true/false).

        :param obs: The obs of this ResourcesData.
        :type: bool
        """

        self._obs = obs

    @property
    def _if(self):
        """
        Gets the _if of this ResourcesData.
        Interface description.

        :return: The _if of this ResourcesData.
        :rtype: str
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """
        Sets the _if of this ResourcesData.
        Interface description.

        :param _if: The _if of this ResourcesData.
        :type: str
        """

        self.__if = _if

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
        if not isinstance(other, ResourcesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
