from mbed_cloud.subscribe.subscribe import RoutingBase

from tests.common import BaseCase


class Test(BaseCase):
    def test_add_and_list_one_item(self):
        a = object()
        router = RoutingBase()
        router.create_route(a, ('a',))
        self.assertEqual([a], router.list_all())

    def test_add_and_get_one_item(self):
        a = object()
        router = RoutingBase()
        router.create_route(a, ('a',))
        self.assertIn(a, router.get_route_items('a'))

    def test_missing_item(self):
        router = RoutingBase()
        self.assertEqual([], router.get_route_items('a'))

    def test_same_items(self):
        a = 12345
        b = a
        router = RoutingBase()
        router.create_route(a, ('a',))
        router.create_route(b, ('b',))
        self.assertEqual([a], sorted(router.list_all()))

        # index a single item
        items = router.get_route_items('a')
        self.assertIn(a, items)

        # index a single item
        items = router.get_route_items('b')
        self.assertIn(b, items)

    def test_same_routes(self):
        a = 12345
        b = 54321
        router = RoutingBase()
        router.create_route(a, ('a',))
        router.create_route(b, ('a',))
        self.assertEqual(sorted([a, b]), sorted(router.list_all()))

        # index a single item
        items = router.get_route_items('a')
        self.assertIn(a, items)
        # explicit sort needed for Python2
        self.assertEqual(sorted([a, b]), sorted(items))

    def test_remove_item(self):
        a = object()
        router = RoutingBase()
        router.create_route(a, ('a',))
        router.remove_routes(a, ('a',))
        self.assertEqual([], router.get_route_items('a'))
