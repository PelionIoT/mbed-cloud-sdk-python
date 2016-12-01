"""Example: listing endpoints and their resources using Device API."""
from mbed_cloud_sdk.logging import LoggingAPI


def _main():
    api = LoggingAPI()
    logs = api.list_device_logs(limit=5, order='desc')

    for idx, log in enumerate(logs):
        print("%d) %s | %s\n%s\n" % (idx + 1, log.date_time, log.device_log_id, log.description))

if __name__ == "__main__":
    _main()
