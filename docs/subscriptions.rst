Subscriptions
~~~~~~~~~~~~~

Usage
-----

The subscription api can be used to interact with asynchronous mbed cloud events.

Currently we support:

- Device State Changes (registration, deregistration etc of devices matching a filter)


.. code-block:: python

  from mbed_cloud import ConnectAPI
  api = ConnectAPI()
  notification = api.subscribe(
    api.subscribe.channels.DeviceStateChange(device_id=1234)
  ).next().block()
  print(notification)

  # equivalent to:
  channel = api.subscribe.channels.DeviceStateChange(device_id=1234)
  api.subscribe(channel)
  observer = channel.observer
  async_wrapper = observer.next()
  notification = async_wrapper.block()

  # equivalent to:
  awaitable = api.subscribe(
    api.subscribe.channels.DeviceStateChange(device_id=1234)
  ).next().defer()
  while True:
    if awaitable.ready():
      notification = awaitable.get()
      break

The subscription system in the Python SDK has the following layers:

| A **Subscription Manager**, which may have several registered channels.
|  The manager routes inbound notifications to channels

| **Channels**, which request and filter notifications from the cloud, and provide a single observer.
|  Channels represent the individual data streams relating to mbed cloud functionality.
|  They are the main abstraction layer between mbed cloud api channels and user code,
|  and may contain filters to further control notification behaviour.

| **Observer**, an iterable of future results, each of which is an async wrapper.
|  Observers are generators; iterables returning potential future results in the order they arrive.

| **Async Wrapper**, a placeholder for an event that is yet to occur.
|  The async wrapper can be used to obtain:
* A Python 2/3 AsyncResult_ object
* A Python 3 asyncio Future_
* Or block until the result can be returned

.. _AsyncResult: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult
.. _Future: https://docs.python.org/3/library/asyncio-task.html#future

Reference
---------

.. automodule:: mbed_cloud.subscribe.channels
  :members: DeviceStateChanges

.. autoclass:: mbed_cloud.subscribe.observer.Observer
  :members:

.. autoclass:: mbed_cloud.subscribe.async_wrapper.AsyncWrapper
  :members:
