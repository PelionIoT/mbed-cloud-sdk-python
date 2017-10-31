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


class TrustedCertificateResp(object):
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
        'service': 'str',
        'status': 'str',
        'description': 'str',
        'certificate': 'str',
        'issuer': 'str',
        'device_execution_mode': 'int',
        'created_at': 'datetime',
        'object': 'str',
        'subject': 'str',
        'account_id': 'str',
        'etag': 'str',
        'validity': 'datetime',
        'owner_id': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'service': 'service',
        'status': 'status',
        'description': 'description',
        'certificate': 'certificate',
        'issuer': 'issuer',
        'device_execution_mode': 'device_execution_mode',
        'created_at': 'created_at',
        'object': 'object',
        'subject': 'subject',
        'account_id': 'account_id',
        'etag': 'etag',
        'validity': 'validity',
        'owner_id': 'owner_id',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, service=None, status=None, description=None, certificate=None, issuer=None, device_execution_mode=None, created_at=None, object=None, subject=None, account_id=None, etag=None, validity=None, owner_id=None, id=None, name=None):
        """
        TrustedCertificateResp - a model defined in Swagger
        """

        self._service = None
        self._status = None
        self._description = None
        self._certificate = None
        self._issuer = None
        self._device_execution_mode = None
        self._created_at = None
        self._object = None
        self._subject = None
        self._account_id = None
        self._etag = None
        self._validity = None
        self._owner_id = None
        self._id = None
        self._name = None

        self.service = service
        if status is not None:
          self.status = status
        if description is not None:
          self.description = description
        self.certificate = certificate
        self.issuer = issuer
        if device_execution_mode is not None:
          self.device_execution_mode = device_execution_mode
        if created_at is not None:
          self.created_at = created_at
        self.object = object
        self.subject = subject
        self.account_id = account_id
        self.etag = etag
        self.validity = validity
        if owner_id is not None:
          self.owner_id = owner_id
        self.id = id
        self.name = name

    @property
    def service(self):
        """
        Gets the service of this TrustedCertificateResp.
        Service name where the certificate is to be used.

        :return: The service of this TrustedCertificateResp.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this TrustedCertificateResp.
        Service name where the certificate is to be used.

        :param service: The service of this TrustedCertificateResp.
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")
        allowed_values = ["lwm2m", "bootstrap"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def status(self):
        """
        Gets the status of this TrustedCertificateResp.
        Status of the certificate.

        :return: The status of this TrustedCertificateResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TrustedCertificateResp.
        Status of the certificate.

        :param status: The status of this TrustedCertificateResp.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def description(self):
        """
        Gets the description of this TrustedCertificateResp.
        Human readable description of this certificate.

        :return: The description of this TrustedCertificateResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TrustedCertificateResp.
        Human readable description of this certificate.

        :param description: The description of this TrustedCertificateResp.
        :type: str
        """

        self._description = description

    @property
    def certificate(self):
        """
        Gets the certificate of this TrustedCertificateResp.
        X509.v3 trusted certificate in PEM format.

        :return: The certificate of this TrustedCertificateResp.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this TrustedCertificateResp.
        X509.v3 trusted certificate in PEM format.

        :param certificate: The certificate of this TrustedCertificateResp.
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")

        self._certificate = certificate

    @property
    def issuer(self):
        """
        Gets the issuer of this TrustedCertificateResp.
        Issuer of the certificate.

        :return: The issuer of this TrustedCertificateResp.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this TrustedCertificateResp.
        Issuer of the certificate.

        :param issuer: The issuer of this TrustedCertificateResp.
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def device_execution_mode(self):
        """
        Gets the device_execution_mode of this TrustedCertificateResp.
        Device execution mode where 1 means a developer certificate.

        :return: The device_execution_mode of this TrustedCertificateResp.
        :rtype: int
        """
        return self._device_execution_mode

    @device_execution_mode.setter
    def device_execution_mode(self, device_execution_mode):
        """
        Sets the device_execution_mode of this TrustedCertificateResp.
        Device execution mode where 1 means a developer certificate.

        :param device_execution_mode: The device_execution_mode of this TrustedCertificateResp.
        :type: int
        """

        self._device_execution_mode = device_execution_mode

    @property
    def created_at(self):
        """
        Gets the created_at of this TrustedCertificateResp.
        Creation UTC time RFC3339.

        :return: The created_at of this TrustedCertificateResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this TrustedCertificateResp.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this TrustedCertificateResp.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this TrustedCertificateResp.
        Entity name: always 'trusted-cert'

        :return: The object of this TrustedCertificateResp.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this TrustedCertificateResp.
        Entity name: always 'trusted-cert'

        :param object: The object of this TrustedCertificateResp.
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
    def subject(self):
        """
        Gets the subject of this TrustedCertificateResp.
        Subject of the certificate.

        :return: The subject of this TrustedCertificateResp.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this TrustedCertificateResp.
        Subject of the certificate.

        :param subject: The subject of this TrustedCertificateResp.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def account_id(self):
        """
        Gets the account_id of this TrustedCertificateResp.
        The UUID of the account.

        :return: The account_id of this TrustedCertificateResp.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this TrustedCertificateResp.
        The UUID of the account.

        :param account_id: The account_id of this TrustedCertificateResp.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def etag(self):
        """
        Gets the etag of this TrustedCertificateResp.
        API resource entity version.

        :return: The etag of this TrustedCertificateResp.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this TrustedCertificateResp.
        API resource entity version.

        :param etag: The etag of this TrustedCertificateResp.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def validity(self):
        """
        Gets the validity of this TrustedCertificateResp.
        Expiration time in UTC formatted as RFC3339.

        :return: The validity of this TrustedCertificateResp.
        :rtype: datetime
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this TrustedCertificateResp.
        Expiration time in UTC formatted as RFC3339.

        :param validity: The validity of this TrustedCertificateResp.
        :type: datetime
        """
        if validity is None:
            raise ValueError("Invalid value for `validity`, must not be `None`")

        self._validity = validity

    @property
    def owner_id(self):
        """
        Gets the owner_id of this TrustedCertificateResp.
        The UUID of the owner.

        :return: The owner_id of this TrustedCertificateResp.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this TrustedCertificateResp.
        The UUID of the owner.

        :param owner_id: The owner_id of this TrustedCertificateResp.
        :type: str
        """

        self._owner_id = owner_id

    @property
    def id(self):
        """
        Gets the id of this TrustedCertificateResp.
        Entity ID.

        :return: The id of this TrustedCertificateResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TrustedCertificateResp.
        Entity ID.

        :param id: The id of this TrustedCertificateResp.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this TrustedCertificateResp.
        Certificate name.

        :return: The name of this TrustedCertificateResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TrustedCertificateResp.
        Certificate name.

        :param name: The name of this TrustedCertificateResp.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

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
        if not isinstance(other, TrustedCertificateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
