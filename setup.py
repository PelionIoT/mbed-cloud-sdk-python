#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
mbed Cloud SDK

mbed Cloud SDK allows IoT developers to communicate with different parts
of the mbed Cloud product suite.

Copyright 2016 ARM Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import find_packages
from setuptools import setup

NAME = "mbed-cloud-sdk"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="mbed Cloud SDK",
    author_email="support@mbed.com",
    url="http://developer.mbed.com",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    mbed Cloud SDK allows IoT developers to programmatcially communiticate with\
    different parts of the mbed Cloud suite.
    """
)
