import logging
import json
import datetime

import queue

from dateutil import parser as du_parser
from dateutil import tz as du_tz

from builtins import str


def serialise(obj):
    """Serialises custom datatypes used in the SDK"""
    try:
        return obj.to_dict()
    except AttributeError:
        pass

    if isinstance(obj, datetime.datetime):
        return obj.isoformat()

    if isinstance(obj, queue.Queue):
        return {}

    raise TypeError("Object of type '%s' is not JSON serializable" %
                    obj.__class__.__name__)


def deserialise(obj):
    """Converts objects from custom json-rpc to Python"""
    if isinstance(obj, str) and len(obj) < 30:
        try:
            # some tests try tricking us with timezones - but we assume naive datetime objects in utc
            # 1970-01-21T21:14:37+12:45 -> 1970-01-21 08:29:37 (1970-01-21T08:29:37)
            x = obj
            obj = du_parser.parse(obj).astimezone(tz=du_tz.tzoffset(None, 0)).replace(tzinfo=None)
            logging.info('datetime rehydrated: %s -> %s (%s)' % (x, obj, obj.isoformat()))
        except (TypeError, ValueError) as e:
            logging.debug('not a date: %s (%s)' % (obj, e))
    return obj


def run_module(method, kwargs):
    """Runs the requested method and returns result as json string"""
    for k, v in kwargs.items():
        kwargs[k] = deserialise(v)

    result = method(**kwargs)

    return json.dumps(result, default=serialise)
