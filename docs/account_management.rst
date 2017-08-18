Account Management
~~~~~~

Listing users and groups in team/organisation
---------------------------------------------

.. code-block:: python

  >>> from mbed_cloud.account_management import AccountManagementAPI
  >>> accountApi = AccountManagementAPI()
  >>>
  >>> u = list(accountApi.list_users())[0]
  >>> print("%r (%s)" % (u.full_name, u.email))
  'David Bowie' (david.bowie@example.org)
  >>>
  >>> print(len(accountApi.list_groups().data))
  13

Creating and managing a new user
--------------------------------

.. code-block:: python

  >>> from mbed_cloud.account_management import AccountManagementAPI
  >>> accountApi = AccountManagementAPI()
  >>>
  >>> # Create a new user with the bare minimum required information
  >>> new_u = accountApi.add_user(username='fooo', email='foo@example.org')
  >>> groups = list(accountApi.list_groups())

Reference
---------

.. autoclass:: mbed_cloud.account_management.AccountManagementAPI
  :members:

.. autoclass:: mbed_cloud.account_management.Account
  :members:
  :inherited-members:
  :exclude-members: to_str, to_dict, object, etag

.. autoclass:: mbed_cloud.account_management.User
  :members:
  :inherited-members:
  :exclude-members: to_str, to_dict, object, etag

.. autoclass:: mbed_cloud.account_management.Group
  :members:
  :inherited-members:
  :exclude-members: to_str, to_dict, object, etag

.. autoclass:: mbed_cloud.account_management.ApiKey
  :members:
  :inherited-members:
  :exclude-members: to_str, to_dict, object, etag
