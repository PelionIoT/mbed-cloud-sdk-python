"""Example: listing firmware images and manifests using Update API."""
from mbed_cloud_sdk.update import UpdateAPI


def _main():
    api = UpdateAPI()

    images = api.list_firmware_images(limit=5, order='desc')
    for i in images:
        print(i)

if __name__ == '__main__':
    _main()
