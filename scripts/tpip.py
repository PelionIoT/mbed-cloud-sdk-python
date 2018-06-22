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
import json
import os
import pkg_resources

# Python packages to exclude form the TPIP report
EXCLUDED_PACKAGES = {
    'mbed-cloud-sdk',
    'packaging',
    'pip',
    'python',
    'setuptools',
    'wheel',
}

BAD_LICENSES = {
    'dual',
}

# Report field names in CSV
FIELDNAMES = [
    'PkgName',
    'PkgType',
    'PkgOriginator',
    'PkgVersion',
    'PkgSummary',
    'PkgHomePageURL',
    'PkgLicense',
    'PkgLicenseURL',
    'PkgMgrURL',
]

# map from metadata keys to Mbed-standardised TPIP report fields
TPIP_FIELD_MAPPINGS = {
    'version': 'PkgVersion',
    'home-page': 'PkgHomePageURL',
    'author': 'PkgOriginator',
    'author-email': 'PkgAuthorEmail',
    'summary': 'PkgSummary',
    'license': 'PkgLicense',
    'licence': 'PkgLicense',
}


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


def license_cleanup(text):
    if not text:
        return None
    text = text.rsplit(':', 1)[-1]
    replacements = [
        'licenses',
        'license',
        'licences',
        'licence',
        'software',
        ',',
    ]
    for replacement in replacements:
        text = text.replace(replacement, '')
    text = text.strip().upper()
    text = text.replace(' ', '_')
    text = text.replace('-', '_')
    if any(trigger.upper() in text for trigger in BAD_LICENSES):
        return None
    return text


def get_package_info_from_line(tpip_pkg, line):
    """Given a line of text from metadata, extract semantic info"""
    lower_line = line.lower()

    try:
        metadata_key, metadata_value = lower_line.split(':', 1)
    except ValueError:
        return

    metadata_key = metadata_key.strip()
    metadata_value = metadata_value.strip()

    if metadata_value == 'unknown':
        return

    # extract exact matches
    if metadata_key in TPIP_FIELD_MAPPINGS:
        tpip_pkg[TPIP_FIELD_MAPPINGS[metadata_key]] = metadata_value
        return

    if metadata_key.startswith('version') and not tpip_pkg.get('PkgVersion'):
        # ... but if not, we'll use whatever we find
        tpip_pkg['PkgVersion'] = metadata_value
        return

    # Handle british and american spelling of licence/license
    if 'licen' in lower_line:
        if metadata_key.startswith('classifier') or '::' in metadata_value:
            license = lower_line.rsplit(':')[-1].strip().lower()
            license = license_cleanup(license)
            if license:
                tpip_pkg.setdefault('PkgLicenses', []).append(license)


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
    tpip_pkg = dict(
        PkgName=pkg_name,
        PkgType='python package',
        PkgMgrURL='https://pypi.org/project/%s/' % pkg_name,
    )

    # Extract the metadata into a list for each field as there may be multiple
    # entries for each one.
    for line in metadata_lines:
        get_package_info_from_line(tpip_pkg, line)

    # condense PkgAuthorEmail into the Originator field
    if 'PkgAuthorEmail' in tpip_pkg:
        tpip_pkg['PkgOriginator'] = '%s <%s>' % (
            tpip_pkg['PkgOriginator'],
            tpip_pkg.pop('PkgAuthorEmail')
        )

    explicit_license = license_cleanup(tpip_pkg.get('PkgLicense'))
    license_candidates = tpip_pkg.pop('PkgLicenses', [])

    if explicit_license:
        tpip_pkg['PkgLicense'] = explicit_license
    else:
        tpip_pkg['PkgLicense'] = ' '.join(set(license_candidates))

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
    parser.add_argument('--only', type=str, help='only parse this package')
    args = parser.parse_args()

    skips = []
    tpip_pkgs = []
    for pkg_name, pkg_item in sorted(pkg_resources.working_set.by_key.items()):
        if args.only and not args.only in pkg_name.lower():
            continue
        if pkg_name in EXCLUDED_PACKAGES:
            skips.append(pkg_name)
            continue
        metadata_lines = get_metadata(pkg_item)
        tpip_pkg = process_metadata(pkg_name, metadata_lines)
        tpip_pkgs.append(force_ascii_values(tpip_pkg))

    print(json.dumps(tpip_pkgs, indent=2, sort_keys=True))
    print('Parsed %s packages\nOutput to CSV: `%s`\nIgnored packages: %s' % (
        len(tpip_pkgs),
        os.path.abspath(args.output_filename),
        ', '.join(skips),
    ))
    write_csv_file(args.output_filename, tpip_pkgs)


if __name__ == '__main__':
    # things that came from python packaging
    main()
