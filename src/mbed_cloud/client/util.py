import functools
import json

from mbed_cloud import pagination


def maybe_cache(func):
    """If lru_cache is available, try to use it"""
    try:
        from functools import lru_cache
    except ImportError:
        pass
    else:
        func = lru_cache()(func)
    return func


def paginate(unpack):
    """Decorator that wraps listable_call

    In a way that allows it to be paginated
    """

    def decorator(listable_call):
        @functools.wraps(listable_call)
        def wrapper(**kwargs):
            return pagination.PaginatedResponse(
                func=listable_call, lwrap_type=unpack, unpack=False, **kwargs
            )

        return wrapper

    return decorator


def pretty_literal(content, indent=2, replace_null=True):
    """Given content comprised of literals, render them line-by-line

    json lib is used instead of pretty print because subjectively it looks better
    """

    # create a mostly-foolproof serialisation of the object
    content = json.dumps(content, indent=2, default=lambda x: str(type(x)))

    # perform 'textwrap.indent'
    # we would use textwrap but it behaves differently on 2/3
    content = "\n".join(" " * indent + l.rstrip() for l in content.splitlines(True))

    if replace_null:
        # straightforward replacement of json literals with Python ones.
        # might get mucky if it's a phrase in a string, but then it's only meant
        # for helping displaying error messages
        content = content.replace(" null", " None")
        content = content.replace(" false", " False")
        content = content.replace(" true", " True")
    return content


def remap_error_fields(remap, fields):
    """Given either a list of fields, or a list of dictionaries {name: x, message: y}

    In-place remap the fields according to remap {<api>:<sdk>}
    """
    if all(isinstance(f, dict) for f in fields):
        for f in fields:
            name = f["name"]
            f["name"] = remap.get(name, name)
    else:
        fields[:] = [remap.get(f, f) for f in fields]
