import os
import subprocess

from mbed_cloud.tests.common import BaseCase


class TestMetrics(BaseCase):
    def test_metrics(self):
        project_root = os.path.abspath(os.path.dirname(os.path.dirname((os.path.dirname(__file__)))))
        subp = subprocess.Popen('flake8', cwd=project_root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subp.wait()
        if subp.returncode:
            indented = '\n'.join(['\t%s' % s for s in subp.stdout.readlines()])
            print('Saw flake8 failures running in %s:\n%s' % (project_root, indented))
