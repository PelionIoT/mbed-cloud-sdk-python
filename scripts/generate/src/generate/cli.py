"""Load cli options"""
import argparse


def get_cli():
    """Load cli options"""
    parser = argparse.ArgumentParser(prog='generator', description='builds SDK core')
    parser.add_argument(
        '--source',
        action='store',
        dest='input_file',
        help='The location of the input yaml.',
        required=True,
    )
    parser.add_argument(
        '--output',
        action='store',
        dest='output_dir',
        help='The output directory.',
    )
    parser.add_argument(
        '-v', '--verbosity',
        action='count',
        default=0,
        help='increase output verbosity. '
             'can be specified multiple times'
    )
    parser.add_argument(
        '--clean',
        action='store_true',
        help='clean top level directory',
    )
    args, others = parser.parse_known_args()
    return args
