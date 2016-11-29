Access
~~~~~~

Listing users and groups in team/organisation
---------------------------------------------

.. code-block:: python

  >>> from mbed_cloud_sdk.access import AccessAPI
  >>> api = AccessAPI()
  >>>
  >>> u = api.list_users()[0]
  >>> print("%r (%s)" % (u.full_name, u.email))
  'David Bowie' (david.bowie@example.org)
  >>>
  >>> print(len(api.list_groups()))
  13

Creating and managing a new user 
--------------------------------

.. code-block:: python

  >>> from mbed_cloud_sdk.access import AccessAPI
  >>> api = AccessAPI()
  >>>
  >>> # Create a new user with the bare minimum required information
  >>> new_u = api.create_user(username='foo', email='foo@example.org')
  >>> groups = api.list_groups()
  >>>
  >>> # Add the new user to first group and set a password
  >>> new_u = api.update_user(new_u.id, password='hunter2', groups=[groups[0].id,])

Reference
---------

.. automodule:: mbed_cloud_sdk.access
  :members:
