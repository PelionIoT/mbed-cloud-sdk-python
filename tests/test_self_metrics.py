import subprocess

import pytest

from tests.common import BaseCase


@pytest.mark.meta
class TestSelfMetrics(BaseCase):
    def test_self_metrics(self):
        subp = subprocess.Popen(['flake8', '.'], cwd=self._project_root_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subp.wait()
        if subp.returncode:
            indented = '\n'.join(['\t%s' % s for s in subp.stdout.readlines() + subp.stderr.readlines()])
            raise ValueError('Saw flake8 failures running in %s:\n%s' % (self._project_root_dir, indented))
