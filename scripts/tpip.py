# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Generate a Third Party Intellectual Property (TPIP) report.

The report is output as a CSV file to the local directory.
"""

import argparse
import csv
import os
import pkg_resources

# Python packages to exclude form the TPIP report
EXCLUDED_PACKAGES = ('python', 'wheel', 'setuptools', 'pip')

# Report field names in CSV
FIELDNAMES = ('PkgName', 'PkgType', 'PkgOriginator', 'PkgVersion',
              'PkgSummary', 'PkgHomePageURL', 'PkgLicense', 'PkgLicenseURL', 'PkgMgrURL')

# Licence strings to exclude from the report as they don't add value
EXCLUDED_LICENSE_STRINGS = ('unknown', 'license', 'licence', 'licensing', 'licencing')


def get_metadata(item):
    """Get metadata information from the distribution.

    Depending on the package this may either be in METADATA or PKG-INFO

    :param item: pkg_resources WorkingSet item
    :returns: metadata resource as list of non-blank non-comment lines
    """
    for metadata_key in ('METADATA', 'PKG-INFO'):
        try:
            metadata_lines = item.get_metadata_lines(metadata_key)
            break
        except (KeyError, IOError):
            # The package will be shown in the report without any license information
            # if a metadata key is not found.
            metadata_lines = []

    return metadata_lines


def process_metadata(pkg_name, metadata_lines):
    """Create a dictionary containing the relevant fields.

    The following is an example of the generated dictionary:

    :Example:

    {
        'name': 'six',
        'version': '1.11.0',
        'repository': 'pypi.python.org/pypi/six',
        'licence': 'MIT',
        'classifier': 'MIT License'
    }

    :param str pkg_name: name of the package
    :param metadata_lines: metadata resource as list of non-blank non-comment lines
    :returns: Dictionary of each of the fields
    :rtype: Dict[str, str]
    """
    # Initialise a dictionary with all the fields to report on.
    tpip_pkg = {}

    tpip_mappings = {
        'version': 'PkgVersion',
        'home-page': 'PkgHomePageURL',
        'author': 'PkgOriginator',
        'author-email': 'PkgAuthorEmail',
        'summary': 'PkgSummary',
        'license': 'PkgLicense',
        'licence': 'PkgLicense',
    }

    tpip_pkg['PkgName'] = pkg_name
    tpip_pkg['PkgType'] = 'python package'
    tpip_pkg['PkgMgrURL'] = 'https://pypi.org/project/%s/' % pkg_name

    # Extract the metadata into a list for each field as there may be multiple
    # entries for each one.
    for line in metadata_lines:
        lower_line = line.lower()

        try:
            metadata_key, metadata_value = lower_line.split(':', 1)
        except ValueError:
            continue

        metadata_key = metadata_key.strip()
        metadata_value = metadata_value.strip()

        if metadata_value == 'unknown':
            continue

        # extract exact matches
        if metadata_key in tpip_mappings:
            tpip_pkg[tpip_mappings[metadata_key]] = metadata_value
            continue

        if metadata_key.startswith('version') and not tpip_pkg.get('PkgVersion'):
            # ... but if not, we'll use whatever we find
            tpip_pkg['PkgVersion'] = metadata_value
            continue

        # Handle british and american spelling of licence/license
        if not tpip_pkg.get('PkgLicense') and 'licen' in lower_line:
            if metadata_key.startswith('classifier') or '::' in metadata_value:
                metadata_value_from_end = lower_line.rsplit(':')[-1].strip()
                tpip_pkg['PkgLicense'] = metadata_value_from_end

    if 'PkgAuthorEmail' in tpip_pkg:
        tpip_pkg['PkgOriginator'] = '%s <%s>' % (
            tpip_pkg['PkgOriginator'],
            tpip_pkg.pop('PkgAuthorEmail')
        )

    return tpip_pkg


def write_csv_file(output_filename, tpip_pkgs):
    """Write the TPIP report out to a CSV file.

    :param str output_filename: filename for CSV.
    :param List tpip_pkgs: a list of dictionaries compatible with DictWriter.
    """
    dirname = os.path.dirname(os.path.abspath(os.path.expanduser(output_filename)))

    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tpip_pkgs)


def force_ascii_values(data):
    """Ensures each value is ascii-only"""
    return {
        k: v.encode('utf8').decode('ascii', 'backslashreplace')
        for k, v in data.items()
    }


def main():
    """Generate a TPIP report."""
    parser = argparse.ArgumentParser(description='Generate a TPIP report as a CSV file.')
    parser.add_argument('output_filename', type=str, metavar='output-file',
                        help='the output path and filename')
    args = parser.parse_args()

    tpip_pkgs = []
    for pkg_name, pkg_item in pkg_resources.working_set.by_key.items():
        if pkg_name not in EXCLUDED_PACKAGES:
            metadata_lines = get_metadata(pkg_item)
            tpip_pkg = process_metadata(pkg_name, metadata_lines)
            tpip_pkgs.append(force_ascii_values(tpip_pkg))

    write_csv_file(args.output_filename, tpip_pkgs)


if __name__ == '__main__':
    # things that came from python packaging
    main()
