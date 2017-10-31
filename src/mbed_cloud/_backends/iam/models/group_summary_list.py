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


class GroupSummaryList(object):
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
        'data': 'list[GroupSummary]',
        'order': 'str'
    }

    attribute_map = {
        'after': 'after',
        'has_more': 'has_more',
        'total_count': 'total_count',
        'object': 'object',
        'limit': 'limit',
        'data': 'data',
        'order': 'order'
    }

    def __init__(self, after=None, has_more=None, total_count=None, object=None, limit=None, data=None, order=None):
        """
        GroupSummaryList - a model defined in Swagger
        """

        self._after = None
        self._has_more = None
        self._total_count = None
        self._object = None
        self._limit = None
        self._data = None
        self._order = None

        if after is not None:
          self.after = after
        self.has_more = has_more
        self.total_count = total_count
        self.object = object
        self.limit = limit
        self.data = data
        if order is not None:
          self.order = order

    @property
    def after(self):
        """
        Gets the after of this GroupSummaryList.
        The entity ID to fetch after the given one.

        :return: The after of this GroupSummaryList.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this GroupSummaryList.
        The entity ID to fetch after the given one.

        :param after: The after of this GroupSummaryList.
        :type: str
        """

        self._after = after

    @property
    def has_more(self):
        """
        Gets the has_more of this GroupSummaryList.
        Flag indicating whether there is more results.

        :return: The has_more of this GroupSummaryList.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this GroupSummaryList.
        Flag indicating whether there is more results.

        :param has_more: The has_more of this GroupSummaryList.
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this GroupSummaryList.
        The total number or records, if requested. It might be returned also for small lists.

        :return: The total_count of this GroupSummaryList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this GroupSummaryList.
        The total number or records, if requested. It might be returned also for small lists.

        :param total_count: The total_count of this GroupSummaryList.
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count

    @property
    def object(self):
        """
        Gets the object of this GroupSummaryList.
        Entity name: always 'list'

        :return: The object of this GroupSummaryList.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this GroupSummaryList.
        Entity name: always 'list'

        :param object: The object of this GroupSummaryList.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["user", "api-key", "group", "account", "account-template", "trusted-cert", "list", "error"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def limit(self):
        """
        Gets the limit of this GroupSummaryList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :return: The limit of this GroupSummaryList.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this GroupSummaryList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :param limit: The limit of this GroupSummaryList.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this GroupSummaryList.
        A list of entities.

        :return: The data of this GroupSummaryList.
        :rtype: list[GroupSummary]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this GroupSummaryList.
        A list of entities.

        :param data: The data of this GroupSummaryList.
        :type: list[GroupSummary]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this GroupSummaryList.
        The order of the records to return based on creation time. Available values: ASC, DESC; by default ASC.

        :return: The order of this GroupSummaryList.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this GroupSummaryList.
        The order of the records to return based on creation time. Available values: ASC, DESC; by default ASC.

        :param order: The order of this GroupSummaryList.
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
        if not isinstance(other, GroupSummaryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
