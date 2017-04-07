Statistics
~~~~~~

Usage
-----

.. code-block:: python

  from mbed_cloud.statistics import StatisticsAPI
  api = StatisticsAPI()

  # Get Metrics from the last 30 days grouped in 1 day interval
  for metric in api.get_metrics(interval="1d", period="30d"):
      print(metric)

Reference
---------

.. autoclass:: mbed_cloud.statistics.StatisticsAPI
  :members:

.. autoclass:: mbed_cloud.statistics.Metric
  :members:
  :inherited-members:
  :exclude-members: object, etag, to_str, to_dict
