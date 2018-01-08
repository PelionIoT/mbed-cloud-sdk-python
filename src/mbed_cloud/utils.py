import datetime

from mbed_cloud.exceptions import CloudValueError


def force_utc(time, name='field'):
    if not isinstance(time, datetime.datetime):
        raise CloudValueError("%s should be of type datetime" % (name,))
    return time.isoformat() + "Z"
