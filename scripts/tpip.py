"""Generate a Third Party Intellectual Property (TPIP) report.
The report is output as a CSV file to the local directory.
"""

import csv
import pkg_resources

# Python packages to exclude form the TPIP report
EXCLUDED_PACKAGES = ('python', 'wheel', 'setuptools', 'pip')

# Report field names in CSV
FIELDNAMES = ('name', 'version', 'repository', 'licence', 'classifier')

# Licence strings to exclide from the report as they don't add vaue
EXCLUDED_LICENSE_STRINGS = ('unknown', 'license', 'licence', 'licensing', 'licencing')


def get_metadata(item):
    """Get metadata information from the distribution.

    Depending on the package this may either be in METADATA or PKG-INFO

    :param item: pkg_resources WorkingSet item
    :returns: metadata resource as list of non-blank non-comment lines
    """
    try:
        metadata_lines = item.get_metadata_lines('METADATA')
    except (KeyError, IOError):
        try:
            metadata_lines = item.get_metadata_lines('PKG-INFO')
        except (KeyError, IOError):
            # The package will be shown in the report without any license information
            metadata_lines = []

    return metadata_lines

def process_metadata(pkg_name, metadata_lines):
    """Create a dictionary containing the relevent fields.

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
        lower_line = line.lower()
        if lower_line.startswith('version'):
            tpip_pkg['version'].append(line.rsplit(':', 1)[-1].strip())
        elif lower_line.startswith('home-page'):
            tpip_pkg['repository'].append(line.rsplit(':', 1)[-1].strip(' /'))
        # Handle british and american spelling of licence/license
        elif lower_line.startswith('licen'):
            licence_str = lower_line.rsplit(':', 1)[-1].strip()
            if licence_str.lower() not in EXCLUDED_LICENSE_STRINGS:
                tpip_pkg['licence'].append(licence_str)
        elif lower_line.startswith('classifier') and 'licen' in lower_line:
            tpip_pkg['classifier'].append(line.rsplit(':', 1)[-1].strip())

    # Convert to a flat structure to be written out in the CSV
    return dict((key, '; '.join(value)) for (key, value) in tpip_pkg.items())

def write_csv_file(tpip_pkgs):
    """Write the TPIP report out to a CSV file.

    :param List tpip_pkgs: a list of dictionaries compatible with DictWriter.
    """
    with open('tpip.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for pkg_dict in tpip_pkgs:
            writer.writerow(pkg_dict)

def main():
    """Generat a the TPIP report."""
    tpip_pkgs = []
    for pkg_name, pkg_item in pkg_resources.working_set.by_key.items():
        if pkg_name not in EXCLUDED_PACKAGES:
            metadata_lines = get_metadata(pkg_item)
            tpip_pkg = process_metadata(pkg_name, metadata_lines)
            tpip_pkgs.append(tpip_pkg)

    write_csv_file(tpip_pkgs)


if __name__ == '__main__':
    # things that came from python packaging
    main()
