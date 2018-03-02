import os

from unittest import TestCase


class BaseCase(TestCase):
    # path assuming that this file is at `tests\common.py`
    _project_root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
