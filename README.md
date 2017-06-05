# mbed Cloud SDK for Python

The `mbed-cloud-sdk` gives developers access to the full mbed suite using Python.

## Prerequisites

Python 2.6+ / Python 3.3+

## Installation

    pip install git+https://github.com/ARMmbed/mbed-cloud-sdk-python.git

## Usage

These instructions can also be found in the [official documentation](https://s3-us-west-2.amazonaws.com/mbed-cloud-sdk-python/index.html#quickstart):

1. Create API key in the [mbed Cloud Portal](https://portal.mbedcloud.com/).

2. Create configuration file in `$HOME` or project directory (`.mbed_cloud_config.json`):

    ```javascript
    {
        "api_key": "ak_your_api_key_here"
    }
    ```

3. Import the library and you're ready to go.

    ```python
    >>> from mbed_cloud.connect import ConnectAPI
    >>> connect_api = ConnectAPI()
    >>> connect_api.list_connected_devices()[0]
    {
      "id": "Device #1",
      "state": "unenrolled",
      ...
    }
    >>> from mbed_cloud.account_management import AccountManagementAPI
    >>> api = AccountManagementAPI()
    >>> list(api.list_users())[0]
    {
      "email": "username@example.org",
      "full_name": "Mrs Example",
      ...
    }
    ```

## Resources

  - Full [documentation and API reference here](https://s3-us-west-2.amazonaws.com/mbed-cloud-sdk-python/index.html).

## License

mbed Cloud SDK for Python is free-to-use and licensed under the Apache License
2.0. See LICENSE file for more information.
