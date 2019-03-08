"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class UserInvitation(Entity):
    """Represents the `UserInvitation` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "created_at",
        "email",
        "expiration",
        "id",
        "login_profiles",
        "updated_at",
        "user_id",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        created_at=None,
        email=None,
        expiration=None,
        id=None,
        login_profiles=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `UserInvitation` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param account_id: The ID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: (Required) Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param id: (Required) The ID of the invitation.
        :type id: str
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The ID of the invited user.
        :type user_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.login_profile import LoginProfile

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._email = fields.StringField(value=email)
        self._expiration = fields.DateTimeField(value=expiration)
        self._id = fields.StringField(value=id)
        self._login_profiles = fields.ListField(value=login_profiles, entity=LoginProfile)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._user_id = fields.StringField(value=user_id)

    @property
    def account_id(self):
        """The ID of the account the user is invited to.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

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
    def email(self):
        """Email address of the invited user.

        This field must be set when creating a new UserInvitation Entity.
        
        api example: 'friend@arm.com'
        
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
    def expiration(self):
        """Invitation expiration as UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._expiration.value

    @expiration.setter
    def expiration(self, value):
        """Set value of `expiration`

        :param value: value to set
        :type value: datetime
        """

        self._expiration.set(value)

    @property
    def id(self):
        """The ID of the invitation.

        This field must be set when updating or deleting an existing UserInvitation Entity.
        
        api example: '01619571e2e89242ac12000600000000'
        
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
    def login_profiles(self):
        """A list of login profiles for the user. Specified as the identity providers the
        user is associated with.
        
        :rtype: list[LoginProfile]
        """

        return self._login_profiles.value

    @login_profiles.setter
    def login_profiles(self, value):
        """Set value of `login_profiles`

        :param value: value to set
        :type value: list[LoginProfile]
        """

        self._login_profiles.set(value)

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
    def user_id(self):
        """The ID of the invited user.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._user_id.value

    @user_id.setter
    def user_id(self, value):
        """Set value of `user_id`

        :param value: value to set
        :type value: str
        """

        self._user_id.set(value)

    def create(self, valid_for_days=None):
        """Create a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/user-invitations
        
        :param valid_for_days: Specifies how many days the invitation will be valid for. The default
            is 30 days. Value should be between 1 and 100 days.
        :type valid_for_days: int
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="post",
            path="/v3/user-invitations",
            body_params={
                "email": self._email.to_api(),
                "login_profiles": self._login_profiles.to_api(),
                "valid_for_days": fields.IntegerField(valid_for_days).to_api(),
            },
            unpack=self,
        )

    def delete(self):
        """Delete a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/user-invitations/{invitation_id}
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="delete",
            path="/v3/user-invitations/{invitation_id}",
            path_params={"invitation_id": self._id.to_api()},
            unpack=self,
        )

    def list(self, include=None, max_results=None, page_size=None, order=None, filter=None):
        """Get the details of all the user invitations.

        **API Filters**

        The following filters are supported by the API when listing UserInvitation entities:

        +----------------------+------+------+------+------+------+------+------+
        |      Field           |  eq  | neq  | gte  | lte  |  in  | nin  | like |
        +======================+======+======+======+======+======+======+======+
        | login_profile        |  x   |      |      |      |      |      |      |
        +----------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python
            api_filter = ApiFilter()
            api_filter.add_filter("login_profile", "eq", <filter value>)
            for user_invitation in UserInvitation.list(filter=api_filter)
                print user_invitation.login_profile
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
            
        :param page_size: The number of results to return (2-1000), default is 50.
        :type page_size: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :param filter: An optional filter to apply when listing entities, please see the above **API Filters** table for supported filters.
        :type filter: mbed_cloud.ApiFilter

        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse(UserInvitation)
        """

        from mbed_cloud.foundation._custom_methods import paginate
        from mbed_cloud.foundation import UserInvitation

        return paginate(
            self=self,
            foreign_key=UserInvitation,
            include=include,
            max_results=max_results,
            page_size=page_size,
            order=order,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, include=None, limit=50, order="ASC"):
        """Get the details of all the user invitations.

        **API Filters**

        The following filters are supported by the API when listing UserInvitation entities:

        +----------------------+------+------+------+------+------+------+------+
        |      Field           |  eq  | neq  | gte  | lte  |  in  | nin  | like |
        +======================+======+======+======+======+======+======+======+
        | login_profile        |  x   |      |      |      |      |      |      |
        +----------------------+------+------+------+------+------+------+------+

        **Example Usage**

        .. code-block:: python
            api_filter = ApiFilter()
            api_filter.add_filter("login_profile", "eq", <filter value>)
            for user_invitation in UserInvitation.paginate_list(filter=api_filter)
                print user_invitation.login_profile
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param include: Not supported by the API.
        :type include: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/user-invitations",
            query_params={
                "after": fields.StringField(after).to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(
                    order, enum=enums.UserInvitationOrderEnum
                ).to_api(),
            },
            unpack=False,
        )

    def read(self):
        """Details of a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/user-invitations/{invitation_id}
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="get",
            path="/v3/user-invitations/{invitation_id}",
            path_params={"invitation_id": self._id.to_api()},
            unpack=self,
        )
