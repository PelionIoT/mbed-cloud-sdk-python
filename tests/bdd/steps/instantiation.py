from tests.bdd.steps.common import when_or_given

from mbed_cloud import sdk
from mbed_cloud.sdk import entities


def new_instance(context, entity, name=None):
    context.entities = getattr(context, "entities", {})
    klass = getattr(entities, entity, None) or getattr(sdk, entity)
    instance = klass()
    key = name or instance.__class__.__name__.lower()
    context.entities[key] = instance
    return instance, key


wrapped = new_instance
wrapped = when_or_given("we have a new {entity} called {name}")(wrapped)
wrapped = when_or_given("we have a new {entity}")(wrapped)
