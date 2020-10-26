"""
.. warning::
    Entities should not be imported via this module as the organisation may change in the future, please use the
    :mod:`mbed_cloud.foundation` module to import entities.

Accounts Foundation Entities
============================

This module contains the Foundation Entities that are grouped together under the Accounts category:

- :mod:`mbed_cloud.foundation.entities.accounts.account`
- :mod:`mbed_cloud.foundation.entities.accounts.active_session`
- :mod:`mbed_cloud.foundation.entities.accounts.api_key`
- :mod:`mbed_cloud.foundation.entities.accounts.identity_provider`
- :mod:`mbed_cloud.foundation.entities.accounts.identity_provider_public_key`
- :mod:`mbed_cloud.foundation.entities.accounts.login_history`
- :mod:`mbed_cloud.foundation.entities.accounts.login_profile`
- :mod:`mbed_cloud.foundation.entities.accounts.oidc_request`
- :mod:`mbed_cloud.foundation.entities.accounts.oidc_request_claim_mapping`
- :mod:`mbed_cloud.foundation.entities.accounts.parent_account`
- :mod:`mbed_cloud.foundation.entities.accounts.password_policy`
- :mod:`mbed_cloud.foundation.entities.accounts.policy`
- :mod:`mbed_cloud.foundation.entities.accounts.policy_group`
- :mod:`mbed_cloud.foundation.entities.accounts.saml2_request`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_api_key`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_identity_provider`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_policy_group`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user`
- :mod:`mbed_cloud.foundation.entities.accounts.subtenant_user_invitation`
- :mod:`mbed_cloud.foundation.entities.accounts.user`
- :mod:`mbed_cloud.foundation.entities.accounts.user_invitation`

------------

How to import Accounts Entities:

.. code-block:: python
    
    from mbed_cloud.foundation import Account
    from mbed_cloud.foundation import ActiveSession
    from mbed_cloud.foundation import ApiKey
    from mbed_cloud.foundation import IdentityProvider
    from mbed_cloud.foundation import IdentityProviderPublicKey
    from mbed_cloud.foundation import LoginHistory
    from mbed_cloud.foundation import LoginProfile
    from mbed_cloud.foundation import OidcRequest
    from mbed_cloud.foundation import OidcRequestClaimMapping
    from mbed_cloud.foundation import ParentAccount
    from mbed_cloud.foundation import PasswordPolicy
    from mbed_cloud.foundation import Policy
    from mbed_cloud.foundation import PolicyGroup
    from mbed_cloud.foundation import Saml2Request
    from mbed_cloud.foundation import SubtenantApiKey
    from mbed_cloud.foundation import SubtenantIdentityProvider
    from mbed_cloud.foundation import SubtenantPolicyGroup
    from mbed_cloud.foundation import SubtenantUser
    from mbed_cloud.foundation import SubtenantUserInvitation
    from mbed_cloud.foundation import User
    from mbed_cloud.foundation import UserInvitation

------------
"""
