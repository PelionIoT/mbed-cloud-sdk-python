# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

iam/models.LoginHistory  # noqa: F401,E501


class UserInfoResp(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'status': 'str',
        'username': 'str',
        'groups': 'list[str]',
        'password_changed_time': 'int',
        'email_verified': 'bool',
        'created_at': 'datetime',
        'object': 'str',
        'is_gtc_accepted': 'bool',
        'account_id': 'str',
        'email': 'str',
        'login_history': 'list[LoginHistory]',
        'is_totp_enabled': 'bool',
        'is_marketing_accepted': 'bool',
        'etag': 'str',
        'full_name': 'str',
        'address': 'str',
        'creation_time': 'int',
        'password': 'str',
        'phone_number': 'str',
        'id': 'str',
        'last_login_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'username': 'username',
        'groups': 'groups',
        'password_changed_time': 'password_changed_time',
        'email_verified': 'email_verified',
        'created_at': 'created_at',
        'object': 'object',
        'is_gtc_accepted': 'is_gtc_accepted',
        'account_id': 'account_id',
        'email': 'email',
        'login_history': 'login_history',
        'is_totp_enabled': 'is_totp_enabled',
        'is_marketing_accepted': 'is_marketing_accepted',
        'etag': 'etag',
        'full_name': 'full_name',
        'address': 'address',
        'creation_time': 'creation_time',
        'password': 'password',
        'phone_number': 'phone_number',
        'id': 'id',
        'last_login_time': 'last_login_time'
    }

    def __init__(self, status=None, username=None, groups=None, password_changed_time=None, email_verified=None, created_at=None, object=None, is_gtc_accepted=None, account_id=None, email=None, login_history=None, is_totp_enabled=None, is_marketing_accepted=None, etag=None, full_name=None, address=None, creation_time=None, password=None, phone_number=None, id=None, last_login_time=None):  # noqa: E501
        """UserInfoResp - a model defined in Swagger"""  # noqa: E501

        self._status = status
        self._username = username
        self._groups = groups
        self._password_changed_time = password_changed_time
        self._email_verified = email_verified
        self._created_at = created_at
        self._object = object
        self._is_gtc_accepted = is_gtc_accepted
        self._account_id = account_id
        self._email = email
        self._login_history = login_history
        self._is_totp_enabled = is_totp_enabled
        self._is_marketing_accepted = is_marketing_accepted
        self._etag = etag
        self._full_name = full_name
        self._address = address
        self._creation_time = creation_time
        self._password = password
        self._phone_number = phone_number
        self._id = id
        self._last_login_time = last_login_time
        self.discriminator = None


    @property
    def status(self):
        """Gets the status of this UserInfoResp.  # noqa: E501

        The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.  # noqa: E501

        :return: The status of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserInfoResp.

        The status of the user. ENROLLING state indicates that the user is in the middle of the enrollment process. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. INACTIVE users are locked out and not permitted to use the system.  # noqa: E501

        :param status: The status of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ENROLLING", "INVITED", "ACTIVE", "RESET", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def username(self):
        """Gets the username of this UserInfoResp.  # noqa: E501

        A username containing alphanumerical letters and -,._@+= characters.  # noqa: E501

        :return: The username of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserInfoResp.

        A username containing alphanumerical letters and -,._@+= characters.  # noqa: E501

        :param username: The username of this UserInfoResp.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def groups(self):
        """Gets the groups of this UserInfoResp.  # noqa: E501

        A list of IDs of the groups this user belongs to.  # noqa: E501

        :return: The groups of this UserInfoResp.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserInfoResp.

        A list of IDs of the groups this user belongs to.  # noqa: E501

        :param groups: The groups of this UserInfoResp.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def password_changed_time(self):
        """Gets the password_changed_time of this UserInfoResp.  # noqa: E501

        A timestamp of the latest change of the user password, in milliseconds.  # noqa: E501

        :return: The password_changed_time of this UserInfoResp.  # noqa: E501
        :rtype: int
        """
        return self._password_changed_time

    @password_changed_time.setter
    def password_changed_time(self, password_changed_time):
        """Sets the password_changed_time of this UserInfoResp.

        A timestamp of the latest change of the user password, in milliseconds.  # noqa: E501

        :param password_changed_time: The password_changed_time of this UserInfoResp.  # noqa: E501
        :type: int
        """

        self._password_changed_time = password_changed_time

    @property
    def email_verified(self):
        """Gets the email_verified of this UserInfoResp.  # noqa: E501

        A flag indicating whether the user's email address has been verified or not.  # noqa: E501

        :return: The email_verified of this UserInfoResp.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this UserInfoResp.

        A flag indicating whether the user's email address has been verified or not.  # noqa: E501

        :param email_verified: The email_verified of this UserInfoResp.  # noqa: E501
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def created_at(self):
        """Gets the created_at of this UserInfoResp.  # noqa: E501

        Creation UTC time RFC3339.  # noqa: E501

        :return: The created_at of this UserInfoResp.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInfoResp.

        Creation UTC time RFC3339.  # noqa: E501

        :param created_at: The created_at of this UserInfoResp.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """Gets the object of this UserInfoResp.  # noqa: E501

        Entity name: always 'user'  # noqa: E501

        :return: The object of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this UserInfoResp.

        Entity name: always 'user'  # noqa: E501

        :param object: The object of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        allowed_values = ["user", "api-key", "group", "account", "account-template", "trusted-cert", "list", "error"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def is_gtc_accepted(self):
        """Gets the is_gtc_accepted of this UserInfoResp.  # noqa: E501

        A flag indicating that the General Terms and Conditions has been accepted.  # noqa: E501

        :return: The is_gtc_accepted of this UserInfoResp.  # noqa: E501
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """Sets the is_gtc_accepted of this UserInfoResp.

        A flag indicating that the General Terms and Conditions has been accepted.  # noqa: E501

        :param is_gtc_accepted: The is_gtc_accepted of this UserInfoResp.  # noqa: E501
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def account_id(self):
        """Gets the account_id of this UserInfoResp.  # noqa: E501

        The UUID of the account.  # noqa: E501

        :return: The account_id of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UserInfoResp.

        The UUID of the account.  # noqa: E501

        :param account_id: The account_id of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def email(self):
        """Gets the email of this UserInfoResp.  # noqa: E501

        The email address.  # noqa: E501

        :return: The email of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInfoResp.

        The email address.  # noqa: E501

        :param email: The email of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def login_history(self):
        """Gets the login_history of this UserInfoResp.  # noqa: E501

        Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.  # noqa: E501

        :return: The login_history of this UserInfoResp.  # noqa: E501
        :rtype: list[LoginHistory]
        """
        return self._login_history

    @login_history.setter
    def login_history(self, login_history):
        """Sets the login_history of this UserInfoResp.

        Timestamps, succeedings, IP addresses and user agent information of the last five logins of the user, with timestamps in RFC3339 format.  # noqa: E501

        :param login_history: The login_history of this UserInfoResp.  # noqa: E501
        :type: list[LoginHistory]
        """

        self._login_history = login_history

    @property
    def is_totp_enabled(self):
        """Gets the is_totp_enabled of this UserInfoResp.  # noqa: E501

        A flag indicating whether 2-factor authentication (TOTP) has been enabled.  # noqa: E501

        :return: The is_totp_enabled of this UserInfoResp.  # noqa: E501
        :rtype: bool
        """
        return self._is_totp_enabled

    @is_totp_enabled.setter
    def is_totp_enabled(self, is_totp_enabled):
        """Sets the is_totp_enabled of this UserInfoResp.

        A flag indicating whether 2-factor authentication (TOTP) has been enabled.  # noqa: E501

        :param is_totp_enabled: The is_totp_enabled of this UserInfoResp.  # noqa: E501
        :type: bool
        """

        self._is_totp_enabled = is_totp_enabled

    @property
    def is_marketing_accepted(self):
        """Gets the is_marketing_accepted of this UserInfoResp.  # noqa: E501

        A flag indicating that receiving marketing information has been accepted.  # noqa: E501

        :return: The is_marketing_accepted of this UserInfoResp.  # noqa: E501
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """Sets the is_marketing_accepted of this UserInfoResp.

        A flag indicating that receiving marketing information has been accepted.  # noqa: E501

        :param is_marketing_accepted: The is_marketing_accepted of this UserInfoResp.  # noqa: E501
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def etag(self):
        """Gets the etag of this UserInfoResp.  # noqa: E501

        API resource entity version.  # noqa: E501

        :return: The etag of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this UserInfoResp.

        API resource entity version.  # noqa: E501

        :param etag: The etag of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")  # noqa: E501

        self._etag = etag

    @property
    def full_name(self):
        """Gets the full_name of this UserInfoResp.  # noqa: E501

        The full name of the user.  # noqa: E501

        :return: The full_name of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserInfoResp.

        The full name of the user.  # noqa: E501

        :param full_name: The full_name of this UserInfoResp.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def address(self):
        """Gets the address of this UserInfoResp.  # noqa: E501

        Address.  # noqa: E501

        :return: The address of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UserInfoResp.

        Address.  # noqa: E501

        :param address: The address of this UserInfoResp.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def creation_time(self):
        """Gets the creation_time of this UserInfoResp.  # noqa: E501

        A timestamp of the user creation in the storage, in milliseconds.  # noqa: E501

        :return: The creation_time of this UserInfoResp.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UserInfoResp.

        A timestamp of the user creation in the storage, in milliseconds.  # noqa: E501

        :param creation_time: The creation_time of this UserInfoResp.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def password(self):
        """Gets the password of this UserInfoResp.  # noqa: E501

        The password when creating a new user. It will be generated when not present in the request.  # noqa: E501

        :return: The password of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserInfoResp.

        The password when creating a new user. It will be generated when not present in the request.  # noqa: E501

        :param password: The password of this UserInfoResp.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone_number(self):
        """Gets the phone_number of this UserInfoResp.  # noqa: E501

        Phone number.  # noqa: E501

        :return: The phone_number of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this UserInfoResp.

        Phone number.  # noqa: E501

        :param phone_number: The phone_number of this UserInfoResp.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def id(self):
        """Gets the id of this UserInfoResp.  # noqa: E501

        The UUID of the user.  # noqa: E501

        :return: The id of this UserInfoResp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInfoResp.

        The UUID of the user.  # noqa: E501

        :param id: The id of this UserInfoResp.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_login_time(self):
        """Gets the last_login_time of this UserInfoResp.  # noqa: E501

        A timestamp of the latest login of the user, in milliseconds.  # noqa: E501

        :return: The last_login_time of this UserInfoResp.  # noqa: E501
        :rtype: int
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this UserInfoResp.

        A timestamp of the latest login of the user, in milliseconds.  # noqa: E501

        :param last_login_time: The last_login_time of this UserInfoResp.  # noqa: E501
        :type: int
        """

        self._last_login_time = last_login_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
