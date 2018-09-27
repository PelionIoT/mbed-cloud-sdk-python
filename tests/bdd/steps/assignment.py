import ast

from tests.bdd.steps.common import when_or_given


@when_or_given("we set {name} {attr} to {other_name} {other_attr}")
def step_impl(context, name, attr, other_name, other_attr):
    set_to = getattr(context.entities[other_name], other_attr)
    setattr(context.entities[name], attr, set_to)


def set_value(context, name, attr, value):
    setattr(context.entities[name], attr, ast.literal_eval(value))


set_value = when_or_given("we set {name} {attr} literally to {value}")(set_value)
