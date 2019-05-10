"""
.. warning::
    Account should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: Account
==========================

Entities normally contain methods to create, read, update, delete and list resources. Other
actions may also be possible on the entity depending on the capabilities present in the API.
This entity has the following methods:

- :meth:`Account.api_keys`
- :meth:`Account.create`
- :meth:`Account.list`
- :meth:`Account.me`
- :meth:`Account.read`
- :meth:`Account.trusted_certificates`
- :meth:`Account.update`
- :meth:`Account.user_invitations`
- :meth:`Account.users`

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    accounts = pelion_dm_sdk.foundation.account()

How to import Account directly:

.. code-block:: python
    
    from mbed_cloud.foundation import Account

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class Account(Entity):
    """Represents the `Account` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "address_line1",
        "address_line2",
        "admin_email",
        "admin_full_name",
        "admin_id",
        "admin_key",
        "admin_name",
        "admin_password",
        "aliases",
        "city",
        "company",
        "contact",
        "contract_number",
        "country",
        "created_at",
        "custom_fields",
        "customer_number",
        "display_name",
        "email",
        "end_market",
        "expiration",
        "expiration_warning_threshold",
        "id",
        "idle_timeout",
        "limits",
        "mfa_status",
        "notification_emails",
        "parent_account",
        "parent_id",
        "password_policy",
        "password_recovery_expiration",
        "phone_number",
        "policies",
        "postal_code",
        "reason",
        "reference_note",
        "sales_contact",
        "state",
        "status",
        "template_id",
        "tier",
        "updated_at",
        "upgraded_at",
    ]

    # List of fields that are available for the user of the SDK
    _sdk_fieldnames = _api_fieldnames

    # Renames to be performed by the SDK when receiving data {<API Field Name>: <SDK Field Name>}
    _renames = {}

    # Renames to be performed by the SDK when sending data {<SDK Field Name>: <API Field Name>}
    _renames_to_api = {}

    def __init__(
        self,
        _client=None,
        address_line1=None,
        address_line2=None,
        admin_email=None,
        admin_full_name=None,
        admin_id=None,
        admin_key=None,
        admin_name=None,
        admin_password=None,
        aliases=None,
        city=None,
        company=None,
        contact=None,
        contract_number=None,
        country=None,
        created_at=None,
        custom_fields=None,
        customer_number=None,
        display_name=None,
        email=None,
        end_market=None,
        expiration=None,
        expiration_warning_threshold=None,
        id=None,
        idle_timeout=None,
        limits=None,
        mfa_status=None,
        notification_emails=None,
        parent_account=None,
        parent_id=None,
        password_policy=None,
        password_recovery_expiration=None,
        phone_number=None,
        policies=None,
        postal_code=None,
        reason=None,
        reference_note=None,
        sales_contact=None,
        state=None,
        status=None,
        template_id=None,
        tier=None,
        updated_at=None,
        upgraded_at=None,
    ):
        """Creates a local `Account` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param address_line1: Postal address line 1.
        :type address_line1: str
        :param address_line2: Postal address line 2.
        :type address_line2: str
        :param admin_email: The email address of the admin user created for this account.
            Present only in the response for account creation.
        :type admin_email: str
        :param admin_full_name: The full name of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_full_name: str
        :param admin_id: The ID of the admin user created for this account.
        :type admin_id: str
        :param admin_key: The admin API key created for this account. Present only in the
            response for account creation.
        :type admin_key: str
        :param admin_name: The username of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_name: str
        :param admin_password: The password of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_password: str
        :param aliases: An array of aliases.
        :type aliases: list
        :param city: The city part of the postal address.
        :type city: str
        :param company: The name of the company.
        :type company: str
        :param contact: The name of the contact person for this account.
        :type contact: str
        :param contract_number: Contract number of the customer.
        :type contract_number: str
        :param country: The country part of the postal address.
        :type country: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param custom_fields: Account's custom properties as key-value pairs.
        :type custom_fields: dict
        :param customer_number: Customer number of the customer.
        :type customer_number: str
        :param display_name: The display name for the account.
        :type display_name: str
        :param email: The company email address for this account.
        :type email: str
        :param end_market: (Required) Account end market.
        :type end_market: str
        :param expiration: Expiration time of the account, as UTC time RFC3339.
        :type expiration: datetime
        :param expiration_warning_threshold: Indicates how many days (1-180) before account expiration a
            notification email is sent.
        :type expiration_warning_threshold: int
        :param id: (Required) Account ID.
        :type id: str
        :param idle_timeout: The reference token expiration time, in minutes, for this account.
        :type idle_timeout: int
        :param limits: List of limits as key-value pairs if requested.
        :type limits: dict
        :param mfa_status: The enforcement status of multi-factor authentication, either
            `enforced` or `optional`.
        :type mfa_status: str
        :param notification_emails: A list of notification email addresses.
        :type notification_emails: list
        :param parent_account: Represents parent account contact details in responses.
        :type parent_account: dict
        :param parent_id: The ID of the parent account, if any.
        :type parent_id: str
        :param password_policy: The password policy for this account.
        :type password_policy: dict
        :param password_recovery_expiration: Indicates for how many minutes a password recovery email is valid.
        :type password_recovery_expiration: int
        :param phone_number: The phone number of a company representative.
        :type phone_number: str
        :param policies: List of policies if requested.
        :type policies: list
        :param postal_code: The postal code part of the postal address.
        :type postal_code: str
        :param reason: A note with the reason for account status update.
        :type reason: str
        :param reference_note: A reference note for updating the status of the account.
        :type reference_note: str
        :param sales_contact: Email address of the sales contact.
        :type sales_contact: str
        :param state: The state part of the postal address.
        :type state: str
        :param status: The status of the account.
        :type status: str
        :param template_id: Account template ID.
        :type template_id: str
        :param tier: The tier level of the account; `0`: free tier, `1`: commercial
            account, `2`: partner tier. Other values are reserved for the
            future.
        :type tier: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param upgraded_at: Time when upgraded to commercial account in UTC format RFC3339.
        :type upgraded_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.parent_account import ParentAccount
        from mbed_cloud.foundation.entities.accounts.password_policy import PasswordPolicy
        from mbed_cloud.foundation.entities.accounts.policy import Policy

        # fields
        self._address_line1 = fields.StringField(value=address_line1)
        self._address_line2 = fields.StringField(value=address_line2)
        self._admin_email = fields.StringField(value=admin_email)
        self._admin_full_name = fields.StringField(value=admin_full_name)
        self._admin_id = fields.StringField(value=admin_id)
        self._admin_key = fields.StringField(value=admin_key)
        self._admin_name = fields.StringField(value=admin_name)
        self._admin_password = fields.StringField(value=admin_password)
        self._aliases = fields.ListField(value=aliases)
        self._city = fields.StringField(value=city)
        self._company = fields.StringField(value=company)
        self._contact = fields.StringField(value=contact)
        self._contract_number = fields.StringField(value=contract_number)
        self._country = fields.StringField(value=country)
        self._created_at = fields.DateTimeField(value=created_at)
        self._custom_fields = fields.DictField(value=custom_fields)
        self._customer_number = fields.StringField(value=customer_number)
        self._display_name = fields.StringField(value=display_name)
        self._email = fields.StringField(value=email)
        self._end_market = fields.StringField(value=end_market)
        self._expiration = fields.DateTimeField(value=expiration)
        self._expiration_warning_threshold = fields.IntegerField(value=expiration_warning_threshold)
        self._id = fields.StringField(value=id)
        self._idle_timeout = fields.IntegerField(value=idle_timeout)
        self._limits = fields.DictField(value=limits)
        self._mfa_status = fields.StringField(value=mfa_status, enum=enums.AccountMfaStatusEnum)
        self._notification_emails = fields.ListField(value=notification_emails)
        self._parent_account = fields.DictField(value=parent_account, entity=ParentAccount)
        self._parent_id = fields.StringField(value=parent_id)
        self._password_policy = fields.DictField(value=password_policy, entity=PasswordPolicy)
        self._password_recovery_expiration = fields.IntegerField(value=password_recovery_expiration)
        self._phone_number = fields.StringField(value=phone_number)
        self._policies = fields.ListField(value=policies, entity=Policy)
        self._postal_code = fields.StringField(value=postal_code)
        self._reason = fields.StringField(value=reason)
        self._reference_note = fields.StringField(value=reference_note)
        self._sales_contact = fields.StringField(value=sales_contact)
        self._state = fields.StringField(value=state)
        self._status = fields.StringField(value=status, enum=enums.AccountStatusEnum)
        self._template_id = fields.StringField(value=template_id)
        self._tier = fields.StringField(value=tier)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._upgraded_at = fields.DateTimeField(value=upgraded_at)

    @property
    def address_line1(self):
        """Postal address line 1.
        
        api example: '110 Fulbourn Rd'
        
        :rtype: str
        """

        return self._address_line1.value

    @address_line1.setter
    def address_line1(self, value):
        """Set value of `address_line1`

        :param value: value to set
        :type value: str
        """

        self._address_line1.set(value)

    @property
    def address_line2(self):
        """Postal address line 2.
        
        api example: ' '
        
        :rtype: str
        """

        return self._address_line2.value

    @address_line2.setter
    def address_line2(self, value):
        """Set value of `address_line2`

        :param value: value to set
        :type value: str
        """

        self._address_line2.set(value)

    @property
    def admin_email(self):
        """The email address of the admin user created for this account. Present only in
        the response for account creation.
        
        api example: 'admin@arm.com'
        
        :rtype: str
        """

        return self._admin_email.value

    @admin_email.setter
    def admin_email(self, value):
        """Set value of `admin_email`

        :param value: value to set
        :type value: str
        """

        self._admin_email.set(value)

    @property
    def admin_full_name(self):
        """The full name of the admin user created for this account. Present only in the
        response for account creation.
        
        api example: 'Admin Doe'
        
        :rtype: str
        """

        return self._admin_full_name.value

    @admin_full_name.setter
    def admin_full_name(self, value):
        """Set value of `admin_full_name`

        :param value: value to set
        :type value: str
        """

        self._admin_full_name.set(value)

    @property
    def admin_id(self):
        """The ID of the admin user created for this account.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """

        return self._admin_id.value

    @property
    def admin_key(self):
        """The admin API key created for this account. Present only in the response for
        account creation.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac120006000000
            00B40IkJADMANmAscAj0Ot0n2yeQnyt9tT'
        
        :rtype: str
        """

        return self._admin_key.value

    @property
    def admin_name(self):
        """The username of the admin user created for this account. Present only in the
        response for account creation.
        
        api example: 'admin'
        
        :rtype: str
        """

        return self._admin_name.value

    @admin_name.setter
    def admin_name(self, value):
        """Set value of `admin_name`

        :param value: value to set
        :type value: str
        """

        self._admin_name.set(value)

    @property
    def admin_password(self):
        """The password of the admin user created for this account. Present only in the
        response for account creation.
        
        api example: 'PZf9eEUH43DAPE9ULINFeuj'
        
        :rtype: str
        """

        return self._admin_password.value

    @admin_password.setter
    def admin_password(self, value):
        """Set value of `admin_password`

        :param value: value to set
        :type value: str
        """

        self._admin_password.set(value)

    @property
    def aliases(self):
        """An array of aliases.
        
        :rtype: list
        """

        return self._aliases.value

    @aliases.setter
    def aliases(self, value):
        """Set value of `aliases`

        :param value: value to set
        :type value: list
        """

        self._aliases.set(value)

    @property
    def city(self):
        """The city part of the postal address.
        
        api example: 'Cambridge'
        
        :rtype: str
        """

        return self._city.value

    @city.setter
    def city(self, value):
        """Set value of `city`

        :param value: value to set
        :type value: str
        """

        self._city.set(value)

    @property
    def company(self):
        """The name of the company.
        
        api example: 'ARM Holdings Plc'
        
        :rtype: str
        """

        return self._company.value

    @company.setter
    def company(self, value):
        """Set value of `company`

        :param value: value to set
        :type value: str
        """

        self._company.set(value)

    @property
    def contact(self):
        """The name of the contact person for this account.
        
        api example: 'J. Doe'
        
        :rtype: str
        """

        return self._contact.value

    @contact.setter
    def contact(self, value):
        """Set value of `contact`

        :param value: value to set
        :type value: str
        """

        self._contact.set(value)

    @property
    def contract_number(self):
        """Contract number of the customer.
        
        api example: '1NX25_0001'
        
        :rtype: str
        """

        return self._contract_number.value

    @contract_number.setter
    def contract_number(self, value):
        """Set value of `contract_number`

        :param value: value to set
        :type value: str
        """

        self._contract_number.set(value)

    @property
    def country(self):
        """The country part of the postal address.
        
        api example: 'United Kingdom'
        
        :rtype: str
        """

        return self._country.value

    @country.setter
    def country(self, value):
        """Set value of `country`

        :param value: value to set
        :type value: str
        """

        self._country.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @property
    def custom_fields(self):
        """Account's custom properties as key-value pairs.
        
        :rtype: dict
        """

        return self._custom_fields.value

    @custom_fields.setter
    def custom_fields(self, value):
        """Set value of `custom_fields`

        :param value: value to set
        :type value: dict
        """

        self._custom_fields.set(value)

    @property
    def customer_number(self):
        """Customer number of the customer.
        
        api example: '1NC25_0001'
        
        :rtype: str
        """

        return self._customer_number.value

    @customer_number.setter
    def customer_number(self, value):
        """Set value of `customer_number`

        :param value: value to set
        :type value: str
        """

        self._customer_number.set(value)

    @property
    def display_name(self):
        """The display name for the account.
        
        api example: 'ARM'
        
        :rtype: str
        """

        return self._display_name.value

    @display_name.setter
    def display_name(self, value):
        """Set value of `display_name`

        :param value: value to set
        :type value: str
        """

        self._display_name.set(value)

    @property
    def email(self):
        """The company email address for this account.
        
        api example: 'info@arm.com'
        
        :rtype: str
        """

        return self._email.value

    @email.setter
    def email(self, value):
        """Set value of `email`

        :param value: value to set
        :type value: str
        """

        self._email.set(value)

    @property
    def end_market(self):
        """Account end market.

        This field must be set when creating a new Account Entity.
        
        api example: 'IT'
        
        :rtype: str
        """

        return self._end_market.value

    @end_market.setter
    def end_market(self, value):
        """Set value of `end_market`

        :param value: value to set
        :type value: str
        """

        self._end_market.set(value)

    @property
    def expiration(self):
        """Expiration time of the account, as UTC time RFC3339.
        
        :rtype: datetime
        """

        return self._expiration.value

    @property
    def expiration_warning_threshold(self):
        """Indicates how many days (1-180) before account expiration a notification email
        is sent.
        
        api example: '180'
        
        :rtype: int
        """

        return self._expiration_warning_threshold.value

    @expiration_warning_threshold.setter
    def expiration_warning_threshold(self, value):
        """Set value of `expiration_warning_threshold`

        :param value: value to set
        :type value: int
        """

        self._expiration_warning_threshold.set(value)

    @property
    def id(self):
        """Account ID.

        This field must be set when updating or deleting an existing Account Entity.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def idle_timeout(self):
        """The reference token expiration time, in minutes, for this account.
        
        api example: '30'
        
        :rtype: int
        """

        return self._idle_timeout.value

    @idle_timeout.setter
    def idle_timeout(self, value):
        """Set value of `idle_timeout`

        :param value: value to set
        :type value: int
        """

        self._idle_timeout.set(value)

    @property
    def limits(self):
        """List of limits as key-value pairs if requested.
        
        :rtype: dict
        """

        return self._limits.value

    @property
    def mfa_status(self):
        """The enforcement status of multi-factor authentication, either `enforced` or
        `optional`.
        
        :rtype: str
        """

        return self._mfa_status.value

    @mfa_status.setter
    def mfa_status(self, value):
        """Set value of `mfa_status`

        :param value: value to set
        :type value: str
        """

        self._mfa_status.set(value)

    @property
    def notification_emails(self):
        """A list of notification email addresses.
        
        :rtype: list
        """

        return self._notification_emails.value

    @notification_emails.setter
    def notification_emails(self, value):
        """Set value of `notification_emails`

        :param value: value to set
        :type value: list
        """

        self._notification_emails.set(value)

    @property
    def parent_account(self):
        """Represents parent account contact details in responses.
        
        :rtype: dict[ParentAccount]
        """

        return self._parent_account.value

    @property
    def parent_id(self):
        """The ID of the parent account, if any.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """

        return self._parent_id.value

    @property
    def password_policy(self):
        """The password policy for this account.
        
        :rtype: dict[PasswordPolicy]
        """

        return self._password_policy.value

    @password_policy.setter
    def password_policy(self, value):
        """Set value of `password_policy`

        :param value: value to set
        :type value: dict[PasswordPolicy]
        """

        self._password_policy.set(value)

    @property
    def password_recovery_expiration(self):
        """Indicates for how many minutes a password recovery email is valid.
        
        :rtype: int
        """

        return self._password_recovery_expiration.value

    @password_recovery_expiration.setter
    def password_recovery_expiration(self, value):
        """Set value of `password_recovery_expiration`

        :param value: value to set
        :type value: int
        """

        self._password_recovery_expiration.set(value)

    @property
    def phone_number(self):
        """The phone number of a company representative.
        
        api example: '+44 (1223) 400 400'
        
        :rtype: str
        """

        return self._phone_number.value

    @phone_number.setter
    def phone_number(self, value):
        """Set value of `phone_number`

        :param value: value to set
        :type value: str
        """

        self._phone_number.set(value)

    @property
    def policies(self):
        """List of policies if requested.
        
        :rtype: list[Policy]
        """

        return self._policies.value

    @property
    def postal_code(self):
        """The postal code part of the postal address.
        
        api example: 'CB1 9NJ'
        
        :rtype: str
        """

        return self._postal_code.value

    @postal_code.setter
    def postal_code(self, value):
        """Set value of `postal_code`

        :param value: value to set
        :type value: str
        """

        self._postal_code.set(value)

    @property
    def reason(self):
        """A note with the reason for account status update.
        
        api example: 'Subscription paid.'
        
        :rtype: str
        """

        return self._reason.value

    @property
    def reference_note(self):
        """A reference note for updating the status of the account.
        
        api example: 'ARM-INT-0001'
        
        :rtype: str
        """

        return self._reference_note.value

    @property
    def sales_contact(self):
        """Email address of the sales contact.
        
        api example: 'sales@arm.com'
        
        :rtype: str
        """

        return self._sales_contact.value

    @sales_contact.setter
    def sales_contact(self, value):
        """Set value of `sales_contact`

        :param value: value to set
        :type value: str
        """

        self._sales_contact.set(value)

    @property
    def state(self):
        """The state part of the postal address.
        
        api example: ' '
        
        :rtype: str
        """

        return self._state.value

    @state.setter
    def state(self, value):
        """Set value of `state`

        :param value: value to set
        :type value: str
        """

        self._state.set(value)

    @property
    def status(self):
        """The status of the account.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """

        return self._status.value

    @property
    def template_id(self):
        """Account template ID.
        
        api example: '01619571e7160242ac12000600000000'
        
        :rtype: str
        """

        return self._template_id.value

    @property
    def tier(self):
        """The tier level of the account; `0`: free tier, `1`: commercial account, `2`:
        partner tier. Other values are reserved for the future.
        
        api example: '1'
        
        :rtype: str
        """

        return self._tier.value

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @property
    def upgraded_at(self):
        """Time when upgraded to commercial account in UTC format RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._upgraded_at.value

    def api_keys(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get all API keys.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/api-keys>`_.

        **API Filters**

        The following filters are supported by the API when listing Account entities:

        +-------+------+------+------+------+------+------+------+
        | Field | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======+======+======+======+======+======+======+======+
        | key   | Y    |      |      |      |      |      |      |
        +-------+------+------+------+------+------+------+------+
        | owner | Y    |      |      |      |      |      |      |
        +-------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Account
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("key", "eq", <filter value>)
            for api_key in Account().api_keys(filter=api_filter):
                print(api_key.key)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantApiKey)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantApiKey
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantApiKey._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantApiKey._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantApiKey,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_api_keys,
        )

    def create(self, action="create"):
        """Create a new account.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts>`_.
        
        :param action: Action, either `create` or `enroll`.
            <ul>
            <li>`create` creates the
            account where its admin user has ACTIVE status if `admin_password` was
            defined in the request, or RESET status if no `admin_password` was
            defined. If the user already exists, its status is not modified. </li>
            <li>`enroll` creates the account where its admin user has ENROLLING
            status. If the user already exists, its status is not modified. Email
            to finish enrollment or notify the existing user about the new account
            is sent to the `admin_email` defined in the request. </li></ul>
        :type action: str
        
        :rtype: Account
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._address_line1.value_set:
            body_params["address_line1"] = self._address_line1.to_api()
        if self._address_line2.value_set:
            body_params["address_line2"] = self._address_line2.to_api()
        if self._admin_email.value_set:
            body_params["admin_email"] = self._admin_email.to_api()
        if self._admin_full_name.value_set:
            body_params["admin_full_name"] = self._admin_full_name.to_api()
        if self._admin_name.value_set:
            body_params["admin_name"] = self._admin_name.to_api()
        if self._admin_password.value_set:
            body_params["admin_password"] = self._admin_password.to_api()
        if self._aliases.value_set:
            body_params["aliases"] = self._aliases.to_api()
        if self._city.value_set:
            body_params["city"] = self._city.to_api()
        if self._company.value_set:
            body_params["company"] = self._company.to_api()
        if self._contact.value_set:
            body_params["contact"] = self._contact.to_api()
        if self._contract_number.value_set:
            body_params["contract_number"] = self._contract_number.to_api()
        if self._country.value_set:
            body_params["country"] = self._country.to_api()
        if self._customer_number.value_set:
            body_params["customer_number"] = self._customer_number.to_api()
        if self._display_name.value_set:
            body_params["display_name"] = self._display_name.to_api()
        if self._email.value_set:
            body_params["email"] = self._email.to_api()
        if self._end_market.value_set:
            body_params["end_market"] = self._end_market.to_api()
        if self._phone_number.value_set:
            body_params["phone_number"] = self._phone_number.to_api()
        if self._postal_code.value_set:
            body_params["postal_code"] = self._postal_code.to_api()
        if self._state.value_set:
            body_params["state"] = self._state.to_api()

        return self._client.call_api(
            method="post",
            path="/v3/accounts",
            content_type="application/json",
            query_params={"action": fields.StringField(action).to_api()},
            body_params=body_params,
            unpack=self,
        )

    def list(
        self, filter=None, order="ASC", max_results=None, page_size=1000, include=None, format=None, properties=None
    ):
        """Get all accounts.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts>`_.

        **API Filters**

        The following filters are supported by the API when listing Account entities:

        +------------+------+------+------+------+------+------+------+
        | Field      | eq   | neq  | gte  | lte  | in   | nin  | like |
        +============+======+======+======+======+======+======+======+
        | country    |      |      |      |      |      |      | Y    |
        +------------+------+------+------+------+------+------+------+
        | end_market | Y    |      |      |      |      |      |      |
        +------------+------+------+------+------+------+------+------+
        | parent     | Y    |      |      |      |      |      |      |
        +------------+------+------+------+------+------+------+------+
        | status     | Y    |      |      |      | Y    | Y    |      |
        +------------+------+------+------+------+------+------+------+
        | tier       | Y    |      |      |      |      |      |      |
        +------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Account
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("country", "like", <filter value>)
            for account in Account().list(filter=api_filter):
                print(account.country)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order. Acceptable values: ASC, DESC. Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 1000.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            limits, policies, sub_accounts.
        :type include: str
        
        :param format: Format information for the query response. Supported:
            format=breakdown.
        :type format: str
        
        :param properties: Property name returned from account-specific properties.
        :type properties: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(Account)
        """

        from mbed_cloud.foundation._custom_methods import paginate

        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=self._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = self._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=self.__class__,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            format=format,
            properties=properties,
            wraps=self._paginate_list,
        )

    def me(self, include=None, properties=None):
        """Get account info.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/me>`_.
        
        :param include: Comma-separated additional data to return. Currently supported:
            limits, policies, sub_accounts.
        :type include: str
        
        :param properties: Property name to return from account-specific properties.
        :type properties: str
        
        :rtype: Account
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/me",
            content_type="application/json",
            query_params={
                "include": fields.StringField(include).to_api(),
                "properties": fields.StringField(properties).to_api(),
            },
            unpack=self,
        )

    def _paginate_api_keys(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get all API keys.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.AccountOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/api-keys",
            content_type="application/json",
            query_params=query_params,
            path_params={"account_id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_list(
        self, after=None, filter=None, order="ASC", limit=1000, include=None, format=None, properties=None
    ):
        """Get all accounts.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order. Acceptable values: ASC, DESC. Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 1000.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            limits, policies, sub_accounts.
        :type include: str
        
        :param format: Format information for the query response. Supported:
            format=breakdown.
        :type format: str
        
        :param properties: Property name returned from account-specific properties.
        :type properties: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.AccountOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()
        query_params["format"] = fields.StringField(format).to_api()
        query_params["properties"] = fields.StringField(properties).to_api()

        return self._client.call_api(
            method="get", path="/v3/accounts", content_type="application/json", query_params=query_params, unpack=False
        )

    def _paginate_trusted_certificates(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get all trusted certificates.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.AccountOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/trusted-certificates",
            content_type="application/json",
            query_params=query_params,
            path_params={"account_id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_user_invitations(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get the details of all user invitations.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Not supported by the API.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.AccountOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/user-invitations",
            content_type="application/json",
            query_params=query_params,
            path_params={"account_id": self._id.to_api()},
            unpack=False,
        )

    def _paginate_users(self, after=None, filter=None, order="ASC", limit=50, include=None):
        """Get the details of all users.
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param filter: Optional API filter for listing resources.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param limit: The number of results to return (2-1000). Default 50.
        :type limit: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        # Filter query parameters
        query_params = filter.to_api() if filter else {}
        # Add in other query parameters
        query_params["after"] = fields.StringField(after).to_api()
        query_params["order"] = fields.StringField(order, enum=enums.AccountOrderEnum).to_api()
        query_params["limit"] = fields.IntegerField(limit).to_api()
        query_params["include"] = fields.StringField(include).to_api()

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}/users",
            content_type="application/json",
            query_params=query_params,
            path_params={"account_id": self._id.to_api()},
            unpack=False,
        )

    def read(self, include=None, properties=None):
        """Get account info.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}>`_.
        
        :param include: Comma-separated additional data to return. Currently supported:
            limits, policies, sub_accounts.
        :type include: str
        
        :param properties: Property name to return from account-specific properties.
        :type properties: str
        
        :rtype: Account
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account_id}",
            content_type="application/json",
            path_params={"account_id": self._id.to_api()},
            query_params={
                "include": fields.StringField(include).to_api(),
                "properties": fields.StringField(properties).to_api(),
            },
            unpack=self,
        )

    def trusted_certificates(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get all trusted certificates.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/trusted-certificates>`_.

        **API Filters**

        The following filters are supported by the API when listing Account entities:

        +-----------------------+------+------+------+------+------+------+------+
        | Field                 | eq   | neq  | gte  | lte  | in   | nin  | like |
        +=======================+======+======+======+======+======+======+======+
        | device_execution_mode | Y    | Y    |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | enrollment_mode       | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | expire                | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | issuer                |      |      |      |      |      |      | Y    |
        +-----------------------+------+------+------+------+------+------+------+
        | name                  | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | owner                 | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | service               | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | status                | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+
        | subject               |      |      |      |      |      |      | Y    |
        +-----------------------+------+------+------+------+------+------+------+
        | valid                 | Y    |      |      |      |      |      |      |
        +-----------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Account
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("device_execution_mode", "eq", <filter value>)
            for trusted_certificate in Account().trusted_certificates(filter=api_filter):
                print(trusted_certificate.device_execution_mode)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantTrustedCertificate)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantTrustedCertificate
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantTrustedCertificate._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantTrustedCertificate._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantTrustedCertificate,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_trusted_certificates,
        )

    def update(self):
        """Update attributes of an existing account.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}>`_.
        
        :rtype: Account
        """

        # Conditionally setup the message body, fields which have not been set will not be sent to the API.
        # This avoids null fields being rejected and allows the default value to be used.
        body_params = {}
        if self._address_line1.value_set:
            body_params["address_line1"] = self._address_line1.to_api()
        if self._address_line2.value_set:
            body_params["address_line2"] = self._address_line2.to_api()
        if self._aliases.value_set:
            body_params["aliases"] = self._aliases.to_api()
        if self._city.value_set:
            body_params["city"] = self._city.to_api()
        if self._company.value_set:
            body_params["company"] = self._company.to_api()
        if self._contact.value_set:
            body_params["contact"] = self._contact.to_api()
        if self._contract_number.value_set:
            body_params["contract_number"] = self._contract_number.to_api()
        if self._country.value_set:
            body_params["country"] = self._country.to_api()
        if self._custom_fields.value_set:
            body_params["custom_fields"] = self._custom_fields.to_api()
        if self._customer_number.value_set:
            body_params["customer_number"] = self._customer_number.to_api()
        if self._display_name.value_set:
            body_params["display_name"] = self._display_name.to_api()
        if self._email.value_set:
            body_params["email"] = self._email.to_api()
        if self._end_market.value_set:
            body_params["end_market"] = self._end_market.to_api()
        if self._expiration_warning_threshold.value_set:
            body_params["expiration_warning_threshold"] = self._expiration_warning_threshold.to_api()
        if self._idle_timeout.value_set:
            body_params["idle_timeout"] = self._idle_timeout.to_api()
        if self._mfa_status.value_set:
            body_params["mfa_status"] = self._mfa_status.to_api()
        if self._notification_emails.value_set:
            body_params["notification_emails"] = self._notification_emails.to_api()
        if self._password_policy.value_set:
            body_params["password_policy"] = self._password_policy.to_api()
        if self._password_recovery_expiration.value_set:
            body_params["password_recovery_expiration"] = self._password_recovery_expiration.to_api()
        if self._phone_number.value_set:
            body_params["phone_number"] = self._phone_number.to_api()
        if self._postal_code.value_set:
            body_params["postal_code"] = self._postal_code.to_api()
        if self._sales_contact.value_set:
            body_params["sales_contact"] = self._sales_contact.to_api()
        if self._state.value_set:
            body_params["state"] = self._state.to_api()

        return self._client.call_api(
            method="put",
            path="/v3/accounts/{account_id}",
            content_type="application/json",
            body_params=body_params,
            path_params={"account_id": self._id.to_api()},
            unpack=self,
        )

    def user_invitations(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get the details of all user invitations.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/user-invitations>`_.

        **API Filters**

        The following filters are supported by the API when listing Account entities:

        +----------------+------+------+------+------+------+------+------+
        | Field          | eq   | neq  | gte  | lte  | in   | nin  | like |
        +================+======+======+======+======+======+======+======+
        | login_profiles | Y    |      |      |      |      |      |      |
        +----------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Account
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("login_profiles", "eq", <filter value>)
            for user_invitation in Account().user_invitations(filter=api_filter):
                print(user_invitation.login_profiles)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma separated additional data to return.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantUserInvitation)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantUserInvitation
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantUserInvitation._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantUserInvitation._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantUserInvitation,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_user_invitations,
        )

    def users(self, filter=None, order="ASC", max_results=None, page_size=50, include=None):
        """Get the details of all users.

        `REST API Documentation <https://os.mbed.com/search/?q=Service+API+References+/v3/accounts/{account_id}/users>`_.

        **API Filters**

        The following filters are supported by the API when listing Account entities:

        +----------------+------+------+------+------+------+------+------+
        | Field          | eq   | neq  | gte  | lte  | in   | nin  | like |
        +================+======+======+======+======+======+======+======+
        | email          | Y    |      |      |      |      |      |      |
        +----------------+------+------+------+------+------+------+------+
        | login_profiles | Y    |      |      |      |      |      |      |
        +----------------+------+------+------+------+------+------+------+
        | status         | Y    |      |      |      | Y    | Y    |      |
        +----------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python

            from mbed_cloud.foundation import Account
            from mbed_cloud import ApiFilter

            api_filter = ApiFilter()
            api_filter.add_filter("email", "eq", <filter value>)
            for user in Account().users(filter=api_filter):
                print(user.email)
        
        :param filter: An optional filter to apply when listing entities, please see the
            above **API Filters** table for supported filters.
        :type filter: mbed_cloud.client.api_filter.ApiFilter
        
        :param order: Record order based on creation time. Acceptable values: ASC, DESC.
            Default: ASC.
        :type order: str
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
        
        :param page_size: The number of results to return (2-1000). Default 50.
        :type page_size: int
        
        :param include: Comma-separated additional data to return. Currently supported:
            total_count.
        :type include: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(SubtenantUser)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import SubtenantUser
        from mbed_cloud import ApiFilter

        # Be permissive and accept an instance of a dictionary as this was how the Legacy interface worked.
        if isinstance(filter, dict):
            filter = ApiFilter(filter_definition=filter, field_renames=SubtenantUser._renames_to_api)
        # The preferred method is an ApiFilter instance as this should be easier to use.
        elif isinstance(filter, ApiFilter):
            # If filter renames have not be defined then configure the ApiFilter so that any renames
            # performed by the SDK are reversed when the query parameters are created.
            if filter.field_renames is None:
                filter.field_renames = SubtenantUser._renames_to_api
        elif filter is not None:
            raise TypeError("The 'filter' parameter may be either 'dict' or 'ApiFilter'.")

        return paginate(
            self=self,
            foreign_key=SubtenantUser,
            filter=filter,
            order=order,
            max_results=max_results,
            page_size=page_size,
            include=include,
            wraps=self._paginate_users,
        )
