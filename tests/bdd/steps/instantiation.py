from tests.bdd.steps.common import when_or_given

from mbed_cloud import sdk
from mbed_cloud.sdk import entities


def new_instance(context, entity_name, name=None):
    # Default dict like behaviour to get top level dictionary
    context.entities = getattr(context, "entities", {})
    # Find class with the specified name in SDK entities or top level of the SDK
    klass = getattr(entities, entity_name, None) or getattr(sdk, entity_name)
    # Instantiate class
    instance = klass()
    # Give default name if not provided
    key = name or instance.__class__.__name__.lower()
    # Store instance against name
    context.entities[key] = instance
    return instance, key


wrapped = new_instance
wrapped = when_or_given("we have a new {entity_name} called {name}")(wrapped)
wrapped = when_or_given("we have a new {entity_name}")(wrapped)
