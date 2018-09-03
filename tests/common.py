import os
import unittest


class BaseCase(unittest.TestCase):
    # path assuming that this file is at `tests\common.py`
    _project_root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    _skip_in_ci = staticmethod(unittest.skipIf(os.environ.get('CI'), 'Do not run in CI'))
