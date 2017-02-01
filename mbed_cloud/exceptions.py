# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""All custom exceptions used in mbed_cloud_sdk."""


class CloudApiException(Exception):
    """Common exception thrown when ApiException is raised from backend API.

    CloudApiException typically means that something went wrong in communicating
    with the cloud API. This can be authentication errors, connectivity issues
    or invalid usage of the API.
    """

    pass


class UnhandledError(Exception):
    """Thrown when function returns async consumer, but the error isn't handled.

    Only applicable when threads are setup and the user needs to call `is_done`
    and `error` before getting value.
    """

    pass


class AsyncError(Exception):
    """Thrown when running in synchronized/blocking mode, but an error is raised.

    Typically only found when an async consumer runs with `sync=True` and an error
    is raised from the backend. Should be handled by the user.
    """

    pass
