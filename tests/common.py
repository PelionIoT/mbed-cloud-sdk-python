import os

from unittest import TestCase


class BaseCase(TestCase):
    _project_root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
