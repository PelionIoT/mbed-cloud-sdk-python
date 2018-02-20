import subprocess

from tests.common import BaseCase


class Flake8Error(Exception):
    pass


def re_render(out):
    # quick and dirty parse of flake8
    # (there is no public api: http://flake8.pycqa.org/en/latest/user/python-api.html)
    by_path = {}
    sum_failures = 0
    for s in out.splitlines():
        sum_failures += 1
        path, line, column, failure = s.split(':', 3)
        by_path.setdefault(path, {}).setdefault((int(line), int(column)), []).append(failure)

    indented = ['\n\tFiles: %s, failures: %s\n' % (len(by_path), sum_failures)]
    for path, by_location in by_path.items():
        indented.append('\t%s:' % path)
        for line_column, failures in sorted(by_location.items()):
            indented.append('\t\t%s:%s:' % line_column)
            for failure in failures:
                indented.append('\t\t\t%s' % failure)
    return '\n'.join(indented)


class TestSelfMetrics(BaseCase):
    def test_self_metrics(self):
        try:
            subprocess.check_output(
                ['flake8', '.'],
                cwd=self._project_root_dir,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            try:
                indented = re_render(e.output)
            except Exception as e:
                print('Failed to parse flake8 output', e)
            raise Flake8Error('Saw flake8 failures running in %s:\n%s' % (self._project_root_dir, indented))
