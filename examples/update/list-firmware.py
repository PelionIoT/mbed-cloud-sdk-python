# ---------------------------------------------------------------------------
# Pelion Device Management SDK
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
"""Example: listing firmware images and manifests using Update API."""
from mbed_cloud import UpdateAPI
import os
import random
import string
import sys

DATE_FMT = "%Y-%m-%d %H:%M:%S"


def _rand_id(N=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


def _main():
    api = UpdateAPI()

    images = api.list_firmware_images(limit=5, order='desc')
    c = images.count()
    if c == 0:
        print("No firmware images currently uploaded")
    else:
        print("** Found %d existing firmware images **\n" % c)
    for idx, image in enumerate(images):
        description = image.description if image.description else "<No description>"
        filename = image.url.rsplit("/", 1)[1]
        print("%d) %s | %s [%s] | %s\n%s\n" % (idx,
                                               image.created_at.strftime(DATE_FMT),
                                               image.name,
                                               image.id,
                                               filename,
                                               description))

    # Upload and delete firmware image
    if len(sys.argv) < 2:
        print("Not doing firmware create/delete as firmware image is not provided on command line")
        return
    filename = os.path.abspath(sys.argv[1])

    nf = api.add_firmware_image(
        name="Auto firmware %s" % _rand_id(),
        datafile=filename,
        description="Uploaded using the Pelion Device Management Python SDK"
    )
    print("Created firmware %r at %s" % (nf.name, nf.created_at.strftime(DATE_FMT)))

    api.delete_firmware_image(nf.id)
    print("Deleted the firmware %r" % nf.name)


if __name__ == '__main__':
    _main()
