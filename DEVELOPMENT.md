# Mbed Cloud SDK for Python

[![CircleCI](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/master.svg?style=shield&circle-token=ec05043ded945f81984e7fd2fce23fe793e7b634)](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/master) - Master

[![CircleCI](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/production.svg?style=shield&circle-token=ec05043ded945f81984e7fd2fce23fe793e7b634)](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/production) - Release

[![CircleCI](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/swagger-branch.svg?style=shield&circle-token=ec05043ded945f81984e7fd2fce23fe793e7b634)](https://circleci.com/gh/ARMmbed/mbed-cloud-sdk-python/tree/swagger-branch) - OpenAPI

[![Builds](https://img.shields.io/badge/sdk-builds-blue.svg)](http://armmbed.github.io/mbed-cloud-sdk-python/builds/)
[![Docs](https://img.shields.io/badge/sdk-documentation-blue.svg)](https://s3-us-west-2.amazonaws.com/mbed-cloud-sdk-python/index.html)

## Prerequisites

It is recommended that contributors use virtual environments for development:
- https://github.com/pypa/pipenv

## Installing

```bash
pipenv install -e git+https://github.com/ARMmbed/mbed-cloud-sdk-python.git#egg=mbed-cloud-sdk --dev
```

alternatively:

```bash
git clone https://github.com/ARMmbed/mbed-cloud-sdk-python.git
pipenv install "-e ." --dev
```

## Tests

```bash
pipenv run python -m unittest discover tests
```

Tests are written using the unittest framework, so you can
use any compatible Python testrunner. For example:
- https://github.com/pytest-dev/pytest
- https://github.com/CleanCut/green

To run the full cross-language TestRunner suite you will also need to
set up AWS credentials and pull the latest docker image.
This may not be available to public contributors.

Some tests may require valid API credentials.

## Documentation

```bash
pipenv run sphinx-build -a -b html -c docs/ docs/ docs/build/
```
