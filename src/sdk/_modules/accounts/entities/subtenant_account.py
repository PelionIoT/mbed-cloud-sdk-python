"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class SubtenantAccount(Entity):
    """Represents the `SubtenantAccount` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
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
        "expiration_warning_threshold",
        "id",
        "idle_timeout",
        "limits",
        "mfa_status",
        "notification_emails",
        "parent_id",
        "password_policy",
        "phone_number",
        "policies",
        "postal_code",
        "reason",
        "reference_note",
        "sales_contact",
        "state",
        "status",
        "sub_accounts",
        "template_id",
        "tier",
        "updated_at",
        "upgraded_at",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

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
        expiration_warning_threshold=None,
        id=None,
        idle_timeout=None,
        limits=None,
        mfa_status=None,
        notification_emails=None,
        parent_id=None,
        password_policy=None,
        phone_number=None,
        policies=None,
        postal_code=None,
        reason=None,
        reference_note=None,
        sales_contact=None,
        state=None,
        status=None,
        sub_accounts=None,
        template_id=None,
        tier=None,
        updated_at=None,
        upgraded_at=None,
    ):
        """Creates a local `SubtenantAccount` instance

        :param address_line1: Postal address line 1.
        :type address_line1: str
        :param address_line2: Postal address line 2.
        :type address_line2: str
        :param admin_email: The email address of the account admin, not longer than 254
            characters.
        :type admin_email: str
        :param admin_full_name: The full name of the admin user to be created.
        :type admin_full_name: str
        :param admin_id: The ID of the admin user created.
        :type admin_id: str
        :param admin_key: The admin API key created for the account.
        :type admin_key: str
        :param admin_name: The username of the admin user to be created, containing
            alphanumerical letters and -,._@+= characters. It must be at least
            4 but not more than 30 character long.
        :type admin_name: str
        :param admin_password: The password when creating a new user. It will be generated when
            not present in the request.
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
        :param end_market: Account end market.
        :type end_market: str
        :param expiration_warning_threshold: Indicates how many days (1-180) before account expiration a
            notification email should be sent.
        :type expiration_warning_threshold: str
        :param id: Account ID.
        :type id: str
        :param idle_timeout: The reference token expiration time in minutes for this account.
        :type idle_timeout: str
        :param limits: List of limits as key-value pairs if requested.
        :type limits: dict
        :param mfa_status: The enforcement status of the multi-factor authentication, either
            'enforced' or 'optional'.
        :type mfa_status: str
        :param notification_emails: A list of notification email addresses.
        :type notification_emails: list
        :param parent_id: The ID of the parent account, if it has any.
        :type parent_id: str
        :param password_policy: 
        :type password_policy: dict
        :param phone_number: The phone number of a representative of the company.
        :type phone_number: str
        :param policies: List of policies if requested.
        :type policies: list
        :param postal_code: The postal code part of the postal address.
        :type postal_code: str
        :param reason: A reason note for updating the status of the account
        :type reason: str
        :param reference_note: A reference note for updating the status of the account
        :type reference_note: str
        :param sales_contact: Email address of the sales contact.
        :type sales_contact: str
        :param state: The state part of the postal address.
        :type state: str
        :param status: The status of the account.
        :type status: str
        :param sub_accounts: List of sub accounts. Not available for developer users.
        :type sub_accounts: list
        :param template_id: Account template ID.
        :type template_id: str
        :param tier: The tier level of the account; '0': free tier, '1': commercial
            account, '2': partner tier. Other values are reserved for the
            future.
        :type tier: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param upgraded_at: Time when upgraded to commercial account in UTC format RFC3339.
        :type upgraded_at: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

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
        self._expiration_warning_threshold = fields.StringField(
            value=expiration_warning_threshold
        )
        self._id = fields.StringField(value=id)
        self._idle_timeout = fields.StringField(value=idle_timeout)
        self._limits = fields.DictField(value=limits)
        self._mfa_status = fields.StringField(
            value=mfa_status, enum=enums.SubtenantAccountMfaStatusEnum
        )
        self._notification_emails = fields.ListField(value=notification_emails)
        self._parent_id = fields.StringField(value=parent_id)
        self._password_policy = fields.DictField(value=password_policy)
        self._phone_number = fields.StringField(value=phone_number)
        self._policies = fields.ListField(value=policies)
        self._postal_code = fields.StringField(value=postal_code)
        self._reason = fields.StringField(value=reason)
        self._reference_note = fields.StringField(value=reference_note)
        self._sales_contact = fields.StringField(value=sales_contact)
        self._state = fields.StringField(value=state)
        self._status = fields.StringField(
            value=status, enum=enums.SubtenantAccountStatusEnum
        )
        self._sub_accounts = fields.ListField(
            value=sub_accounts, entity=SubtenantAccount
        )
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
        """The email address of the account admin, not longer than 254 characters.
        
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
        """The full name of the admin user to be created.
        
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
        """The ID of the admin user created.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """
        return self._admin_id.value

    @admin_id.setter
    def admin_id(self, value):
        """Set value of `admin_id`

        :param value: value to set
        :type value: str
        """
        self._admin_id.set(value)

    @property
    def admin_key(self):
        """The admin API key created for the account.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac120006000000
            00B40IkJADMANmAscAj0Ot0n2yeQnyt9tT'
        
        :rtype: str
        """
        return self._admin_key.value

    @admin_key.setter
    def admin_key(self, value):
        """Set value of `admin_key`

        :param value: value to set
        :type value: str
        """
        self._admin_key.set(value)

    @property
    def admin_name(self):
        """The username of the admin user to be created, containing alphanumerical
        letters and -,._@+= characters. It must be at least 4 but not more than 30
        character long.
        
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
        """The password when creating a new user. It will be generated when not present
        in the request.
        
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

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """
        self._created_at.set(value)

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
    def expiration_warning_threshold(self):
        """Indicates how many days (1-180) before account expiration a notification email
        should be sent.
        
        api example: '180'
        
        :rtype: str
        """
        return self._expiration_warning_threshold.value

    @expiration_warning_threshold.setter
    def expiration_warning_threshold(self, value):
        """Set value of `expiration_warning_threshold`

        :param value: value to set
        :type value: str
        """
        self._expiration_warning_threshold.set(value)

    @property
    def id(self):
        """Account ID.
        
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
        """The reference token expiration time in minutes for this account.
        
        api example: '30'
        
        :rtype: str
        """
        return self._idle_timeout.value

    @idle_timeout.setter
    def idle_timeout(self, value):
        """Set value of `idle_timeout`

        :param value: value to set
        :type value: str
        """
        self._idle_timeout.set(value)

    @property
    def limits(self):
        """List of limits as key-value pairs if requested.
        
        :rtype: dict
        """
        return self._limits.value

    @limits.setter
    def limits(self, value):
        """Set value of `limits`

        :param value: value to set
        :type value: dict
        """
        self._limits.set(value)

    @property
    def mfa_status(self):
        """The enforcement status of the multi-factor authentication, either 'enforced'
        or 'optional'.
        
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
    def parent_id(self):
        """The ID of the parent account, if it has any.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """
        return self._parent_id.value

    @parent_id.setter
    def parent_id(self, value):
        """Set value of `parent_id`

        :param value: value to set
        :type value: str
        """
        self._parent_id.set(value)

    @property
    def password_policy(self):
        """
        
        :rtype: dict
        """
        return self._password_policy.value

    @password_policy.setter
    def password_policy(self, value):
        """Set value of `password_policy`

        :param value: value to set
        :type value: dict
        """
        self._password_policy.set(value)

    @property
    def phone_number(self):
        """The phone number of a representative of the company.
        
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
        
        :rtype: list
        """
        return self._policies.value

    @policies.setter
    def policies(self, value):
        """Set value of `policies`

        :param value: value to set
        :type value: list
        """
        self._policies.set(value)

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
        """A reason note for updating the status of the account
        
        api example: 'Subscription paid.'
        
        :rtype: str
        """
        return self._reason.value

    @reason.setter
    def reason(self, value):
        """Set value of `reason`

        :param value: value to set
        :type value: str
        """
        self._reason.set(value)

    @property
    def reference_note(self):
        """A reference note for updating the status of the account
        
        api example: 'ARM-INT-0001'
        
        :rtype: str
        """
        return self._reference_note.value

    @reference_note.setter
    def reference_note(self, value):
        """Set value of `reference_note`

        :param value: value to set
        :type value: str
        """
        self._reference_note.set(value)

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

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """
        self._status.set(value)

    @property
    def sub_accounts(self):
        """List of sub accounts. Not available for developer users.
        
        :rtype: list[SubtenantAccount]
        """
        return self._sub_accounts.value

    @sub_accounts.setter
    def sub_accounts(self, value):
        """Set value of `sub_accounts`

        :param value: value to set
        :type value: list[SubtenantAccount]
        """
        self._sub_accounts.set(value)

    @property
    def template_id(self):
        """Account template ID.
        
        api example: '01619571e7160242ac12000600000000'
        
        :rtype: str
        """
        return self._template_id.value

    @template_id.setter
    def template_id(self, value):
        """Set value of `template_id`

        :param value: value to set
        :type value: str
        """
        self._template_id.set(value)

    @property
    def tier(self):
        """The tier level of the account; '0': free tier, '1': commercial account, '2':
        partner tier. Other values are reserved for the future.
        
        api example: '1'
        
        :rtype: str
        """
        return self._tier.value

    @tier.setter
    def tier(self, value):
        """Set value of `tier`

        :param value: value to set
        :type value: str
        """
        self._tier.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """
        self._updated_at.set(value)

    @property
    def upgraded_at(self):
        """Time when upgraded to commercial account in UTC format RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._upgraded_at.value

    @upgraded_at.setter
    def upgraded_at(self, value):
        """Set value of `upgraded_at`

        :param value: value to set
        :type value: datetime
        """
        self._upgraded_at.set(value)
