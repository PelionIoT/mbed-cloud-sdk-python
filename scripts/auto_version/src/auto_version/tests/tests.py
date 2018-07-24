import os
import unittest
import functools

from auto_version.auto_version_tool import main


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dir = os.path.dirname(__file__)
        os.chdir(os.path.abspath(dir))

    def setUp(self):
        self.call = functools.partial(main, config_path='example.toml')
        self.call(set_to='19.99.0')

    def test_bump_patch(self):
        old, new, updates = self.call(bump='patch', release=True)
        updates.pop('COMMIT')
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '19.99.1',
            'VERSION_AGAIN': '19.99.1',
        })

    def test_bump_major(self):
        old, new, updates = self.call(bump='major', release=True)
        updates.pop('COMMIT')
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '20.0.0',
            'VERSION_AGAIN': '20.0.0',
        })

    def test_bump_news(self):
        old, new, updates = self.call(file_triggers=True, release=True)
        updates.pop('COMMIT')
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '19.100.0',
            'VERSION_AGAIN': '19.100.0',
        })

    def test_dev(self):
        old, new, updates = self.call()
        updates.pop('COMMIT')
        self.assertEqual(updates, {
            'VERSION': '19.99.0.devX',
            'VERSION_AGAIN': '19.99.0.devX',
        })
