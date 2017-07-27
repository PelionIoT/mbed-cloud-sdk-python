# coding: utf-8

"""
    Update Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ManifestContentsDigestAlgorithm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, parameters=None, algorithm=None):
        """
        ManifestContentsDigestAlgorithm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parameters': 'str',
            'algorithm': 'str'
        }

        self.attribute_map = {
            'parameters': 'parameters',
            'algorithm': 'algorithm'
        }

        self._parameters = parameters
        self._algorithm = algorithm

    @property
    def parameters(self):
        """
        Gets the parameters of this ManifestContentsDigestAlgorithm.

        :return: The parameters of this ManifestContentsDigestAlgorithm.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ManifestContentsDigestAlgorithm.

        :param parameters: The parameters of this ManifestContentsDigestAlgorithm.
        :type: str
        """

        self._parameters = parameters

    @property
    def algorithm(self):
        """
        Gets the algorithm of this ManifestContentsDigestAlgorithm.

        :return: The algorithm of this ManifestContentsDigestAlgorithm.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this ManifestContentsDigestAlgorithm.

        :param algorithm: The algorithm of this ManifestContentsDigestAlgorithm.
        :type: str
        """

        self._algorithm = algorithm

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
        if not isinstance(other, ManifestContentsDigestAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
