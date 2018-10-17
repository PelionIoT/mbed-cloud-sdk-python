import functools
import random
import string

import behave


def when_or_given(*behave_args):
    """Behave's verbage is a little weird

    Cucumber implies you can interchange the keywords
    However, behave matches them quite strictly
    You have to explicitly tag a phrase as 'given' *and* as 'when'
    in order to use them interchangeably (as makes sense ... typically a 'given' precondition
    is no more than an action you might perform in 'when')
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        wrapped = behave.given(*behave_args)(wrapped)
        wrapped = behave.when(*behave_args)(wrapped)
        return wrapped

    return decorator


def randstr(length=3):
    return "".join([random.choice(string.ascii_uppercase) for _ in range(length)])


def is_not_equal(a, b):
    if a == b:
        raise AssertionError("%s == %s" % (a, b))


def is_equal(a, b):
    if a != b:
        raise AssertionError("%s != %s" % (a, b))


def ensure_list(item):
    if hasattr(item, "__iter__ ") or hasattr(item, "__len__"):
        item = list(item)
    else:
        item = [item]
    return item


def operator_compare(a, b, operator):
    if hasattr(a, "__call__"):
        a = a()
    if hasattr(b, "__call__"):
        b = b()

    if operator == "equivalent-to":
        is_equal(a, b)
    elif operator == "not-equivalent-to":
        is_not_equal(a, b)
    elif operator == "contains":
        b = ensure_list(b)
        for item in b:
            if item not in a:
                raise AssertionError("%s not in the list" % b)
    elif operator == "does-not-contain":
        b = ensure_list(b)
        for item in b:
            if item in a:
                raise AssertionError("%s should not be in the list" % b)
