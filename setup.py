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
#!/usr/bin/python
from setuptools import find_packages
from setuptools import setup

# Render the README in reST
# http://stackoverflow.com/a/26737672
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","")
except(IOError, ImportError):
    long_description = open('README.md').read()

NAME = "mbed-cloud-sdk"
VERSION = "0.0.1"

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="mbed Cloud SDK",
    author="Herman Schistad",
    author_email="support@mbed.com",
    url="https://github.com/ARMmbed/mbed-cloud-sdk-python",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description
)
