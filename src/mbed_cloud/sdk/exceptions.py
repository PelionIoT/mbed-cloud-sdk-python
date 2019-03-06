"""Exceptions for Primary, Foundation and Client Interfaces

These exceptions are not used by the Legacy interface
"""


class ApiErrorResponse(IOError):
    """Container for errors received when communicating with the cloud service"""

    raw = None
    status_code = None
    all_parameters = None
