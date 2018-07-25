import imp
import os
import unittest
import functools
import re

from auto_version.auto_version_tool import main
from auto_version.auto_version_tool import extract_keypairs
from auto_version.auto_version_tool import replace_lines
from auto_version.auto_version_tool import get_whitespace_parts
from auto_version.replacement_handler import ReplacementHandler
from auto_version.config import AutoVersionConfig as config


class Test(unittest.TestCase):
    call = functools.partial(main, config_path='example.toml')

    @classmethod
    def setUpClass(cls):
        dir = os.path.dirname(__file__)
        os.chdir(os.path.abspath(dir))

    def tearDown(self):
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

    def test_end_to_end(self):
        self.call(bump='major')
        filepath = os.path.join(os.path.dirname(__file__), 'example.py')
        example = imp.load_source('example', filepath)
        self.assertEqual(example.VERSION, '20.0.0.devX')


class TestsWithNoSideEffects(unittest.TestCase):
    def test_whitespace(self):
        prefix, line, suffix = get_whitespace_parts('   some text we like \r\n')
        self.assertEqual('   ', prefix)
        self.assertEqual('some text we like', line)
        self.assertEqual(' \r\n', suffix)

    def test_whitespace_short(self):
        prefix, line, suffix = get_whitespace_parts('x\n')
        self.assertEqual('', prefix)
        self.assertEqual('x', line)
        self.assertEqual('\n', suffix)

    def test_whitespace_blank(self):
        prefix, line, suffix = get_whitespace_parts('\n')
        self.assertEqual('', prefix)
        self.assertEqual('\n', line)
        self.assertEqual('', suffix)


class BaseReplaceCheck(unittest.TestCase):
    key = 'custom_Key'
    value = '1.2.3.4+dev0'
    value_replaced = '5.6.7.8+dev1'
    regexer = None
    lines = []  # simply specify the line if it's trivial to do ''.replace() with
    explicit_replacement = {}  # otherwise, specify the line, and the output

    def test_match(self):
        for line in self.lines:
            with self.subTest(line=line):
                extracted = extract_keypairs([line], self.regexer)
                self.assertEqual({self.key: self.value}, extracted)

    def test_replace(self):
        replacements = {}
        replacements.update(self.explicit_replacement)
        replacements.update({k: k.replace(self.value, self.value_replaced) for k in self.lines})
        for line, replaced in replacements.items():
            with self.subTest(line=line):
                extracted = replace_lines(self.regexer, ReplacementHandler(**{self.key: self.value_replaced}), [line])
                self.assertEqual([replaced], extracted)


class PythonRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.py'], flags=re.DOTALL)
    lines = [
        'custom_Key = "1.2.3.4+dev0"\r\n',
        '    custom_Key = "1.2.3.4+dev0"\r\n',
    ]


class PropertiesRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.properties'])
    lines = [
        'custom_Key=1.2.3.4+dev0\r\n',
        '    custom_Key = 1.2.3.4+dev0\r\n',
    ]
    explicit_replacement = {
        'custom_Key=\r\n': 'custom_Key=5.6.7.8+dev1\r\n'
    }
