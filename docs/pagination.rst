Pagination
~~~~~~~~~~

The API behind the scenes responds to requests in a paginated fashion, which we
encapsulate in the Python client by returning an object where the developer can
fine control the behaviour when iterating and exploring the data.

Basic iteration
---------------

.. code-block:: python

  >>> from mbed_cloud import DeviceDirectoryAPI
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

  >>> from mbed_cloud import DeviceDirectoryAPI
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

    >>> from mbed_cloud import AccountManagementAPI
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
