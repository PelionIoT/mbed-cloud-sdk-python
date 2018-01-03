import os
import subprocess
from distutils.version import LooseVersion


def main():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    metafile = os.path.join(PROJECT_ROOT, 'docs', 'changelog', 'changes', 'last_built.meta')
    last_known = '0'
    if os.path.isfile(metafile):
        with open(metafile) as fh:
            last_known = fh.read()

    import mbed_cloud
    current = mbed_cloud.__version__

    sigfigs = 3  # depends on the versioning scheme (api major, api minor, sdk major, sdk minor, sdk patch)

    should_towncrier = LooseVersion(current).version[:sigfigs] != LooseVersion(last_known).version[:sigfigs]

    print('%s -- %s :: current vs previous changelog build' % (current, last_known))
    if should_towncrier:
        print('%s >> %s :: running changelog build' % (current, last_known))
        subprocess.call(['towncrier', '--yes', '--dir', os.path.join(PROJECT_ROOT, 'docs', 'changelog')])
        with open(metafile, 'w') as fh:
            fh.write(current)


if __name__ == '__main__':
    main()
