# Changelog

## 1.2.4

### Deliverables

The application is primarily hosted on pypi at https://pypi.org/project/mbed-cloud-sdk and can be installed using pip:

```
$ pip install mbed-cloud-sdk
```

### Changes

- Filter construction logic reworked
- Added webhook notification handler
- AsyncConsumer.wait()
- Various bugfixes

### Known Issues

- Testing shows that `get_resource_value` will fail
when the cloud service returns a value directly, rather than
through an open notification channel. This affects all previous versions.
- The only known workaround at present is to ensure the cloud cache is not used by:
  - Waiting between calls to get_resource_value
  - Reducing [the configured TTL](https://cloud.mbed.com/docs/latest/collecting/handle-resources.html#working-with-the-server-cache) on the cloud client image on the device

## 1.2.3

### Deliverables

The application is additionally hosted on pypi at https://pypi.org/project/mbed-cloud-sdk and can be installed using pip:

```
$ pip install mbed-cloud-sdk
```

### Changes

- Initial early access release tracking Mbed Cloud 1.2 APIs
- Added unittests
- Added coverage collection
- Python versions supported:
  - 2.7.10+
  - 3.4.3+
- Examples working with both Python 2.7.10+ and 3.4.3+

## 1.2.0-alpha

### Deliverables

The application is hosted on GitHub at https://github.com/ARMmbed/mbed-cloud-sdk-python and can be installed using pip:

```
$ pip install ARMmbed/mbed-cloud-sdk-python@1.2.0-alpha
```

### Changes

- Initial early access release tracking Mbed Cloud 1.2 APIs
- APIs supported:
  - Account Management
  - Certificates
  - Connect
  - Device Diectory
  - Update
- Python versions supported:
  - 2.6+
  - 3.3+
- Examples working with both Python 2.6+ and 3.3+
- Full documentation outlining usage
