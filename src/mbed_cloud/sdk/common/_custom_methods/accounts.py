from mbed_cloud.sdk.common import util
from mbed_cloud.sdk.common import logs


def subtenant_account_switch_create(self, foreign_key, *args, **kwargs):
    if not self.id or self.id == own_account(self._client).id:
        return self._create_on_aggregator(*args, **kwargs)
    else:
        return self._create_on_subtenant(*args, **kwargs)


def subtenant_account_switch_get(self, foreign_key, *args, **kwargs):
    if not self.id or self.id == own_account(self._client).id:
        return self._get_on_aggregator(*args, **kwargs)
    else:
        return self._get_on_subtenant(*args, **kwargs)


@util.maybe_cache
def own_account(client):
    from mbed_cloud.sdk.entities import MyAccount

    logs.LOGGER.debug("automatically fetching MyAccount")
    return MyAccount(_client=client).get()
