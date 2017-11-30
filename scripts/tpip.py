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
FIELDNAMES = ('name', 'version', 'repository', 'licence', 'classifier')

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
    tpip_pkg = dict(zip(FIELDNAMES, [[pkg_name], [], [], [], []]))

    # Extract the metadata into a list for each field as there may be multiple
    # entries for each one.
    for line in metadata_lines:
        try:
            metadata_key, metadata_value = line.rsplit(':', 1)
        except ValueError:
            continue

        metadata_key = metadata_key.strip().lower()
        metadata_value = metadata_value.strip()

        if metadata_key.startswith('version'):
            tpip_pkg['version'].append(metadata_value)
        elif metadata_key.startswith('home-page'):
            tpip_pkg['repository'].append(metadata_value.strip(' /'))
        # Handle british and american spelling of licence/license
        elif metadata_key.startswith('licen'):
            if metadata_value.lower() not in EXCLUDED_LICENSE_STRINGS:
                tpip_pkg['licence'].append(metadata_value)
        elif metadata_key.startswith('classifier') and 'licen' in metadata_key:
            tpip_pkg['classifier'].append(metadata_value)

    # Convert to a flat structure to be written out in the CSV
    return dict((key, '; '.join(value)) for (key, value) in tpip_pkg.items())


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
        for pkg_dict in tpip_pkgs:
            writer.writerow(pkg_dict)


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
            tpip_pkgs.append(tpip_pkg)

    write_csv_file(args.output_filename, tpip_pkgs)


if __name__ == '__main__':
    # things that came from python packaging
    main()
