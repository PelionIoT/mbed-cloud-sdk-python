import subprocess
import sys


def main():
    twine_repo = sys.argv[1]
    print('tagging and releasing to %s' % twine_repo)
    version = subprocess.check_output(['python', 'setup.py', '--version']).decode().strip()
    if 'dev' in version:
        raise Exception('cannot release unversioned project: %s' % version)
    subprocess.check_call(['git', 'tag', version])
    subprocess.check_call(['git', 'push', '--tags'])
    subprocess.check_call(['git', 'add', 'NEWS.rst' 'docs/news/*'])
    subprocess.check_call(['git', 'commit', '-m', ':newspaper: Update changelog [skip ci]'])
    # subprocess.check_call(['git', 'push'])
    subprocess.check_call(['twine', 'upload', '--repository-url', twine_repo, 'dist/*'])


if __name__ == '__main__':
    main()
