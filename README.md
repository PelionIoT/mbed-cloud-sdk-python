# Python mbed Cloud SDK

Work in progress..

## Examples

See [examples directory](examples/) for a collection of use-cases of this API.

To run the examples, you would need to setup your environment by installing the
dependencies in the `requirements.txt` file. This can be easily done using
virtualenv:

    virtualenv venv/
    source venv/bin/activate
    pip install -r requirements.txt

## Running examples using integration lab

Get an API key using the [cloud portal](https://lab.mbedcloudintegration.net) and
enter it into `api_key` in the `mbed_cloud_config_integration.json` file.

Run the following command to list accounts in the organisation:

```
MBED_CLOUD_SDK_CONFIG=$PWD/mbed_cloud_config_integration.json python examples/access/list-details.py
```

## Updating auto-generated code from Swagger files

Run `./bootstrap.sh`, which will run the script in
[/ARMmbed/mbed-cloud-sdk-codegen](/ARMmbed/mbed-cloud-sdk-codegen) as populate
the backend Python SDK.
