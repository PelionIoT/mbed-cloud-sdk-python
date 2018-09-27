import ast

import behave

from tests.bdd.steps.common import operator_compare
from tests.bdd.steps.common import is_equal


@behave.then("{name} object is {operator} {other_name}")
def assert_entity(context, name, operator, other_name):
    first = context.entities[name]
    second = context.entities[other_name]
    operator_compare(first, second, operator)


@behave.then("{name} {attr} is {operator} {other_name} {other_attr}")
def assert_attrs(context, name, attr, operator, other_name, other_attr):
    first = getattr(context.entities[name], attr)
    second = getattr(context.entities[other_name], other_attr)
    operator_compare(first, second, operator)


@behave.then("{name} {attr} is literally {value}")
def assert_literal(context, name, attr, value):
    first = getattr(context.entities[name], attr)
    is_equal(first, ast.literal_eval(value))


@behave.then("{name} {attr} has a {bool_like} value")
def assert_bool(context, name, attr, bool_like):
    first = getattr(context.entities[name], attr)
    is_equal(bool(first), bool_like == "truthy")


@behave.then("{stored} {operator} {name}")
@behave.then("{stored} {operator} {name} {attr}")
def assert_stored_attr(context, stored, operator, name, attr=None):
    first = context.entities[name]
    second = context.stored_results[stored]
    if attr:
        first = getattr(first, attr)
    operator_compare(second, first, operator)
