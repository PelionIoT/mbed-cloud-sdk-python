"""
.. warning::
    OidcRequest should not be imported directly from this module as the
    organisation may change in the future, please use the :mod:`mbed_cloud.foundation` module to import entities.

Foundation Entity: OidcRequest
==============================

The OidcRequest entity does not have any methods, all actions must be performed via
the encapsulating entity.

Entity Usage and Importing
--------------------------

The recommended way of working with Entities is via the SDK Interface which will return an instance of an Entity which
will share the same context as other Entities. There is more information in the :mod:`mbed_cloud.sdk.sdk` module.

.. code-block:: python

    from mbed_cloud import SDK
    pelion_dm_sdk = SDK()
    oidc_requests = pelion_dm_sdk.foundation.oidc_request()

How to import OidcRequest directly:

.. code-block:: python
    
    from mbed_cloud.foundation import OidcRequest

------------
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.foundation.common.entity_base import Entity
from mbed_cloud.foundation.common import fields
from mbed_cloud.foundation import enums


class OidcRequest(Entity):
    """Represents the `OidcRequest` entity in Pelion Device Management"""

    # List of fields that are serialised between the API and SDK
    _api_fieldnames = [
        "authorization_endpoint",
        "auto_enrollment",
        "claim_mapping",
        "client_id",
        "client_secret",
        "end_session_endpoint",
        "issuer",
        "jwks_uri",
        "keys",
        "redirect_uri",
        "revocation_endpoint",
        "scopes",
        "token_endpoint",
        "token_request_mode",
        "token_response_path",
        "userinfo_endpoint",
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
        authorization_endpoint=None,
        auto_enrollment=None,
        claim_mapping=None,
        client_id=None,
        client_secret=None,
        end_session_endpoint=None,
        issuer=None,
        jwks_uri=None,
        keys=None,
        redirect_uri=None,
        revocation_endpoint=None,
        scopes=None,
        token_endpoint=None,
        token_request_mode=None,
        token_response_path=None,
        userinfo_endpoint=None,
    ):
        """Creates a local `OidcRequest` instance

        Parameters can be supplied on creation of the instance or given by
        setting the properties on the instance after creation.

        Parameters marked as `required` must be set for one or more operations
        on the entity. For details on when they are required please see the
        documentation for the setter method.

        :param authorization_endpoint: URL of the OAuth 2.0 authorization endpoint.
        :type authorization_endpoint: str
        :param auto_enrollment: For future use.
        :type auto_enrollment: bool
        :param claim_mapping: Mapping for non-standard OIDC claim names.
        :type claim_mapping: dict
        :param client_id: Client ID needed to authenticate and gain access to identity
            provider's API.
        :type client_id: str
        :param client_secret: Client secret needed to authenticate and gain access to identity
            provider's API.
        :type client_secret: str
        :param end_session_endpoint: URL of the provider's end session endpoint.
        :type end_session_endpoint: str
        :param issuer: Issuer of the identity provider.
        :type issuer: str
        :param jwks_uri: URL of the provider's JSON web key set document.
        :type jwks_uri: str
        :param keys: Provider's public keys and key IDs used to sign ID tokens. PEM-
            encoded.
        :type keys: list
        :param redirect_uri: The URI needed to authenticate and gain access to identity
            provider's API. Leave this empty to use the default redirect URI.
        :type redirect_uri: str
        :param revocation_endpoint: URL of the provider's token revocation endpoint.
        :type revocation_endpoint: str
        :param scopes: Space-separated list of scopes sent in the authentication request.
            When not configured otherwise, the default scopes are ['openid
            profile email'](https://openid.net/specs/openid-connect-
            core-1_0.html#ScopeClaims).
        :type scopes: str
        :param token_endpoint: URL of the OAuth 2.0 authorization endpoint.
        :type token_endpoint: str
        :param token_request_mode: One way to obtain the access token. Since the request results in
            the transmission of clear-text credentials, the client must use
            the POST mode.
        :type token_request_mode: str
        :param token_response_path: Path to the standard data in the token response. Levels in the
            JSON structure must be separated by '.' (dot) characters.
        :type token_response_path: str
        :param userinfo_endpoint: URL of the OAuth 2.0 UserInfo endpoint.
        :type userinfo_endpoint: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.foundation.entities.accounts.oidc_request_claim_mapping import OidcRequestClaimMapping
        from mbed_cloud.foundation.entities.accounts.identity_provider_public_key import IdentityProviderPublicKey

        # fields
        self._authorization_endpoint = fields.StringField(value=authorization_endpoint)
        self._auto_enrollment = fields.BooleanField(value=auto_enrollment)
        self._claim_mapping = fields.DictField(value=claim_mapping, entity=OidcRequestClaimMapping)
        self._client_id = fields.StringField(value=client_id)
        self._client_secret = fields.StringField(value=client_secret)
        self._end_session_endpoint = fields.StringField(value=end_session_endpoint)
        self._issuer = fields.StringField(value=issuer)
        self._jwks_uri = fields.StringField(value=jwks_uri)
        self._keys = fields.ListField(value=keys, entity=IdentityProviderPublicKey)
        self._redirect_uri = fields.StringField(value=redirect_uri)
        self._revocation_endpoint = fields.StringField(value=revocation_endpoint)
        self._scopes = fields.StringField(value=scopes)
        self._token_endpoint = fields.StringField(value=token_endpoint)
        self._token_request_mode = fields.StringField(value=token_request_mode, enum=enums.OidcRequestTokenModeEnum)
        self._token_response_path = fields.StringField(value=token_response_path)
        self._userinfo_endpoint = fields.StringField(value=userinfo_endpoint)

    @property
    def authorization_endpoint(self):
        """URL of the OAuth 2.0 authorization endpoint.
        
        :rtype: str
        """

        return self._authorization_endpoint.value

    @property
    def auto_enrollment(self):
        """For future use.
        
        :rtype: bool
        """

        return self._auto_enrollment.value

    @property
    def claim_mapping(self):
        """Mapping for non-standard OIDC claim names.
        
        :rtype: dict[OidcRequestClaimMapping]
        """

        return self._claim_mapping.value

    @property
    def client_id(self):
        """Client ID needed to authenticate and gain access to identity provider's API.
        
        :rtype: str
        """

        return self._client_id.value

    @property
    def client_secret(self):
        """Client secret needed to authenticate and gain access to identity provider's
        API.
        
        :rtype: str
        """

        return self._client_secret.value

    @property
    def end_session_endpoint(self):
        """URL of the provider's end session endpoint.
        
        :rtype: str
        """

        return self._end_session_endpoint.value

    @property
    def issuer(self):
        """Issuer of the identity provider.
        
        :rtype: str
        """

        return self._issuer.value

    @property
    def jwks_uri(self):
        """URL of the provider's JSON web key set document.
        
        :rtype: str
        """

        return self._jwks_uri.value

    @property
    def keys(self):
        """Provider's public keys and key IDs used to sign ID tokens. PEM-encoded.
        
        :rtype: list[IdentityProviderPublicKey]
        """

        return self._keys.value

    @property
    def redirect_uri(self):
        """The URI needed to authenticate and gain access to identity provider's API.
        Leave this empty to use the default redirect URI.
        
        :rtype: str
        """

        return self._redirect_uri.value

    @property
    def revocation_endpoint(self):
        """URL of the provider's token revocation endpoint.
        
        :rtype: str
        """

        return self._revocation_endpoint.value

    @property
    def scopes(self):
        """Space-separated list of scopes sent in the authentication request. When not
        configured otherwise, the default scopes are ['openid profile
        email'](https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims).
        
        api example: 'openid email'
        
        :rtype: str
        """

        return self._scopes.value

    @property
    def token_endpoint(self):
        """URL of the OAuth 2.0 authorization endpoint.
        
        :rtype: str
        """

        return self._token_endpoint.value

    @property
    def token_request_mode(self):
        """One way to obtain the access token. Since the request results in the
        transmission of clear-text credentials, the client must use the POST mode.
        
        :rtype: str
        """

        return self._token_request_mode.value

    @property
    def token_response_path(self):
        """Path to the standard data in the token response. Levels in the JSON structure
        must be separated by '.' (dot) characters.
        
        api example: 'oidc.data'
        
        :rtype: str
        """

        return self._token_response_path.value

    @property
    def userinfo_endpoint(self):
        """URL of the OAuth 2.0 UserInfo endpoint.
        
        :rtype: str
        """

        return self._userinfo_endpoint.value
