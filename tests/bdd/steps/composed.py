from tests.bdd.steps.common import when_or_given
from tests.bdd.steps.instantiation import new_instance
from tests.bdd.steps.common import randstr
from tests.bdd.steps.assignment import set_value
from tests.bdd.steps.method_call import call_method


@when_or_given(u"we have already created a {entity}")
@when_or_given(u"we have already created a {entity} called {name}")
@when_or_given(u"we have already created an {entity}")
@when_or_given(u"we have already created an {entity} called {name}")
def step_impl(context, entity, name=None):
    instance, key = new_instance(context, entity, name)
    if entity == "ApiKey":
        set_value(context, key, "name", '"test-api-key-bdd-%s"' % randstr())
    if entity == "User":
        set_value(context, key, "email", '"test+%s@example.com"' % randstr())
    call_method(context, key, "create")
