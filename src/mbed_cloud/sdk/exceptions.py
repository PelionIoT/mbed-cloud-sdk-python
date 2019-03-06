class ApiErrorResponse(IOError):
    """Container for errors received when communicating with the cloud service"""

    raw = None
    status_code = None
    all_parameters = None
