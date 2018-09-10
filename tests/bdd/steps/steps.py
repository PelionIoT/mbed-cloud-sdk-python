import behave

import functools

import mbed_cloud
from mbed_cloud.sdk import entities
from mbed_cloud import sdk

import ast


#
# def when_or_given(*behave_args):
#     def decorator():
#         def wrapped():
#         behave.given()


def is_not_equal(a, b):
    if a == b:
        raise AssertionError('%s == %s' % (a, b))


def is_equal(a, b):
    if a != b:
        raise AssertionError('%s != %s' % (a, b))


@behave.given(u'we have an {entity}')
@behave.when(u'we have an {entity}')
@behave.given(u'we have a {entity}')
@behave.when(u'we have a {entity}')
@behave.given(u'we have an {entity} called {name}')
@behave.when(u'we have an {entity} called {name}')
@behave.given(u'we have a {entity} called {name}')
@behave.when(u'we have a {entity} called {name}')
def step_impl(context, entity, name=None):
    context.entities = getattr(context, 'entities', {})
    key = name or entity.__class__.__name__
    klass = getattr(entities, entity, None) or getattr(sdk, entity)
    context.entities[key] = klass()


@behave.when(u'we set {name} {attr} to literally {value}')
@behave.given(u'we set {name} {attr} to literally {value}')
def step_impl(context, name, attr, value):
    setattr(context.entities[name], attr, ast.literal_eval(value))


@behave.when(u'we set {name} {attr} to {other_name} {other_attr}')
def step_impl(context, name, attr, other_name, other_attr):
    set_to = getattr(context.entities[other_name], other_attr)
    setattr(context.entities[name], attr, set_to)


@behave.then(u'{name} {attr} is {operator} {other_name} {attr}')
def step_impl(context, name, attr, operator, other_name, other_attr):
    first = getattr(context.entities[name], attr)
    second = getattr(context.entities[other_name], other_attr)
    if operator == 'equivalent to':
        is_equal(first, second)
    elif operator == 'not equivalent to':
        is_not_equal(first, second)


@behave.then(u'{name} object is {operator} {other_name}')
def step_impl(context, name, operator, other_name):
    if operator == 'equivalent to':
        is_equal(context.entities[name], context.entities[other_name])
    elif operator == 'not equivalent to':
        is_not_equal(context.entities[name], context.entities[other_name])


@behave.then(u'{name} {attr} is literally {value}')
def step_impl(context, name, attr, value):
    first = getattr(context.entities[name], attr)
    is_equal(first, ast.literal_eval(value))
