Account Management
~~~~~~

Listing users and groups in team/organisation
---------------------------------------------

.. code-block:: python

  >>> from mbed_cloud.account_management import AccountManagementAPI
  >>> api = AccountManagementAPI()
  >>>
  >>> u = list(api.list_users())[0]
  >>> print("%r (%s)" % (u.full_name, u.email))
  'David Bowie' (david.bowie@example.org)
  >>>
  >>> print(len(api.list_groups()))
  13

Creating and managing a new user
--------------------------------

.. code-block:: python

  >>> from mbed_cloud.account_management import AccountManagementAPI
  >>> api = AccountManagementAPI()
  >>>
  >>> # Create a new user with the bare minimum required information
  >>> new_u = api.create_user(username='foo', email='foo@example.org')
  >>> groups = list(api.list_groups())
  >>>
  >>> # Add the new user to first group and set a password
  >>> new_u = api.update_user(new_u.id, password='hunter2', groups=[groups[0].id,])

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
