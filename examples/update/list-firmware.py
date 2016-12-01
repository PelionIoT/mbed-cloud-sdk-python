"""Example: listing firmware images and manifests using Update API."""
from mbed_cloud_sdk.update import UpdateAPI


def _main():
    api = UpdateAPI()

    images = api.list_firmware_images(limit=5, order='desc')
    date_fmt = "%Y-%m-%d %H:%M:%S"
    for idx, image in enumerate(images):
        description = image.description if image.description else "<No description>"
        filename = image.datafile.rsplit("/", 1)[1]
        print("%d) %s | %s [%s] | %s\n%s\n" % (idx,
                                               image.created_at.strftime(date_fmt),
                                               image.name,
                                               image.image_id,
                                               filename,
                                               description))

if __name__ == '__main__':
    _main()
