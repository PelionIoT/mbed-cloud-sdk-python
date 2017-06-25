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
    def __init__(self, after=None, has_more=None, object=None, limit=None, continuation_token=None, data=None):
        """
        SuccessfulResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'after': 'str',
            'has_more': 'bool',
            'object': 'str',
            'limit': 'int',
            'continuation_token': 'str',
            'data': 'list[Metric]'
        }

        self.attribute_map = {
            'after': 'after',
            'has_more': 'has_more',
            'object': 'object',
            'limit': 'limit',
            'continuation_token': 'continuation_token',
            'data': 'data'
        }

        self._after = after
        self._has_more = has_more
        self._object = object
        self._limit = limit
        self._continuation_token = continuation_token
        self._data = data

    @property
    def after(self):
        """
        Gets the after of this SuccessfulResponse.
        continuation_token included in the request or null.

        :return: The after of this SuccessfulResponse.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this SuccessfulResponse.
        continuation_token included in the request or null.

        :param after: The after of this SuccessfulResponse.
        :type: str
        """

        self._after = after

    @property
    def has_more(self):
        """
        Gets the has_more of this SuccessfulResponse.
        true when there are more results to fetch using the included continuation_token.

        :return: The has_more of this SuccessfulResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this SuccessfulResponse.
        true when there are more results to fetch using the included continuation_token.

        :param has_more: The has_more of this SuccessfulResponse.
        :type: bool
        """

        self._has_more = has_more

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
        limit used in the request to retrieve the results.

        :return: The limit of this SuccessfulResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this SuccessfulResponse.
        limit used in the request to retrieve the results.

        :param limit: The limit of this SuccessfulResponse.
        :type: int
        """

        self._limit = limit

    @property
    def continuation_token(self):
        """
        Gets the continuation_token of this SuccessfulResponse.
        token to use in after request parameter to fetch more results.

        :return: The continuation_token of this SuccessfulResponse.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """
        Sets the continuation_token of this SuccessfulResponse.
        token to use in after request parameter to fetch more results.

        :param continuation_token: The continuation_token of this SuccessfulResponse.
        :type: str
        """

        self._continuation_token = continuation_token

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
