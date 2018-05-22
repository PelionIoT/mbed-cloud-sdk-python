Pagination
~~~~~~~~~~

The API provides a paginated response to requests, encapsulated
in the Python client, returning an object that you can
use to iterate over and explore the data.

.. code-block:: python

  from mbed_cloud import ConnectAPI
  api = ConnectAPI()
  paginator = api.list_connected_devices()
  print(paginator.count())
  print(paginator.first())
  print(len(paginator))
  for d in paginator:
    print(d)

Reference
---------

.. automodule:: mbed_cloud.pagination
  :members: PaginatedResponse
