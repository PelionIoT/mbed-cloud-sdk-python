# coding: utf-8

"""
    Connect Statistics API

    mbed Cloud Connect Statistics API provides statistics about other cloud services through defined counters.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SuccessfulResponse(object):
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
        'after': 'str',
        'has_more': 'bool',
        'total_count': 'int',
        'object': 'str',
        'limit': 'int',
        'data': 'list[Metric]'
    }

    attribute_map = {
        'after': 'after',
        'has_more': 'has_more',
        'total_count': 'total_count',
        'object': 'object',
        'limit': 'limit',
        'data': 'data'
    }

    def __init__(self, after=None, has_more=None, total_count=None, object=None, limit=None, data=None):
        """
        SuccessfulResponse - a model defined in Swagger
        """

        self._after = after
        self._has_more = has_more
        self._total_count = total_count
        self._object = object
        self._limit = limit
        self._data = data
        self.discriminator = None

    @property
    def after(self):
        """
        Gets the after of this SuccessfulResponse.
        The metric ID included in the request or null.

        :return: The after of this SuccessfulResponse.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this SuccessfulResponse.
        The metric ID included in the request or null.

        :param after: The after of this SuccessfulResponse.
        :type: str
        """

        self._after = after

    @property
    def has_more(self):
        """
        Gets the has_more of this SuccessfulResponse.
        Indicates whether there are more results for you to fetch in the next page.

        :return: The has_more of this SuccessfulResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this SuccessfulResponse.
        Indicates whether there are more results for you to fetch in the next page.

        :param has_more: The has_more of this SuccessfulResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this SuccessfulResponse.
        The total number of records available.

        :return: The total_count of this SuccessfulResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this SuccessfulResponse.
        The total number of records available.

        :param total_count: The total_count of this SuccessfulResponse.
        :type: int
        """

        self._total_count = total_count

    @property
    def object(self):
        """
        Gets the object of this SuccessfulResponse.
        API resource name.

        :return: The object of this SuccessfulResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this SuccessfulResponse.
        API resource name.

        :param object: The object of this SuccessfulResponse.
        :type: str
        """

        self._object = object

    @property
    def limit(self):
        """
        Gets the limit of this SuccessfulResponse.
        The limit used in the request to retrieve the results.

        :return: The limit of this SuccessfulResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this SuccessfulResponse.
        The limit used in the request to retrieve the results.

        :param limit: The limit of this SuccessfulResponse.
        :type: int
        """

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this SuccessfulResponse.

        :return: The data of this SuccessfulResponse.
        :rtype: list[Metric]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this SuccessfulResponse.

        :param data: The data of this SuccessfulResponse.
        :type: list[Metric]
        """

        self._data = data

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
        if not isinstance(other, SuccessfulResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
