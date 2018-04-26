import behave

import mbed_cloud


@behave.given(u'we have an MbedCloud')
def step_impl(context):
    context.api = mbed_cloud.ConnectAPI()


@behave.when(u'we subscribe to a registration device event')
def step_impl(context):
    context.api.subscribe


@behave.when(u'we request the first value')
def step_impl(context):
    raise NotImplementedError(u'STEP: When request the first value')


@behave.then(u'we get a timeout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we get a timeout')


@behave.when(u'we listen for notifications')
def step_impl(context):
    raise NotImplementedError(u'STEP: When listen for notifications')


@behave.then(u'we receive a notification')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we receive a notification')