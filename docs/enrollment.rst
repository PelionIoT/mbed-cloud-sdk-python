Enrollment
~~~~~~~~~~
For claiming (or transferring) device ownership.

Usage
-----

.. code-block:: python

  from mbed_cloud import EnrollmentAPI
  api = EnrollmentAPI()

  api.add_enrollment_claim(enrollment_identity='your enrollment identity here')


Reference
---------

.. automodule:: mbed_cloud.enrollment
  :members: EnrollmentAPI, EnrollmentClaim
