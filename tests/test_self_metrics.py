import os
import subprocess

import pytest

from tests.common import BaseCase


@pytest.mark.meta
class TestSelfMetrics(BaseCase):
    def test_self_metrics(self):
        project_root = os.path.abspath(os.path.dirname(os.path.dirname((os.path.dirname(__file__)))))
        subp = subprocess.Popen('flake8', cwd=project_root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subp.wait()
        if subp.returncode:
            indented = '\n'.join(['\t%s' % s for s in subp.stdout.readlines()])
            raise ValueError('Saw flake8 failures running in %s:\n%s' % (project_root, indented))
