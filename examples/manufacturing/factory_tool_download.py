"""Example showing basic usage of manufacturing API / factory tool download."""
from mbed_cloud_sdk.manufacturing import ManufacturingAPI

import tempfile


def _main():
    api = ManufacturingAPI()

    print("Operating systems:")
    versions = api.factory_tool_versions().to_dict()
    for v in versions.itervalues():
        print("\t- %s (%s)[%s MB]" % (v["os"], v["filename"], v["size"]))

    resp = api.factory_tool_download("Linux")
    fh = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    fh.write(resp)

    print("Downloaded %r to %s" % (versions["lin_archive_info"]["filename"], fh.name))

if __name__ == "__main__":
    _main()
