import logging
from mbed_cloud.subscribe.observer import Observer


class _API_CHANNELS:
    """API channels"""
    notifications = 'notifications'
    async_responses = 'async_responses'
    registrations = 'registrations'
    de_registrations = 'de_registrations'
    reg_updates = 'reg_updates'
    registrations_expired = 'registrations_expired'


class ChannelSubscription(object):
    """Represents a subscription to a channel

    (In mbed terms, this may be a Presubscription or a Subscription)
    """
    _api = None  # type: mbed_cloud.connect.ConnectAPI
    _observer = None
    _observer_params = None
    _manager = None
    _routes = None
    _optional_filters = None
    _optional_filter_keys = None
    _route_keys = None
    _active = False

    def get_routing_keys(self):
        """Primary, mandatory routing keys (list of hashables)"""
        return self._route_keys

    def get_extra_keys(self):
        """Secondary, optional routing keys (list of hashables)"""
        return self._optional_filter_keys

    @property
    def active(self):
        return self._active

    @property
    def observer(self):
        return self._observer

    def filter_notification(self, data):
        """A further level of filtering for this channel

        Subclasses can further extend or override this to provide
        custom behaviours e.g. filtering on timestamp ranges or other conditions
        """
        for k, v in (self._optional_filters or {}).items():
            logging.debug('optional filter %s: %s (%s)', k, v, data.get(k))
            if data.get(k) not in v:
                logging.debug('optional filter rejecting %s: %s (%s)', k, v, data.get(k))
                return False
        return True

    def notify(self, data):
        """Notify this channel of inbound data"""
        if self.filter_notification(data):
            self.observer.notify(data)

    def __enter__(self):
        return self.ensure_started()

    def __exit__(self, exc_type, exc_value, traceback):
        return self.ensure_stopped()

    def start(self):
        """Base method for starting the channel"""
        pass

    def stop(self):
        """Base method for stopping the channel"""
        pass

    def configure(self, manager, connect_api_instance, observer_params):
        """Configure behind-the-scenes settings for the channel"""
        self._manager = manager
        self._api = connect_api_instance
        self._observer_params = observer_params

    def ensure_started(self):
        """Idempotent channel start"""
        if self.active:
            return self
        self._observer = Observer(**self._observer_params)
        self.start()
        self._active = True
        return self

    def ensure_stopped(self):
        """Idempotent channel stop"""
        if not self.active:
            return self
        self.stop()
        self.observer.cancel()
        self._manager.remove_routes(self.get_routing_keys())  # hmm - SoC?
        self._active = False
        return self
