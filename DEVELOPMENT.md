# Mbed Cloud SDK for Python

[![Circle CI](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python.svg?style=shield&circle-token=ec05043ded945f81984e7fd2fce23fe793e7b634)](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/)

[![Builds](https://img.shields.io/badge/sdk-builds-blue.svg)](http://armmbed.github.io/mbed-cloud-sdk-python/builds/)
[![Docs](https://img.shields.io/badge/sdk-documentation-blue.svg)](https://s3-us-west-2.amazonaws.com/mbed-cloud-sdk-python/index.html)

## Prerequisites

Development should be undertaken using virtual environments. See:
- https://github.com/kennethreitz/pipenv

## Installing

```bash
pip install -e git+https://github.com/ARMmbed/mbed-cloud-sdk-python.git
```

Or more directly, clone the repository and in the resulting directory:

```bash
pip install -e .
```

## Tests

```bash
python -m unittest discover tests
```

Tests are written using the unittest framework, so you can
use more feature-rich testrunners if desired. See:
- https://github.com/pytest-dev/pytest
- https://github.com/CleanCut/green

Refer to `tox.ini` for examples.
