"""API reference for asset components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI

# TODO(Herman): Import backend API

LOG = logging.getLogger(__name__)


class AssetsAPI(BaseAPI):
    """Describing the public assets API.

    Exposing functionality from the following underlying services:

        - Asset management
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(AssetsAPI, self).__init__(params)
        raise NotImplementedError
