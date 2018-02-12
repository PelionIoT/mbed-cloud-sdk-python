# coding: utf-8

"""
    Update Service API

    This is the API documentation for the Mbed deployment service, which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCampaignFilter(object):
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
        'description': 'str',
        'root_manifest_id': 'str',
        'created_at': 'datetime',
        'when': 'datetime',
        'updated_at': 'datetime',
        'state': 'str',
        'etag': 'datetime',
        'finished': 'datetime',
        'started_at': 'datetime',
        'id': 'str',
        'device_filter': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'root_manifest_id': 'root_manifest_id',
        'created_at': 'created_at',
        'when': 'when',
        'updated_at': 'updated_at',
        'state': 'state',
        'etag': 'etag',
        'finished': 'finished',
        'started_at': 'started_at',
        'id': 'id',
        'device_filter': 'device_filter',
        'name': 'name'
    }

    def __init__(self, description=None, root_manifest_id=None, created_at=None, when=None, updated_at=None, state=None, etag=None, finished=None, started_at=None, id=None, device_filter=None, name=None):
        """
        UpdateCampaignFilter - a model defined in Swagger
        """

        self._description = description
        self._root_manifest_id = root_manifest_id
        self._created_at = created_at
        self._when = when
        self._updated_at = updated_at
        self._state = state
        self._etag = etag
        self._finished = finished
        self._started_at = started_at
        self._id = id
        self._device_filter = device_filter
        self._name = name
        self.discriminator = None

    @property
    def description(self):
        """
        Gets the description of this UpdateCampaignFilter.

        :return: The description of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCampaignFilter.

        :param description: The description of this UpdateCampaignFilter.
        :type: str
        """

        self._description = description

    @property
    def root_manifest_id(self):
        """
        Gets the root_manifest_id of this UpdateCampaignFilter.

        :return: The root_manifest_id of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._root_manifest_id

    @root_manifest_id.setter
    def root_manifest_id(self, root_manifest_id):
        """
        Sets the root_manifest_id of this UpdateCampaignFilter.

        :param root_manifest_id: The root_manifest_id of this UpdateCampaignFilter.
        :type: str
        """

        self._root_manifest_id = root_manifest_id

    @property
    def created_at(self):
        """
        Gets the created_at of this UpdateCampaignFilter.

        :return: The created_at of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UpdateCampaignFilter.

        :param created_at: The created_at of this UpdateCampaignFilter.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def when(self):
        """
        Gets the when of this UpdateCampaignFilter.

        :return: The when of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._when

    @when.setter
    def when(self, when):
        """
        Sets the when of this UpdateCampaignFilter.

        :param when: The when of this UpdateCampaignFilter.
        :type: datetime
        """

        self._when = when

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UpdateCampaignFilter.

        :return: The updated_at of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UpdateCampaignFilter.

        :param updated_at: The updated_at of this UpdateCampaignFilter.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def state(self):
        """
        Gets the state of this UpdateCampaignFilter.

        :return: The state of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateCampaignFilter.

        :param state: The state of this UpdateCampaignFilter.
        :type: str
        """

        self._state = state

    @property
    def etag(self):
        """
        Gets the etag of this UpdateCampaignFilter.

        :return: The etag of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this UpdateCampaignFilter.

        :param etag: The etag of this UpdateCampaignFilter.
        :type: datetime
        """

        self._etag = etag

    @property
    def finished(self):
        """
        Gets the finished of this UpdateCampaignFilter.

        :return: The finished of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this UpdateCampaignFilter.

        :param finished: The finished of this UpdateCampaignFilter.
        :type: datetime
        """

        self._finished = finished

    @property
    def started_at(self):
        """
        Gets the started_at of this UpdateCampaignFilter.

        :return: The started_at of this UpdateCampaignFilter.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this UpdateCampaignFilter.

        :param started_at: The started_at of this UpdateCampaignFilter.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def id(self):
        """
        Gets the id of this UpdateCampaignFilter.

        :return: The id of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateCampaignFilter.

        :param id: The id of this UpdateCampaignFilter.
        :type: str
        """

        self._id = id

    @property
    def device_filter(self):
        """
        Gets the device_filter of this UpdateCampaignFilter.

        :return: The device_filter of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """
        Sets the device_filter of this UpdateCampaignFilter.

        :param device_filter: The device_filter of this UpdateCampaignFilter.
        :type: str
        """

        self._device_filter = device_filter

    @property
    def name(self):
        """
        Gets the name of this UpdateCampaignFilter.

        :return: The name of this UpdateCampaignFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCampaignFilter.

        :param name: The name of this UpdateCampaignFilter.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, UpdateCampaignFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
