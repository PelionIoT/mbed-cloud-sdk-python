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

- A Subscription Manager, which may have several registered:
- Channels, which request and filter notifications from a server, and provides an:
- Observer, an iterable of future results, each of which is an:
- Async Wrapper, a placeholder for an event that is yet to occur, and can be used to obtain:
- A Python 2/3 AsyncResult_ object, or a Python 3 asyncio Future_ , or to block until the event occurs.

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
