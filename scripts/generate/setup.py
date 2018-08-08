from setuptools import setup
from setuptools import find_packages

setup(
    name='generate',
    long_description='Builds the SDK core.',
    license='Apache 2.0',
    version='2018',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['pyyaml', 'chevron'],
)
