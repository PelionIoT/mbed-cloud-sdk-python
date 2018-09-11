from tests.bdd.steps.common import when_or_given


def call_method(context, name, method, store_as=None):
    entity = context.entities[name]
    if method == "create":
        created = getattr(context, "created_entities", [])
        created.append(entity)
        context.created_entities = created
    response = getattr(entity, method)()

    # store the result for use later
    store_as = store_as or "%s.%s" % (name, method)
    store = getattr(context, "stored_results", {})
    store[store_as] = response
    context.stored_results = store

    return response


call_method = when_or_given(u"we call {name} {method} --> {store_as}")(call_method)
call_method = when_or_given(u"we call {name} {method}")(call_method)
