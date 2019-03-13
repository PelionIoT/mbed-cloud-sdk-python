"""
Accounts Foundation Entities
============================

This module contains the Foundation Entities that are grouped together under the Accounts category:

- :class:`mbed_cloud.foundation.entities.accounts.account.Account`
- :class:`mbed_cloud.foundation.entities.accounts.active_session.ActiveSession`
- :class:`mbed_cloud.foundation.entities.accounts.api_key.ApiKey`
- :class:`mbed_cloud.foundation.entities.accounts.login_history.LoginHistory`
- :class:`mbed_cloud.foundation.entities.accounts.login_profile.LoginProfile`
- :class:`mbed_cloud.foundation.entities.accounts.parent_account.ParentAccount`
- :class:`mbed_cloud.foundation.entities.accounts.password_policy.PasswordPolicy`
- :class:`mbed_cloud.foundation.entities.accounts.policy.Policy`
- :class:`mbed_cloud.foundation.entities.accounts.subtenant_user.SubtenantUser`
- :class:`mbed_cloud.foundation.entities.accounts.subtenant_user_invitation.SubtenantUserInvitation`
- :class:`mbed_cloud.foundation.entities.accounts.user.User`
- :class:`mbed_cloud.foundation.entities.accounts.user_invitation.UserInvitation`

.. warning::
    Entities should not be imported via this module as the organisation may change in the future, please use the top
    level foundation module to import entities.

How to import Accounts Entities:

.. code-block:: python
    
    from mbed_cloud.foundation import Account
    from mbed_cloud.foundation import ActiveSession
    from mbed_cloud.foundation import ApiKey
    from mbed_cloud.foundation import LoginHistory
    from mbed_cloud.foundation import LoginProfile
    from mbed_cloud.foundation import ParentAccount
    from mbed_cloud.foundation import PasswordPolicy
    from mbed_cloud.foundation import Policy
    from mbed_cloud.foundation import SubtenantUser
    from mbed_cloud.foundation import SubtenantUserInvitation
    from mbed_cloud.foundation import User
    from mbed_cloud.foundation import UserInvitation

"""
