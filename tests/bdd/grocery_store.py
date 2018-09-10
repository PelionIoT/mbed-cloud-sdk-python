"""Fetch some Gherkins"""
import logging
import os
import subprocess

import dotenv

from tests.common import BaseCase


def run():
    logging.basicConfig()
    dotenv.load_dotenv()
    gh_token = os.getenv('GITHUB_TOKEN')
    grocery_store = os.getenv('GROCERY_STORE', 'https://{GITHUB_TOKEN}@github.com/ARMmbed/mbed-cloud-sdk-bdd.git')
    logging.info('using token: ***%s', gh_token[-4:])
    grocery_store = grocery_store.format(gh_token)
    checkout_dir = os.path.join(BaseCase._project_root_dir, 'bdd')
    subprocess.check_call(['git', 'clone', grocery_store, checkout_dir])
    subprocess.check_call(['git', 'pull', '--ff', checkout_dir])
    logging.info('repository ')


__name__ == '__main__' and run()
