import os

import requests
import dotenv

from mbed_cloud import utils

dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))
DEFAULT_HOST = 'https://api.us-east-1.mbedcloud.com'

def pluck_if_not_none(source, *pluck):
    return {k: source[k] for k in pluck if source[k] is not None}

def strip_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


class DropFields:
    """Represents the remote `DropFields` entity in Mbed Cloud"""
    def __init__(self, ):
        """Creates a local `DropFields` instance

        """
        self._fieldnames = [
        ]
        self._auth_api_key = os.getenv('MBED_CLOUD_SDK_API_KEY')
        self._auth_host = os.getenv('MBED_CLOUD_SDK_HOST')
        self._default_headers = {
            'Authorization': 'Bearer %s' % self._auth_api_key,
            'UserAgent': utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})



class Entities:
    """Represents the remote `Entities` entity in Mbed Cloud"""
    def __init__(self, ):
        """Creates a local `Entities` instance

        """
        self._fieldnames = [
        ]
        self._auth_api_key = os.getenv('MBED_CLOUD_SDK_API_KEY')
        self._auth_host = os.getenv('MBED_CLOUD_SDK_HOST')
        self._default_headers = {
            'Authorization': 'Bearer %s' % self._auth_api_key,
            'UserAgent': utils.get_user_agent(),
        }

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

