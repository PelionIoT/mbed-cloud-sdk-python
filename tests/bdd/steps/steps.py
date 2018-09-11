import behave

import functools

import mbed_cloud
from mbed_cloud.sdk import entities
from mbed_cloud import sdk
from mbed_cloud.pagination import PaginatedResponse

import ast
import random
import logging
import traceback
import string


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
    return ''.join([random.choice(string.ascii_uppercase) for _ in range(length)])


def is_not_equal(a, b):
    if a == b:
        raise AssertionError('%s == %s' % (a, b))


def is_equal(a, b):
    if a != b:
        raise AssertionError('%s != %s' % (a, b))


def new_instance(context, entity, name=None):
    context.entities = getattr(context, 'entities', {})
    klass = getattr(entities, entity, None) or getattr(sdk, entity)
    instance = klass()
    key = name or instance.__class__.__name__.lower()
    print('new entity', key)
    context.entities[key] = instance
    return instance, key


wrapped = new_instance
wrapped = when_or_given(u'we have a new {entity} called {name}')(wrapped)
wrapped = when_or_given(u'we have a new {entity}')(wrapped)


def call_method(context, name, method, store_as=None):
    entity = context.entities[name]
    if method == 'create':
        created = getattr(context, 'created_entities', [])
        created.append(entity)
        context.created_entities = created
    response = getattr(entity, method)()

    # store the result for use later
    store_as = store_as or '%s.%s' % (name, method)
    store = getattr(context, 'stored_results', {})
    store[store_as] = response
    context.stored_results = store

    return response


call_method = when_or_given(u'we call {name} {method} --> {store_as}')(call_method)
call_method = when_or_given(u'we call {name} {method}')(call_method)


def set_value(context, name, attr, value):
    setattr(context.entities[name], attr, ast.literal_eval(value))


set_value = when_or_given(u'we set {name} {attr} literally to {value}')(set_value)


@when_or_given(u'we set {name} {attr} to {other_name} {other_attr}')
def step_impl(context, name, attr, other_name, other_attr):
    set_to = getattr(context.entities[other_name], other_attr)
    setattr(context.entities[name], attr, set_to)


@when_or_given(u'we have already created a {entity}')
@when_or_given(u'we have already created a {entity} called {name}')
@when_or_given(u'we have already created an {entity}')
@when_or_given(u'we have already created an {entity} called {name}')
def step_impl(context, entity, name=None):
    instance, key = new_instance(context, entity, name)
    if entity == 'ApiKey':
        set_value(context, key, 'name', '"test-api-key-bdd-%s"' % randstr())
    if entity == 'User':
        set_value(context, key, 'email', '"test+%s@example.com"' % randstr())
    call_method(context, key, 'create')


def ensure_list(item):
    if hasattr(item, '__iter__ ') or hasattr(item, '__len__'):
        item = list(item)
    else:
        item = [item]
    return item


def operator_compare(a, b, operator):
    if hasattr(a, '__call__'):
        a = a()
    if hasattr(b, '__call__'):
        b = b()

    if operator == 'equivalent-to':
        is_equal(a, b)
    elif operator == 'not-equivalent-to':
        is_not_equal(a, b)
    elif operator == 'contains':
        b = ensure_list(b)
        for item in b:
            if item not in a:
                raise AssertionError('%s not in the list' % b)
    elif operator == 'does-not-contain':
        b = ensure_list(b)
        for item in b:
            if item in a:
                raise AssertionError('%s should not be in the list' % b)


@behave.then(u'{name} object is {operator} {other_name}')
def step_impl(context, name, operator, other_name):
    first = context.entities[name]
    second = context.entities[other_name]
    operator_compare(first, second, operator)


@behave.then(u'{name} {attr} is {operator} {other_name} {other_attr}')
def step_impl(context, name, attr, operator, other_name, other_attr):
    first = getattr(context.entities[name], attr)
    second = getattr(context.entities[other_name], other_attr)
    operator_compare(first, second, operator)


@behave.then(u'{name} {attr} is literally {value}')
def step_impl(context, name, attr, value):
    first = getattr(context.entities[name], attr)
    is_equal(first, ast.literal_eval(value))


@behave.then(u'{name} {attr} has a {bool_like} value')
def step_impl(context, name, attr, bool_like):
    first = getattr(context.entities[name], attr)
    is_equal(bool(first), bool_like == 'truthy')


@behave.then(u'{stored} {operator} {name}')
@behave.then(u'{stored} {operator} {name} {attr}')
def step_impl(context, stored, operator, name, attr=None):
    first = context.entities[name]
    second = context.stored_results[stored]
    if attr:
        first = getattr(first, attr)
    operator_compare(second, first, operator)
