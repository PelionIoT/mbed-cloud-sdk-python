from mbed_cloud.subscribe.subscribe import expand_dict_as_keys

from tests.common import BaseCase


class Test(BaseCase):
    def test_empty(self):
        self.assertEqual(expand_dict_as_keys(dict()), [
            tuple()
        ])

    def test_static(self):
        self.assertEqual(expand_dict_as_keys(dict(a=1, b=2)), [
            tuple([('a', 1), ('b', 2)])
        ])

    def test_static_sorted(self):
        self.assertEqual(expand_dict_as_keys(dict(c=1, b=2)), [
            tuple([('b', 2), ('c', 1)])
        ])

    def test_expand(self):
        self.assertEqual(expand_dict_as_keys(dict(a=1, b=[2, 3])), [
            tuple([('a', 1), ('b', 2)]),
            tuple([('a', 1), ('b', 3)]),
        ])

    def test_product(self):
        self.assertEqual(expand_dict_as_keys(dict(a=1, b=[2, 3], c=[4, 5])), [
            tuple([('a', 1), ('b', 2), ('c', 4)]),
            tuple([('a', 1), ('b', 2), ('c', 5)]),
            tuple([('a', 1), ('b', 3), ('c', 4)]),
            tuple([('a', 1), ('b', 3), ('c', 5)]),
        ])

    def test_usage(self):
        keys = set(expand_dict_as_keys(dict(a=1, b=[2, 3], c=[4, 5])))

        self.assertIn(expand_dict_as_keys(dict(a=1, b=2, c=5))[0], keys)
        self.assertNotIn(expand_dict_as_keys(dict(a=1, b=2, c=6))[0], keys)
