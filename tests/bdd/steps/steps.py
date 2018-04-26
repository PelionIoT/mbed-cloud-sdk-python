import behave

import mbed_cloud
import queue


@behave.given(u'we have an MbedCloud')
def step_impl(context):
    # for this sequence we don't really want a notification thread, so fake it:
    context.api = mbed_cloud.ConnectAPI(dict(autostart_notification_thread=False))
    context.api.ensure_notifications_thread = lambda: True


@behave.when(u'we subscribe to a registration device event')
def step_impl(context):
    context.observer = context.api.subscribe(mbed_cloud.channels.DeviceStateChanges())


@behave.when(u'we request the next value')
def step_impl(context):
    context.waitable = context.observer.next()


@behave.then(u'we see a timeout')
def step_impl(context):
    try:
        context.waitable.block(timeout=0.1)
    except (queue.Empty,):
        # TODO: shouldn't the observer re-raise Empty as Timeout?!
        pass


@behave.when(u'a device changes state to {state}')
def step_impl(context, state):
    # send a device state change notification
    state_channel = {
        'registered': mbed_cloud.channels._API_CHANNELS.registrations,
    }[state.lower()]
    context.api.subscribe.notify({state_channel: [{'device_id': '456'}]})


@behave.then(u'we receive a notification')
def step_impl(context):
    context.waitable.block(timeout=1)
