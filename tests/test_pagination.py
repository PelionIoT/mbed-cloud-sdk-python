from functools import partial

from mbed_cloud.pagination import PaginatedResponse

from tests.common import BaseCase


class D:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __str__(self):
        return 'D<%s>' % self.id

    def __repr__(self):
        return str(self)


def get_response(total=5, per_page=2, include=None, **kwargs):
    """Statelessly stubs the behaviour of APIs to vaguely match the swagger specs"""

    class X:
        data = [D(i) for i in range(total)]
        after = kwargs.get('after')
        if after is not None:
            after += 1  # because 'after' refers to IDs (right-aligned) rather than indices (left-aligned)
            data = data[after:after + per_page]
        else:
            data = data[:per_page]
        if include:
            total_count = total
        has_more = (after or 0) + per_page < total
    return X


class ListCompatMixin(object):
    def assert_list_compat(self, a, b):
        return (
                getattr(self, 'assertCountEqual', None) or
                getattr(self, 'assertItemsEqual', None)  # Python2 compat
        )(a, b)


class TestStubber(BaseCase, ListCompatMixin):
    def test_stubber_basics(self):
        self.assertEqual(D(0), D(0))
        self.assertNotEqual(D(0), D(1))

    def test_stubber_at_zero(self):
        R = get_response()
        self.assertTrue(R.has_more)
        self.assert_list_compat(R.data, [D(0), D(1)])

    def test_stubber_after(self):
        R = get_response(after=2)
        self.assertEqual(R.data[0], D(3))
        self.assertEqual(R.data[1], D(4))
        self.assertEqual(len(R.data), 2)

    def test_stubber_has_more(self):
        R = get_response(total=3)
        self.assertTrue(R.has_more, '[0, 1] 2 -> more')

        R = get_response(total=4, after=0)
        self.assertTrue(R.has_more, '0, [1, 2], 3 -> more')

        R = get_response(total=3, after=0)
        self.assertFalse(R.has_more, '0, [1, 2] -> no more')

        R = get_response(total=3, after=1)
        self.assertFalse(R.has_more, '0, 1, [2] -> no more')

        R = get_response(total=3, per_page=3)
        self.assertFalse(R.has_more, '[0, 1, 2] -> no more')


class Test(BaseCase, ListCompatMixin):
    """
    Ths test sequence uses a stub implementation of a 'list' API endpoint
    Which uses 'after' as a form of cursor to perform pagination

    The sequence is run a second time with TestNoCache, wherein
    `_is_caching` is set False. Some tests behave differently without caching.
    (namely, without the cache you can't repeatedly list an exhausted iterator).
    """
    paginator = PaginatedResponse

    def test_wrapped(self):
        def wrapper(x):
            x.wrapped = True
            return x

        p = self.paginator(get_response, wrapper)
        first = next(p)
        second = p.next()
        self.assertEqual(first, D(0))
        self.assertTrue(first.wrapped)
        self.assertTrue(second.wrapped)

    def test_empty_response(self):
        p = self.paginator(get_response, total=0)
        self.assert_list_compat(p, [])

    def test_one_response(self):
        p = self.paginator(get_response, total=2)
        self.assert_list_compat(p, [D(0), D(1)])

    def test_has_more(self):
        getter = partial(get_response)
        p = PaginatedResponse(getter)
        self.assertEqual([next(p) for _ in range(4)], [D(0), D(1), D(2), D(3)])

    def test_partial_state(self):
        # cheats a bit, writes internal state
        p = self.paginator(get_response, total=12)
        p._current_data_page = [D(i) for i in range(5, 9)]  # 5, 6, 7, 8
        p._next_id = 8
        self.assertEqual(None, p._total_count)
        self.assertEqual(12, len(p))
        self.assert_list_compat([D(i) for i in range(5, 12)], p)  # 5, 6, 7, 8, 9, 10, 11

    def test_single_page_state(self):
        # cheats a bit, reads internal state
        p = self.paginator(get_response, total=12, per_page=4)
        d = next(p)
        self.assertEqual(d, D(0))  # 0
        self.assert_list_compat(p._current_data_page, [D(i) for i in range(1, 4)])  # 1, 2, 3

    def test_exhausted(self):
        p = self.paginator(get_response)
        self.assertFalse(p._is_exhausted)
        x = list(p)  # exhaust the generator
        self.assertTrue(p._is_exhausted)
        self.assertEqual(p._current_count, 5)
        self.assertEqual(p._get_total_concrete(), 5)
        self.assertEqual(5, len(x))
        if p._is_caching:
            self.assert_list_compat(x, list(p))  # iterating again returns same data

        with self.assertRaises(StopIteration):
            next(p)

    def test_limit(self):
        p = self.paginator(get_response, total=7, limit=5)
        self.assertEqual(5, len(list(p)))

    def test_count(self):
        p = self.paginator(get_response, total=7)
        self.assertEqual(7, p.count())

    def test_bool_false(self):
        # check boolean of object is exactly a boolean False
        p = self.paginator(get_response, total=0)
        self.assertIs(bool(p), False)

    def test_bool_true(self):
        # check boolean of object is exactly a boolean True
        p = self.paginator(get_response)
        self.assertIs(bool(p), True)

    def test_repr(self):
        p = self.paginator(get_response)
        self.assertEqual('<PaginatedResponse D<0>,D<1>,D<2>...>', repr(p))

    def test_all(self):
        p = self.paginator(get_response)
        next(p)
        self.assert_list_compat(p.all(), [D(0), D(1), D(2), D(3), D(4)])

    def test_first(self):
        p = self.paginator(get_response)
        self.assertEqual(p.first(), D(0))

    def test_first_or_none(self):
        p = self.paginator(get_response, total=0)
        self.assertIs(p.first(), None)

    def test_first_all_iter(self):
        p = self.paginator(get_response)
        iter_first = next(p)
        iter_rest = list(p)
        explicit_first = p.first()
        self.assertEqual(iter_first, D(0))
        self.assertEqual(explicit_first, D(0))
        self.assert_list_compat(iter_rest, [D(1), D(2), D(3), D(4)])

        if p._is_caching:
            explicit_all = iter(p)
            self.assert_list_compat(explicit_all, [D(0), D(1), D(2), D(3), D(4)])
        else:
            with self.assertRaises(StopIteration):
                iter(p)

    def test_to_dict(self):
        p = self.paginator(get_response, total=2)
        self.assertEqual(
            {
                'after': None,
                'data': [D(0), D(1)],
                'has_more': False,
                'limit': None,
                'order': 'ASC',
                'total_count': 2
            },
            p.to_dict()
        )

    def test_data_deprecation(self):
        p = self.paginator(get_response, total=2)
        if p._is_caching:
            # this is how a lot of old code was written (.data[0])
            self.assertEqual(list(p)[0], p.data[0])

        # elevate warnings to errors and check we throw one on calling .data
        import warnings
        warnings.simplefilter('error')
        with self.assertRaises(DeprecationWarning):
            self.assertTrue(p.data)
        warnings.resetwarnings()


class TestNoCache(Test):
    paginator = partial(PaginatedResponse, _results_cache=False)

    def test_is_not_caching(self):
        p = self.paginator(get_response)
        self.assertFalse(p._is_caching)
        all(p)
        self.assertIsNone(p._results_cache)

    def test_all(self):
        p = self.paginator(get_response)
        next(p)
        self.assert_list_compat(p.all(), [D(1), D(2), D(3), D(4)])
