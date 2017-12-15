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
"""Example: Listing and creating update campaigns."""
from mbed_cloud import DeviceDirectoryAPI
from mbed_cloud import UpdateAPI
import os
import random
import string
import sys


def _rand_id(N=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


def _print_manifests(mresp):
    num_manifests = mresp.count()
    if num_manifests == 0:
        print("No manifests found.")
        return

    header = "Manifests (%d)" % (num_manifests)
    print("%s\n%s" % (header, "-" * len(header)))
    for idx, m in enumerate(mresp):
        print("%s | %s | %s" % (m.name, m.url, m.created_at.strftime("%Y-%m-%d %H:%M:%S")))


def _main():
    update_api = UpdateAPI()

    # Read manifest from first argument on command line
    if len(sys.argv) < 2:
        raise ValueError("No manifest filename found on command line")
    filename = os.path.abspath(sys.argv[1])

    # Upload manifest
    mobj = update_api.add_firmware_manifest(
        name="Auto manifest %s" % _rand_id(),
        datafile=filename,
        description="Manifest uploaded using Mbed Cloud SDK")
    print("Successfully uploaded manifest %r\n\tURL: %s\nProperties:" % (mobj.name, mobj.url))

    # List all manifests currently uploaded
    mresp = update_api.list_firmware_manifests(limit=10)
    _print_manifests(mresp)

    # List all filters
    device_api = DeviceDirectoryAPI()
    fresp = device_api.list_queries()
    header = "Current filters:"
    print("\n%s\n%s" % (header, "-" * len(header)))
    if fresp.count() == 0:
        print("No filters created. Please create one to apply the update on.")
        sys.exit(1)
    filters = [f for idx, f in enumerate(fresp)]
    print("\n".join(["\t- %s" % (f.name) for f in filters]))
    selected_query = random.choice(filters)
    print("Randomly chose %r for applying update" % (selected_query.name))

    # Create update campaign. For this step we need three pieces of information:
    # 1. The name of the update campaign (we auto-generate this)
    # 2. What manifest to use for running the update
    # 3. What devices we should apply the updat on (i.e. the filter to use)
    campaign_name = _rand_id()
    print("\nCreating campaign %r using:\n\t- Manifest ID: %r\n\t- Filter ID: %r" % (
        campaign_name,
        mobj.id,
        selected_query.id)
    )
    cobj = update_api.add_campaign(
        name=campaign_name,
        manifest_id=mobj.id,
        device_filter=selected_query.filter
    )
    print("Campaign successfully created. Current state: %r" % (cobj.state))

    #
    # List the current campaigns
    #
    header = "Update campaigns"
    print("\n%s\n%s" % (header, "-" * len(header)))
    for idx, c in enumerate(update_api.list_campaigns()):
        print("\t- %s (State: %r)" % (c.name, c.state))

    #
    # Start the update campaign we've created.
    #
    print("\n** Starting the update campign **")
    # By default a new campaign is created with the 'draft' status. We can manually start it.
    new_cobj = update_api.start_campaign(cobj)
    print("Campaign successfully started. Current state: %r. Checking updates.." % (new_cobj.state))
    countdown = 10
    while countdown > 0:
        c = update_api.get_campaign(new_cobj.id)
        print("[%d/10] Current state: %r (Finished: %s)" % (
            countdown, c.state, c.finished_at
        ))
        countdown -= 1

    #
    # Cleanup.
    #
    print("\n** Deleting update campaign and manifest **")
    update_api.delete_campaign(new_cobj.id)
    update_api.delete_firmware_manifest(mobj.id)


if __name__ == '__main__':
    _main()
