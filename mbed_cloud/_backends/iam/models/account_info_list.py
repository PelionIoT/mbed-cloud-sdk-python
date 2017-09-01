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


class AccountInfoList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, after=None, has_more=None, total_count=None, object=None, limit=None, data=None, order=None):
        """
        AccountInfoList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'after': 'str',
            'has_more': 'bool',
            'total_count': 'int',
            'object': 'str',
            'limit': 'int',
            'data': 'list[AccountInfo]',
            'order': 'str'
        }

        self.attribute_map = {
            'after': 'after',
            'has_more': 'has_more',
            'total_count': 'total_count',
            'object': 'object',
            'limit': 'limit',
            'data': 'data',
            'order': 'order'
        }

        self._after = after
        self._has_more = has_more
        self._total_count = total_count
        self._object = object
        self._limit = limit
        self._data = data
        self._order = order

    @property
    def after(self):
        """
        Gets the after of this AccountInfoList.
        The entity ID to fetch after the given one.

        :return: The after of this AccountInfoList.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this AccountInfoList.
        The entity ID to fetch after the given one.

        :param after: The after of this AccountInfoList.
        :type: str
        """

        self._after = after

    @property
    def has_more(self):
        """
        Gets the has_more of this AccountInfoList.
        Flag indicating whether there is more results.

        :return: The has_more of this AccountInfoList.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this AccountInfoList.
        Flag indicating whether there is more results.

        :param has_more: The has_more of this AccountInfoList.
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this AccountInfoList.
        The total number or records, if requested. It might be returned also for small lists.

        :return: The total_count of this AccountInfoList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this AccountInfoList.
        The total number or records, if requested. It might be returned also for small lists.

        :param total_count: The total_count of this AccountInfoList.
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count

    @property
    def object(self):
        """
        Gets the object of this AccountInfoList.
        Entity name: always 'list'

        :return: The object of this AccountInfoList.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this AccountInfoList.
        Entity name: always 'list'

        :param object: The object of this AccountInfoList.
        :type: str
        """
        allowed_values = ["user", "api-key", "group", "account", "account-template", "trusted-cert", "list", "error", "agreement", "signed-agreement"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def limit(self):
        """
        Gets the limit of this AccountInfoList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :return: The limit of this AccountInfoList.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this AccountInfoList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :param limit: The limit of this AccountInfoList.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this AccountInfoList.
        A list of entities.

        :return: The data of this AccountInfoList.
        :rtype: list[AccountInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this AccountInfoList.
        A list of entities.

        :param data: The data of this AccountInfoList.
        :type: list[AccountInfo]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this AccountInfoList.
        The order of the records to return. Available values: ASC, DESC; by default ASC.

        :return: The order of this AccountInfoList.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AccountInfoList.
        The order of the records to return. Available values: ASC, DESC; by default ASC.

        :param order: The order of this AccountInfoList.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

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
        if not isinstance(other, AccountInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
