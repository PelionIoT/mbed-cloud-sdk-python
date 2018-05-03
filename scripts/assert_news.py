# -*- coding: utf8 -*-

import subprocess
import sys
import os


def main(news_dir=None):
    """Checks for existence of a new newsfile"""
    if news_dir is None:
        from generate_news import news_dir
    news_dir = os.path.abspath(news_dir)
    added_news = subprocess.check_output(
        ['git', 'diff', 'HEAD', '--name-status', news_dir],
        cwd=news_dir
    ).decode()
    if not added_news:
        print('🚫️ Error: Did not find any news files!\nPlease add a news file to `%s`' % (news_dir,))
        exit(1)  # exit with an error status, no need for a traceback
    print('✔️ %s new files in `%s`' % (len(added_news.splitlines()), news_dir))

    # the output of the git command looks like:
    # 'A       docs/news/789.feature'

    # [optional] ensure we have an addition, rather than just modify/delete
    # for line in added_news.splitlines():
    #     if line.startswith('A'):
    #         break
    # else:
    #     raise Exception('No news files additions!\nAdd a news file to `%s`' % (news_dir,))


if __name__ == '__main__':
    news_dir = sys.argv[1] if len(sys.argv) > 1 else None
    main(news_dir)
