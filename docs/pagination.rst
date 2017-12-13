Pagination
~~~~~~~~~~

The API provides a paginated response to requests,
encapsulated in the Python client, returning an object that you can
use to iterate over and explore the data.

Basic iteration
---------------

.. code-block:: python

  >>> from mbed_cloud.device_directory import DeviceDirectoryAPI
  >>> deviceDirectoryApi = DeviceDirectoryAPI()
  >>> for idx, f in enumerate(deviceDirectoryApi.list_queries(limit=2)):
        print(idx, f)
  1,<F>
  2,<F>
  3,<F>
  4,<F>

Manual control of iteration
---------------------------

.. code-block:: python

  >>> from mbed_cloud.device_directory import DeviceDirectoryAPI
  >>> deviceDirectoryApi = DeviceDirectoryAPI()
  >>> presp = deviceDirectoryApi.list_queries(limit=2)
  >>> elements = []
  >>> while True:
        elements.extend(presp.data)
        if not presp.has_more:
          break
        presp.next()
  >>> print len(elements)
  4

.. code-block:: python

    >>> from mbed_cloud.account_management import AccountManagementAPI
    >>> accountManagementApi = AccountManagementAPI()
    >>> usersResponse = accountManagementApi.list_users()
    >>> users = []
    >>> while usersResponse.has_more:
          elements.append(usersResponse.next())
    >>> print len(elements)
    78

Reference
---------

.. automodule:: mbed_cloud
  :members: PaginatedResponse
