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
        has_more = (after + 1 if after is not None else 0) + per_page < total
        if after is not None:
            after += 1  # because 'after' refers to IDs (right-aligned) rather than indices (left-aligned)
            data = data[after:after + per_page]
        else:
            data = data[:per_page]
        if include:
            total_count = total

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
    def test_wrapped(self):
        def wrapper(x):
            x.wrapped = True
            return x

        p = PaginatedResponse(get_response, wrapper)
        first = next(p)
        self.assertEqual(first, D(0))
        self.assertTrue(first.wrapped)

    def test_one_response(self):
        p = PaginatedResponse(get_response, total=2)
        self.assert_list_compat(p, [D(0), D(1)])

    def test_has_more(self):
        getter = partial(get_response)
        p = PaginatedResponse(getter)
        self.assertEqual([next(p) for _ in range(4)], [D(0), D(1), D(2), D(3)])

    def test_partial_state(self):
        # cheats a bit, writes internal state
        p = PaginatedResponse(get_response, total=15)
        p._current_data_page = [D(i) for i in range(5, 9)]  # 5, 6, 7, 8
        p._next_id = 8
        self.assertEqual(None, p._total_count)
        self.assertEqual(4, len(p))
        self.assertEqual(15, p.count())
        self.assert_list_compat([D(i) for i in range(5, 15)], p)

    def test_single_page_state(self):
        # cheats a bit, reads internal state
        p = PaginatedResponse(get_response, total=12, per_page=4)
        d = next(p)
        self.assertEqual(d, D(0))  # 0
        self.assert_list_compat(p._current_data_page, [D(i) for i in range(1, 4)])  # 1, 2, 3

    def test_exhausted(self):
        p = PaginatedResponse(get_response)
        list(p)  # exhaust the generator
        with self.assertRaises(IndexError):
            list(p)

        with self.assertRaises(IndexError):
            next(p)

    def test_repr(self):
        p = PaginatedResponse(get_response)
        r = repr(p)
        self.assertEqual('<PaginatedResponse D<0>,D<1>,D<2>...>', r)

    def test_all(self):
        p = PaginatedResponse(get_response)
        self.assert_list_compat(p.all(), [D(0), D(1), D(2), D(3), D(4)])

    def test_first(self):
        p = PaginatedResponse(get_response)
        self.assertEqual(p.first(), D(0))

    def test_first_all_iter(self):
        p = PaginatedResponse(get_response)
        iter_first = next(p)
        iter_rest = list(p)
        explicit_first = p.first()
        explicit_all = p.all()
        self.assertEqual(iter_first, D(0))
        self.assertEqual(explicit_first, D(0))
        self.assert_list_compat(iter_rest, [D(1), D(2), D(3), D(4)])
        self.assert_list_compat(explicit_all, [D(0), D(1), D(2), D(3), D(4)])
