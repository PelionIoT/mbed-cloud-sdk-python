Exceptions
~~~~~~~~~~

Exception hierarchy
----------------

- Exception
    - CloudApiException
        - CloudBackendError
        - CloudValueError
        - CloudUnhandledError
        - CloudAsyncError
        - CloudTimeoutError

Basic exceptions handling.
---------------

.. code-block:: python

  from mbed_cloud.exceptions import CloudApiException
  from mbed_cloud.access import AccessAPI
  api = AccessAPI()
  try:
    u = list(api.list_users())[0]
    print("%r (%s)" % (u.full_name, u.email))
  except CloudApiException e:
    print("Error occurred, status_code: %d , message: %s" % (e.status, e.message))
