from setuptools import setup
from setuptools import find_packages

setup(
    name='auto_version',
    long_description='Tool for managing SemVer versioning of a project.',
    license='Apache 2.0',
    version='2018',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['toml'],
    entry_points=dict(
        console_scripts=['auto_version = auto_version.auto_version_tool:main', ],
    )
)
