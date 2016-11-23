from mbed_cloud_sdk.devices.catalog import CatalogAPI

def main():
    api = CatalogAPI()
    devices = api.list_devices()
    print devices
    print len(devices)

if __name__ == "__main__":
    main()
