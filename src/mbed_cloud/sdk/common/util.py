import functools
import json
import textwrap

from mbed_cloud import pagination


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
    content = textwrap.indent(
        json.dumps(content, indent=2, default=lambda x: str(type(x))), " " * indent
    )
    if replace_null:
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
