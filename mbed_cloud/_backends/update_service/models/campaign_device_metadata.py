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


class CampaignDeviceMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, campaign=None, created_at=None, object=None, updated_at=None, mechanism=None, name=None, etag=None, mechanism_url=None, deployment_state=None, id=None, device_id=None):
        """
        CampaignDeviceMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'campaign': 'str',
            'created_at': 'datetime',
            'object': 'str',
            'updated_at': 'datetime',
            'mechanism': 'str',
            'name': 'str',
            'etag': 'str',
            'mechanism_url': 'str',
            'deployment_state': 'str',
            'id': 'str',
            'device_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'campaign': 'campaign',
            'created_at': 'created_at',
            'object': 'object',
            'updated_at': 'updated_at',
            'mechanism': 'mechanism',
            'name': 'name',
            'etag': 'etag',
            'mechanism_url': 'mechanism_url',
            'deployment_state': 'deployment_state',
            'id': 'id',
            'device_id': 'device_id'
        }

        self._description = description
        self._campaign = campaign
        self._created_at = created_at
        self._object = object
        self._updated_at = updated_at
        self._mechanism = mechanism
        self._name = name
        self._etag = etag
        self._mechanism_url = mechanism_url
        self._deployment_state = deployment_state
        self._id = id
        self._device_id = device_id

    @property
    def description(self):
        """
        Gets the description of this CampaignDeviceMetadata.
        Description

        :return: The description of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CampaignDeviceMetadata.
        Description

        :param description: The description of this CampaignDeviceMetadata.
        :type: str
        """

        self._description = description

    @property
    def campaign(self):
        """
        Gets the campaign of this CampaignDeviceMetadata.
        The ID of the campaign the device is in

        :return: The campaign of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this CampaignDeviceMetadata.
        The ID of the campaign the device is in

        :param campaign: The campaign of this CampaignDeviceMetadata.
        :type: str
        """

        self._campaign = campaign

    @property
    def created_at(self):
        """
        Gets the created_at of this CampaignDeviceMetadata.
        The time the campaign was created

        :return: The created_at of this CampaignDeviceMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CampaignDeviceMetadata.
        The time the campaign was created

        :param created_at: The created_at of this CampaignDeviceMetadata.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this CampaignDeviceMetadata.
        Entity name: always 'update-campaign-device-metadata'

        :return: The object of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CampaignDeviceMetadata.
        Entity name: always 'update-campaign-device-metadata'

        :param object: The object of this CampaignDeviceMetadata.
        :type: str
        """

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CampaignDeviceMetadata.
        This time this record was modified in the database format: date-time

        :return: The updated_at of this CampaignDeviceMetadata.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CampaignDeviceMetadata.
        This time this record was modified in the database format: date-time

        :param updated_at: The updated_at of this CampaignDeviceMetadata.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def mechanism(self):
        """
        Gets the mechanism of this CampaignDeviceMetadata.
        The mechanism used to deliver the firmware (connector or direct)

        :return: The mechanism of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this CampaignDeviceMetadata.
        The mechanism used to deliver the firmware (connector or direct)

        :param mechanism: The mechanism of this CampaignDeviceMetadata.
        :type: str
        """

        self._mechanism = mechanism

    @property
    def name(self):
        """
        Gets the name of this CampaignDeviceMetadata.
        The name of the record

        :return: The name of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignDeviceMetadata.
        The name of the record

        :param name: The name of this CampaignDeviceMetadata.
        :type: str
        """

        self._name = name

    @property
    def etag(self):
        """
        Gets the etag of this CampaignDeviceMetadata.
        API resource entity version

        :return: The etag of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CampaignDeviceMetadata.
        API resource entity version

        :param etag: The etag of this CampaignDeviceMetadata.
        :type: str
        """

        self._etag = etag

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this CampaignDeviceMetadata.
        The URL of cloud connect used

        :return: The mechanism_url of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this CampaignDeviceMetadata.
        The URL of cloud connect used

        :param mechanism_url: The mechanism_url of this CampaignDeviceMetadata.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def deployment_state(self):
        """
        Gets the deployment_state of this CampaignDeviceMetadata.
        The state of the update campaign on the device

        :return: The deployment_state of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._deployment_state

    @deployment_state.setter
    def deployment_state(self, deployment_state):
        """
        Sets the deployment_state of this CampaignDeviceMetadata.
        The state of the update campaign on the device

        :param deployment_state: The deployment_state of this CampaignDeviceMetadata.
        :type: str
        """
        allowed_values = ["pending", "updated_connector_channel", "failed_connector_channel_update", "deployed", "manifestremoved"]
        if deployment_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_state` ({0}), must be one of {1}"
                .format(deployment_state, allowed_values)
            )

        self._deployment_state = deployment_state

    @property
    def id(self):
        """
        Gets the id of this CampaignDeviceMetadata.
        The ID of the metadata record

        :return: The id of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignDeviceMetadata.
        The ID of the metadata record

        :param id: The id of this CampaignDeviceMetadata.
        :type: str
        """

        self._id = id

    @property
    def device_id(self):
        """
        Gets the device_id of this CampaignDeviceMetadata.
        The ID of the device

        :return: The device_id of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this CampaignDeviceMetadata.
        The ID of the device

        :param device_id: The device_id of this CampaignDeviceMetadata.
        :type: str
        """

        self._device_id = device_id

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
        if not isinstance(other, CampaignDeviceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
