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


class UserInvitation(Entity):
    """Represents the `UserInvitation` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "created_at",
        "email",
        "expiration",
        "groups",
        "id",
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
        groups=None,
        id=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `UserInvitation` instance

        :param account_id: The UUID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param groups: A list of IDs of the groups the user is invited to.
        :type groups: list
        :param id: The UUID of the invitation.
        :type id: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The UUID of the invited user.
        :type user_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._email = fields.StringField(value=email)
        self._expiration = fields.DateTimeField(value=expiration)
        self._groups = fields.ListField(value=groups)
        self._id = fields.StringField(value=id)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._user_id = fields.StringField(value=user_id)

    @property
    def account_id(self):
        """The UUID of the account the user is invited to.
        
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
    def groups(self):
        """A list of IDs of the groups the user is invited to.
        
        :rtype: list
        """

        return self._groups.value

    @groups.setter
    def groups(self, value):
        """Set value of `groups`

        :param value: value to set
        :type value: list
        """

        self._groups.set(value)

    @property
    def id(self):
        """The UUID of the invitation.
        
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
        """The UUID of the invited user.
        
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

    def create(self):
        """Create a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account-id}/user-invitations",
            body_params={"email": self._email.to_api()},
            path_params={"account-id": self._account_id.to_api()},
            unpack=self,
        )

    def delete(self):
        """Delete a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations/{invitation-id}
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account-id}/user-invitations/{invitation-id}",
            path_params={
                "account-id": self._account_id.to_api(),
                "invitation-id": self._id.to_api(),
            },
            unpack=self,
        )

    def get(self):
        """Details of a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations/{invitation-id}
        
        :rtype: UserInvitation
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account-id}/user-invitations/{invitation-id}",
            path_params={
                "account-id": self._account_id.to_api(),
                "invitation-id": self._id.to_api(),
            },
            unpack=self,
        )

    def list(self, include=None, max_results=None, page_size=None, order=None):
        """Get the details of all the user invitations.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations
        
        :param max_results: Total maximum number of results to retrieve
        :type max_results: int
            
        :param page_size: The number of results to return (2-1000), default is 50.
        :type page_size: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :return: An iterator object which yields instances of an entity.
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import UserInvitation

        return paginate(
            self=self,
            foreign_key=UserInvitation,
            include=include,
            max_results=max_results,
            page_size=page_size,
            order=order,
            wraps=self._paginate_list,
        )

    def _paginate_list(self, after=None, limit=50, order="ASC"):
        """Get the details of all the user invitations.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account-id}/user-invitations",
            path_params={"account-id": self._account_id.to_api()},
            query_params={
                "after": fields.StringField(after).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(
                    order, enum=enums.UserInvitationOrderEnum
                ).to_api(),
            },
            unpack=False,
        )
