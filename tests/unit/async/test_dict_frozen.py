from mbed_cloud.subscribe.subscribe import dict_to_frozen

from tests.common import BaseCase


class Test(BaseCase):
    def test_empty(self):
        self.assertEqual(dict_to_frozen(dict()), [
            frozenset()
        ])

    def test_static(self):
        self.assertEqual(dict_to_frozen(dict(a=1, b=2)), [
            frozenset([('a', 1), ('b', 2)])
        ])

    def test_static_sorted(self):
        self.assertEqual(dict_to_frozen(dict(c=1, b=2)), [
            frozenset([('b', 2), ('c', 1)])
        ])

    def test_expand(self):
        self.assertEqual(dict_to_frozen(dict(a=1, b=[2, 3])), [
            frozenset([('a', 1), ('b', 2)]),
            frozenset([('a', 1), ('b', 3)]),
        ])

    def test_product(self):
        self.assertEqual(dict_to_frozen(dict(a=1, b=[2, 3], c=[4, 5])), [
            frozenset([('a', 1), ('b', 2), ('c', 4)]),
            frozenset([('a', 1), ('b', 2), ('c', 5)]),
            frozenset([('a', 1), ('b', 3), ('c', 4)]),
            frozenset([('a', 1), ('b', 3), ('c', 5)]),
        ])

    def test_usage(self):
        keys = set(dict_to_frozen(dict(a=1, b=[2, 3], c=[4, 5])))

        self.assertIn(dict_to_frozen(dict(a=1, b=2, c=5))[0], keys)
        self.assertNotIn(dict_to_frozen(dict(a=1, b=2, c=6))[0], keys)
