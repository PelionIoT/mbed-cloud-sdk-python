from mbed_cloud.subscribe.subscribe import RoutingBase
from mbed_cloud.subscribe.subscribe import RoutingConflict

from tests.common import BaseCase


class Test(BaseCase):
    def test_route_item(self):
        a = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',))
        self.assertEqual([a], router.list_all())

        # index a single item
        item = router.get_route_item('a')
        self.assertIn(a, item.values())

    def test_route_two_items(self):
        a = 12345
        b = 54321
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',))
        router.get_or_create_routes(b, ('b',))
        self.assertEqual(sorted(router.list_all()), sorted([a, b]))

        # index a single item
        item = router.get_route_item('a')
        self.assertIn(a, item.values())

        # index a single item
        item = router.get_route_item('b')
        self.assertIn(b, item.values())

    def test_cache(self):
        a = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',))
        self.assertEqual(router.list_all(), [a])

        # idempotent / cache
        b = object()
        item = router.get_or_create_routes(b, ('a',))
        self.assertEqual(a, item)

    def test_remove(self):
        a = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',))
        router.remove_routes(('a',))
        item = router.get_route_item('a')
        self.assertIsNone(item)

    def test_cache_clear(self):
        a = object()
        b = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',))
        router.remove_routes(('a',))
        # get_or_create_routes against the same key should return the new object, not a stale one
        item = router.get_or_create_routes(b, ('a',))
        self.assertEqual(b, item)

    def test_routing_extras(self):
        a = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',), sub_routes=('b', 'c'))
        self.assertEqual(router.list_all(), [a])

        item = router.get_route_item('a')
        self.assertEqual({'b': a, 'c': a}, item)

        # additional top level route for 'a' with no sub_routes
        b = object()
        item = router.get_or_create_routes(b, ('a',))
        self.assertEqual(b, item)

        # re-setting existing sub route for 'a' ... returns 'a'
        c = object()
        item = router.get_or_create_routes(c, ('a',), ('b',))
        self.assertEqual(a, item)

        # additional route for 'a' with no sub_routes ... should return 'b' from top-level cache
        d = object()
        item = router.get_or_create_routes(d, ('a',))
        self.assertEqual(b, item)

        # our router now has only two unique items
        self.assertEqual(2, len(router.list_all()))
        self.assertEqual({a, b}, set(router.list_all()))

        # now if we look up an entry we see the items we need to iterate
        # to resolve the sub_routes (the router does not resolve them for us)
        item = router.get_route_item('a')
        self.assertEqual({a, b}, set(list(item.values())))

    def test_routing_conflict(self):
        a = object()
        b = object()
        router = RoutingBase()
        router.get_or_create_routes(a, ('a',), sub_routes=('b', 'c'))

        # You can't route across partial existing routes
        # I think this is important, but finding it hard to justify why.
        # If you could, you'd be partially overwriting sub routes
        # If you can't, I suspect some legitimate use cases might fail e.g.
        #    - subscribe(channel=notifications, device_id=1, resource_path=4)            # ok
        #    - subscribe(channel=notifications, device_id=1, resource_path=4, time_gt=5) # ok
        #    - subscribe(channel=notifications, device_id=1, resource_path=4, time_gt=3) # fail
        # Maybe this is indicative that the right hand side needs to be a list (again?!?)
        with self.assertRaises(RoutingConflict):
            router.get_or_create_routes(b, ('a',), sub_routes=('c', 'd'))
