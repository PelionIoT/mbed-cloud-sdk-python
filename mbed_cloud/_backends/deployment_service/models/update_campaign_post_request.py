# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCampaignPostRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, when=None, object=None, root_manifest_id=None, state=None, device_filter=None, name=None):
        """
        UpdateCampaignPostRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'when': 'str',
            'object': 'str',
            'root_manifest_id': 'str',
            'state': 'str',
            'device_filter': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'when': 'when',
            'object': 'object',
            'root_manifest_id': 'root_manifest_id',
            'state': 'state',
            'device_filter': 'device_filter',
            'name': 'name'
        }

        self._description = description
        self._when = when
        self._object = object
        self._root_manifest_id = root_manifest_id
        self._state = state
        self._device_filter = device_filter
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateCampaignPostRequest.
        An optional description of the campaign.

        :return: The description of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCampaignPostRequest.
        An optional description of the campaign.

        :param description: The description of this UpdateCampaignPostRequest.
        :type: str
        """

        self._description = description

    @property
    def when(self):
        """
        Gets the when of this UpdateCampaignPostRequest.
        The timestamp at which update campaign scheduled to start.

        :return: The when of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._when

    @when.setter
    def when(self, when):
        """
        Sets the when of this UpdateCampaignPostRequest.
        The timestamp at which update campaign scheduled to start.

        :param when: The when of this UpdateCampaignPostRequest.
        :type: str
        """

        self._when = when

    @property
    def object(self):
        """
        Gets the object of this UpdateCampaignPostRequest.
        The API resource entity.

        :return: The object of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UpdateCampaignPostRequest.
        The API resource entity.

        :param object: The object of this UpdateCampaignPostRequest.
        :type: str
        """

        self._object = object

    @property
    def root_manifest_id(self):
        """
        Gets the root_manifest_id of this UpdateCampaignPostRequest.

        :return: The root_manifest_id of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._root_manifest_id

    @root_manifest_id.setter
    def root_manifest_id(self, root_manifest_id):
        """
        Sets the root_manifest_id of this UpdateCampaignPostRequest.

        :param root_manifest_id: The root_manifest_id of this UpdateCampaignPostRequest.
        :type: str
        """
        if root_manifest_id is not None and len(root_manifest_id) > 32:
            raise ValueError("Invalid value for `root_manifest_id`, length must be less than or equal to `32`")

        self._root_manifest_id = root_manifest_id

    @property
    def state(self):
        """
        Gets the state of this UpdateCampaignPostRequest.
        The state of the campaign.

        :return: The state of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateCampaignPostRequest.
        The state of the campaign.

        :param state: The state of this UpdateCampaignPostRequest.
        :type: str
        """
        allowed_values = ["draft", "scheduled", "devicefetch", "devicecopy", "devicecopycomplete", "publishing", "deploying", "deployed", "manifestremoved", "expired"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def device_filter(self):
        """
        Gets the device_filter of this UpdateCampaignPostRequest.
        The filter for the devices the campaign will target.

        :return: The device_filter of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """
        Sets the device_filter of this UpdateCampaignPostRequest.
        The filter for the devices the campaign will target.

        :param device_filter: The device_filter of this UpdateCampaignPostRequest.
        :type: str
        """
        if device_filter is None:
            raise ValueError("Invalid value for `device_filter`, must not be `None`")

        self._device_filter = device_filter

    @property
    def name(self):
        """
        Gets the name of this UpdateCampaignPostRequest.
        A name for this campaign.

        :return: The name of this UpdateCampaignPostRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCampaignPostRequest.
        A name for this campaign.

        :param name: The name of this UpdateCampaignPostRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

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
        if not isinstance(other, UpdateCampaignPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
