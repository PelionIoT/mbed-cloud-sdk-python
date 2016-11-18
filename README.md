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

## Updating auto-generated code from Swagger files

Run `./bootstrap.sh`, which will run the script in
[/ARMmbed/mbed-cloud-sdk-codegen](/ARMmbed/mbed-cloud-sdk-codegen) as populate
the backend Python SDK.

