import os
import unittest


class BaseCase(unittest.TestCase):
    # path assuming that this file is at `tests\common.py`
    _project_root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    _skip_in_ci = staticmethod(unittest.skipIf(os.environ.get('CI'), 'Do not run in CI'))


class CrudMixinTests(object):
    """Test definition for generic CRUD operations."""

    @classmethod
    def setUpClass(cls):
        print("\n** %s **" % cls.class_under_test.__name__)

    def test_listing(self):
        count = 0
        for entity in self.class_under_test().list(page_size=3, max_results=5):
            self.assertEqual(self.class_under_test, entity.__class__, "Unexpected class returned from the list method")
            count += 1

        self.assertTrue(count <= 5, "At most 5 entities should be returned due to the max_results parameter")
