"""Example: listing endpoints and their resources using Device API."""
from mbed_cloud.logging import LoggingAPI


def _print_log(idx, l):
    print("%d) %s | %s\n%s\n" % (idx, l.date_time, l.device_log_id, l.description))


def _main():
    api = LoggingAPI()
    logs = api.list_device_logs(limit=5, order='desc')

    for idx, log in enumerate(logs):
        _print_log(idx + 1, log)

    print("-" * 30 + "\n")

    filters = {
        'device_id': str(logs[0].device_id),
    }
    device_logs = api.list_device_logs(limit=5, filters=filters)
    for idx, device_log in enumerate(device_logs):
        _print_log(idx + 1, device_log)

if __name__ == "__main__":
    _main()
