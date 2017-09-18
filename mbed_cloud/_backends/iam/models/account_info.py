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


class AccountInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, end_market=None, status=None, password_policy=None, postal_code=None, id=None, aliases=None, address_line2=None, city=None, address_line1=None, display_name=None, parent_id=None, state=None, etag=None, is_provisioning_allowed=None, email=None, phone_number=None, company=None, object=None, reason=None, upgraded_at=None, tier=None, sub_accounts=None, limits=None, country=None, created_at=None, idle_timeout=None, contact=None, policies=None, template_id=None):
        """
        AccountInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_market': 'str',
            'status': 'str',
            'password_policy': 'PasswordPolicy',
            'postal_code': 'str',
            'id': 'str',
            'aliases': 'list[str]',
            'address_line2': 'str',
            'city': 'str',
            'address_line1': 'str',
            'display_name': 'str',
            'parent_id': 'str',
            'state': 'str',
            'etag': 'str',
            'is_provisioning_allowed': 'bool',
            'email': 'str',
            'phone_number': 'str',
            'company': 'str',
            'object': 'str',
            'reason': 'str',
            'upgraded_at': 'datetime',
            'tier': 'str',
            'sub_accounts': 'list[AccountInfo]',
            'limits': 'dict(str, str)',
            'country': 'str',
            'created_at': 'datetime',
            'idle_timeout': 'str',
            'contact': 'str',
            'policies': 'list[FeaturePolicy]',
            'template_id': 'str'
        }

        self.attribute_map = {
            'end_market': 'end_market',
            'status': 'status',
            'password_policy': 'password_policy',
            'postal_code': 'postal_code',
            'id': 'id',
            'aliases': 'aliases',
            'address_line2': 'address_line2',
            'city': 'city',
            'address_line1': 'address_line1',
            'display_name': 'display_name',
            'parent_id': 'parent_id',
            'state': 'state',
            'etag': 'etag',
            'is_provisioning_allowed': 'is_provisioning_allowed',
            'email': 'email',
            'phone_number': 'phone_number',
            'company': 'company',
            'object': 'object',
            'reason': 'reason',
            'upgraded_at': 'upgraded_at',
            'tier': 'tier',
            'sub_accounts': 'sub_accounts',
            'limits': 'limits',
            'country': 'country',
            'created_at': 'created_at',
            'idle_timeout': 'idle_timeout',
            'contact': 'contact',
            'policies': 'policies',
            'template_id': 'template_id'
        }

        self._end_market = end_market
        self._status = status
        self._password_policy = password_policy
        self._postal_code = postal_code
        self._id = id
        self._aliases = aliases
        self._address_line2 = address_line2
        self._city = city
        self._address_line1 = address_line1
        self._display_name = display_name
        self._parent_id = parent_id
        self._state = state
        self._etag = etag
        self._is_provisioning_allowed = is_provisioning_allowed
        self._email = email
        self._phone_number = phone_number
        self._company = company
        self._object = object
        self._reason = reason
        self._upgraded_at = upgraded_at
        self._tier = tier
        self._sub_accounts = sub_accounts
        self._limits = limits
        self._country = country
        self._created_at = created_at
        self._idle_timeout = idle_timeout
        self._contact = contact
        self._policies = policies
        self._template_id = template_id

    @property
    def end_market(self):
        """
        Gets the end_market of this AccountInfo.
        Account end market.

        :return: The end_market of this AccountInfo.
        :rtype: str
        """
        return self._end_market

    @end_market.setter
    def end_market(self, end_market):
        """
        Sets the end_market of this AccountInfo.
        Account end market.

        :param end_market: The end_market of this AccountInfo.
        :type: str
        """
        if end_market is None:
            raise ValueError("Invalid value for `end_market`, must not be `None`")

        self._end_market = end_market

    @property
    def status(self):
        """
        Gets the status of this AccountInfo.
        The status of the account.

        :return: The status of this AccountInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AccountInfo.
        The status of the account.

        :param status: The status of this AccountInfo.
        :type: str
        """
        allowed_values = ["ENROLLING", "ACTIVE", "RESTRICTED", "SUSPENDED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def password_policy(self):
        """
        Gets the password_policy of this AccountInfo.
        The password policy for this account.

        :return: The password_policy of this AccountInfo.
        :rtype: PasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """
        Sets the password_policy of this AccountInfo.
        The password policy for this account.

        :param password_policy: The password_policy of this AccountInfo.
        :type: PasswordPolicy
        """

        self._password_policy = password_policy

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountInfo.
        The postal code part of the postal address.

        :return: The postal_code of this AccountInfo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountInfo.
        The postal code part of the postal address.

        :param postal_code: The postal_code of this AccountInfo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def id(self):
        """
        Gets the id of this AccountInfo.
        Account ID.

        :return: The id of this AccountInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccountInfo.
        Account ID.

        :param id: The id of this AccountInfo.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountInfo.
        An array of aliases.

        :return: The aliases of this AccountInfo.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountInfo.
        An array of aliases.

        :param aliases: The aliases of this AccountInfo.
        :type: list[str]
        """
        if aliases is None:
            raise ValueError("Invalid value for `aliases`, must not be `None`")

        self._aliases = aliases

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountInfo.
        Postal address line 2.

        :return: The address_line2 of this AccountInfo.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountInfo.
        Postal address line 2.

        :param address_line2: The address_line2 of this AccountInfo.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """
        Gets the city of this AccountInfo.
        The city part of the postal address.

        :return: The city of this AccountInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountInfo.
        The city part of the postal address.

        :param city: The city of this AccountInfo.
        :type: str
        """

        self._city = city

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountInfo.
        Postal address line 1.

        :return: The address_line1 of this AccountInfo.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountInfo.
        Postal address line 1.

        :param address_line1: The address_line1 of this AccountInfo.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountInfo.
        The display name for the account.

        :return: The display_name of this AccountInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountInfo.
        The display name for the account.

        :param display_name: The display_name of this AccountInfo.
        :type: str
        """

        self._display_name = display_name

    @property
    def parent_id(self):
        """
        Gets the parent_id of this AccountInfo.
        The ID of the parent account, if it has any.

        :return: The parent_id of this AccountInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this AccountInfo.
        The ID of the parent account, if it has any.

        :param parent_id: The parent_id of this AccountInfo.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def state(self):
        """
        Gets the state of this AccountInfo.
        The state part of the postal address.

        :return: The state of this AccountInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountInfo.
        The state part of the postal address.

        :param state: The state of this AccountInfo.
        :type: str
        """

        self._state = state

    @property
    def etag(self):
        """
        Gets the etag of this AccountInfo.
        API resource entity version.

        :return: The etag of this AccountInfo.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this AccountInfo.
        API resource entity version.

        :param etag: The etag of this AccountInfo.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def is_provisioning_allowed(self):
        """
        Gets the is_provisioning_allowed of this AccountInfo.
        Flag (true/false) indicating whether Factory Tool is allowed to download or not.

        :return: The is_provisioning_allowed of this AccountInfo.
        :rtype: bool
        """
        return self._is_provisioning_allowed

    @is_provisioning_allowed.setter
    def is_provisioning_allowed(self, is_provisioning_allowed):
        """
        Sets the is_provisioning_allowed of this AccountInfo.
        Flag (true/false) indicating whether Factory Tool is allowed to download or not.

        :param is_provisioning_allowed: The is_provisioning_allowed of this AccountInfo.
        :type: bool
        """
        if is_provisioning_allowed is None:
            raise ValueError("Invalid value for `is_provisioning_allowed`, must not be `None`")

        self._is_provisioning_allowed = is_provisioning_allowed

    @property
    def email(self):
        """
        Gets the email of this AccountInfo.
        The company email address for this account.

        :return: The email of this AccountInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountInfo.
        The company email address for this account.

        :param email: The email of this AccountInfo.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountInfo.
        The phone number of the company.

        :return: The phone_number of this AccountInfo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountInfo.
        The phone number of the company.

        :param phone_number: The phone_number of this AccountInfo.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def company(self):
        """
        Gets the company of this AccountInfo.
        The name of the company.

        :return: The company of this AccountInfo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountInfo.
        The name of the company.

        :param company: The company of this AccountInfo.
        :type: str
        """

        self._company = company

    @property
    def object(self):
        """
        Gets the object of this AccountInfo.
        Entity name: always 'account'

        :return: The object of this AccountInfo.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this AccountInfo.
        Entity name: always 'account'

        :param object: The object of this AccountInfo.
        :type: str
        """
        allowed_values = ["user", "api-key", "group", "account", "account-template", "trusted-cert", "list", "error"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def reason(self):
        """
        Gets the reason of this AccountInfo.
        A reason note for updating the status of the account

        :return: The reason of this AccountInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this AccountInfo.
        A reason note for updating the status of the account

        :param reason: The reason of this AccountInfo.
        :type: str
        """

        self._reason = reason

    @property
    def upgraded_at(self):
        """
        Gets the upgraded_at of this AccountInfo.
        Time when upgraded to commercial account in UTC format RFC3339.

        :return: The upgraded_at of this AccountInfo.
        :rtype: datetime
        """
        return self._upgraded_at

    @upgraded_at.setter
    def upgraded_at(self, upgraded_at):
        """
        Sets the upgraded_at of this AccountInfo.
        Time when upgraded to commercial account in UTC format RFC3339.

        :param upgraded_at: The upgraded_at of this AccountInfo.
        :type: datetime
        """

        self._upgraded_at = upgraded_at

    @property
    def tier(self):
        """
        Gets the tier of this AccountInfo.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future.

        :return: The tier of this AccountInfo.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this AccountInfo.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future.

        :param tier: The tier of this AccountInfo.
        :type: str
        """
        if tier is None:
            raise ValueError("Invalid value for `tier`, must not be `None`")

        self._tier = tier

    @property
    def sub_accounts(self):
        """
        Gets the sub_accounts of this AccountInfo.
        List of sub accounts.

        :return: The sub_accounts of this AccountInfo.
        :rtype: list[AccountInfo]
        """
        return self._sub_accounts

    @sub_accounts.setter
    def sub_accounts(self, sub_accounts):
        """
        Sets the sub_accounts of this AccountInfo.
        List of sub accounts.

        :param sub_accounts: The sub_accounts of this AccountInfo.
        :type: list[AccountInfo]
        """

        self._sub_accounts = sub_accounts

    @property
    def limits(self):
        """
        Gets the limits of this AccountInfo.
        List of limits as key-value pairs if requested.

        :return: The limits of this AccountInfo.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this AccountInfo.
        List of limits as key-value pairs if requested.

        :param limits: The limits of this AccountInfo.
        :type: dict(str, str)
        """

        self._limits = limits

    @property
    def country(self):
        """
        Gets the country of this AccountInfo.
        The country part of the postal address.

        :return: The country of this AccountInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountInfo.
        The country part of the postal address.

        :param country: The country of this AccountInfo.
        :type: str
        """

        self._country = country

    @property
    def created_at(self):
        """
        Gets the created_at of this AccountInfo.
        Creation UTC time RFC3339.

        :return: The created_at of this AccountInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this AccountInfo.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this AccountInfo.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def idle_timeout(self):
        """
        Gets the idle_timeout of this AccountInfo.
        The reference token expiration time in minutes for this account.

        :return: The idle_timeout of this AccountInfo.
        :rtype: str
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """
        Sets the idle_timeout of this AccountInfo.
        The reference token expiration time in minutes for this account.

        :param idle_timeout: The idle_timeout of this AccountInfo.
        :type: str
        """

        self._idle_timeout = idle_timeout

    @property
    def contact(self):
        """
        Gets the contact of this AccountInfo.
        The name of the contact person for this account.

        :return: The contact of this AccountInfo.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountInfo.
        The name of the contact person for this account.

        :param contact: The contact of this AccountInfo.
        :type: str
        """

        self._contact = contact

    @property
    def policies(self):
        """
        Gets the policies of this AccountInfo.
        List of policies if requested.

        :return: The policies of this AccountInfo.
        :rtype: list[FeaturePolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this AccountInfo.
        List of policies if requested.

        :param policies: The policies of this AccountInfo.
        :type: list[FeaturePolicy]
        """

        self._policies = policies

    @property
    def template_id(self):
        """
        Gets the template_id of this AccountInfo.
        Account template ID.

        :return: The template_id of this AccountInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this AccountInfo.
        Account template ID.

        :param template_id: The template_id of this AccountInfo.
        :type: str
        """

        self._template_id = template_id

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
        if not isinstance(other, AccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
