Access
~~~~~~

Listing users and groups in team/organisation
---------------------------------------------

.. code-block:: python

  >>> from mbed_cloud_sdk.access.accounts import AccountsAPI
  >>> api = AccountsAPI()
  >>> first_user = api.list_users()[0]
  >>> print "%s (%s)" % (first_user.full_name, first_user.email)
  David Bowie (david.bowie@example.org)
  >>> print len(api.list_groups())
  13

Reference
---------

.. automodule:: mbed_cloud_sdk.access
  :members:
