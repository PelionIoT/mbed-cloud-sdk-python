import unittest

from tests.common import BaseCase
from mbed_cloud.core import BaseAPI


class TestSortParams(BaseCase):

    @classmethod
    def setUpClass(cls):
        cls.api = BaseAPI()

    def _run(self, expected, **kwargs):
        outcome = self.api._verify_sort_options(kwargs)
        self.assertEqual(outcome, expected)

    def test_simple_invalid_str(self):
        with self.assertRaises(ValueError):
            self._run(None, order='banana')

    @unittest.expectedFailure
    def test_simple_invalid_int(self):
        # FIXME: raises a different kind of error?!
        with self.assertRaises(ValueError):
            self._run(None, order=1337)

    def test_simple_valid_asc(self):
        self._run({'order': 'ASC'}, order='ASC')

    def test_simple_valid_desc(self):
        self._run({'order': 'DESC'}, order='desc')

    def test_limit_low(self):
        with self.assertRaises(ValueError):
            self._run(None, limit=1)

    def test_limit_high(self):
        with self.assertRaises(ValueError):
            self._run(None, limit=1e12)

    def test_limit_just_right(self):
        self._run({'limit': 500}, limit=500)

    def test_limit_and_sort(self):
        self._run({'limit': 3, 'order': 'ASC', 'irrelevant': 'banana'}, limit=3, order='asc', irrelevant='banana')
