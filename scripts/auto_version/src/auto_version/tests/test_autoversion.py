import imp
import contextlib
import os
import unittest
import functools
import re

import six

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
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '19.99.1',
            'VERSION_AGAIN': '19.99.1',
        })

    def test_bump_major(self):
        old, new, updates = self.call(bump='major', release=True)
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '20.0.0',
            'VERSION_AGAIN': '20.0.0',
        })

    def test_bump_news(self):
        old, new, updates = self.call(file_triggers=True, release=True)
        self.assertEqual(updates, {
            'RELEASE': True,
            'VERSION': '19.100.0',
            'VERSION_AGAIN': '19.100.0',
        })

    def test_dev(self):
        old, new, updates = self.call()
        self.assertEqual(updates, {
            'VERSION': '19.99.0.devX',
            'VERSION_AGAIN': '19.99.0.devX',
        })

    def test_end_to_end(self):
        self.call(bump='major')
        filepath = os.path.join(os.path.dirname(__file__), 'example.py')
        example = imp.load_source('example', filepath)
        self.assertEqual(example.VERSION, '20.0.0.devX')


class TestWhitespace(unittest.TestCase):
    def test_whitespace(self):
        prefix, line, suffix = get_whitespace_parts('   some text we like \r\n')
        self.assertEqual('   ', prefix)
        self.assertEqual('some text we like', line)
        self.assertEqual(' \r\n', suffix)

    def test_whitespace_alt(self):
        prefix, line, suffix = get_whitespace_parts('   some text we like \t')
        self.assertEqual('   ', prefix)
        self.assertEqual('some text we like', line)
        self.assertEqual(' \t', suffix)

    def test_whitespace_interstitial(self):
        prefix, line, suffix = get_whitespace_parts('\tx o x\n')
        self.assertEqual('\t', prefix)
        self.assertEqual('x o x', line)
        self.assertEqual('\n', suffix)

    def test_whitespace_short(self):
        prefix, line, suffix = get_whitespace_parts('x')
        self.assertEqual('', prefix)
        self.assertEqual('x', line)
        self.assertEqual('', suffix)

    def test_whitespace_prefix(self):
        prefix, line, suffix = get_whitespace_parts('\tx')
        self.assertEqual('\t', prefix)
        self.assertEqual('x', line)
        self.assertEqual('', suffix)

    def test_whitespace_newline(self):
        prefix, line, suffix = get_whitespace_parts('x\n')
        self.assertEqual('', prefix)
        self.assertEqual('x', line)
        self.assertEqual('\n', suffix)

    def test_whitespace_blank(self):
        prefix, line, suffix = get_whitespace_parts('\n')
        self.assertEqual('', prefix)
        self.assertEqual('\n', line)
        self.assertEqual('', suffix)


@contextlib.contextmanager
def Noop():
    """A no-op context manager"""
    yield


class BaseReplaceCheck(unittest.TestCase):
    key = 'custom_Key'
    value = '1.2.3.4+dev0'
    value_replaced = '5.6.7.8+dev1'
    regexer = None
    lines = []  # simply specify the line if it's trivial to do ''.replace() with
    explicit_replacement = {}  # otherwise, specify the line, and the output
    non_matching = []  # specify example lines that should not match

    def test_match(self):
        for line in self.lines:
            with self.subTest(line=line) if six.PY3 else Noop():
                extracted = extract_keypairs([line], self.regexer)
                self.assertEqual({self.key: self.value}, extracted)

    def test_non_match(self):
        for line in self.non_matching:
            with self.subTest(line=line) if six.PY3 else Noop():
                extracted = extract_keypairs([line], self.regexer)
                self.assertEqual({}, extracted)

    def test_replace(self):
        replacements = {}
        replacements.update(self.explicit_replacement)
        replacements.update({k: k.replace(self.value, self.value_replaced) for k in self.lines})
        for line, replaced in replacements.items():
            with self.subTest(line=line) if six.PY3 else Noop():
                extracted = replace_lines(self.regexer, ReplacementHandler(**{self.key: self.value_replaced}), [line])
                self.assertEqual([replaced], extracted)


class PythonRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.py'], flags=re.DOTALL)
    lines = [
        'custom_Key = "1.2.3.4+dev0"\r\n',
        '    custom_Key = "1.2.3.4+dev0"\r\n',
        '    custom_Key: "1.2.3.4+dev0",\r\n',
    ]
    non_matching = [
        '# custom_Key = "1.2.3.4+dev0"\r\n',
    ]


class JSONRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.json'])
    lines = [
        '"custom_Key": "1.2.3.4+dev0"\r\n',
        '    "custom_Key" : "1.2.3.4+dev0",\r\n',
    ]


class JSONBoolRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.json'])
    value = 'false'
    value_replaced = 'true'
    key = 'is_production'
    lines = [
    ]
    explicit_replacement = {
        '"is_production": false,\r\n': '"is_production": true,\r\n'
    }


class PropertiesRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.properties'])
    lines = [
        'custom_Key=1.2.3.4+dev0\r\n',
        '    custom_Key = 1.2.3.4+dev0\r\n',
    ]
    explicit_replacement = {
        'custom_Key=\r\n': 'custom_Key=5.6.7.8+dev1\r\n'
    }


class CSharpRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.cs'])
    lines = [
        '  public const string custom_Key = "1.2.3.4+dev0";  // auto\r\n',
    ]
    non_matching = [
        '// <copyright file="Version.cs" company="Arm">\r\n',
        '//  public const string custom_Key = "1.2.3.4+dev0";  // auto\r\n',
    ]
    explicit_replacement = {
        # check for no-op on these comment strings that contain variable assignment
        '// <copyright file="Version.cs" company="Arm">': '// <copyright file="Version.cs" company="Arm">',
        '// <copyright file="Version.cs" company="Arm">\r\n': '// <copyright file="Version.cs" company="Arm">\r\n',
    }


class XMLRegexTest(BaseReplaceCheck):
    regexer = re.compile(config.regexers['.csproj'])
    lines = [
        '  <custom_Key>1.2.3.4+dev0</custom_Key>\r\n',
    ]
    non_matching = [
        '<Project Sdk="Microsoft.NET.Sdk">\r\n',
        '''<PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|AnyCPU'">\r\n''',
    ]
