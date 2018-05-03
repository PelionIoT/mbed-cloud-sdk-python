from generate_news import news_dir

import os
import subprocess


def main():
    """Checks for existence of a new newsfile"""
    subprocess.check_call(
        ['git', 'diff', ''],
        cwd=news_dir
    )

if __name__ == '__main__':
    main()
