from mbed_cloud_sdk.devices.connector import ConnectorAPI

def main():
    api = ConnectorAPI()
    endpoints = api.list_endpoints()

    for endpoint in endpoints:
        resources = api.list_resources(endpoint.name)

        # Print endpoint name header
        header = endpoint.name
        print header
        print len(header) * "-"

        for r in resources:
            print "\t- %s (%s / Observable: %s)" % (r.uri, r.rt if r.rt else "-", r.obs)

        # Space between endpoints
        print

if __name__ == "__main__":
    main()
