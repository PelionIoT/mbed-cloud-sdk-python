"""API reference for update components in mbed Cloud"""
from __future__ import absolute_import
import logging

# Import common functions and exceptions from frontend API
from mbed_cloud_sdk import BaseAPI

# TODO(Herman): Import backend API

LOG = logging.getLogger(__name__)


class UpdateAPI(BaseAPI):
    """Describing the public update API.

    Exposing functionality from the following underlying services:

        - Update service
        - Update campaigns
        - Manifest management
    """

    def __init__(self, params={}):
        """Setup the backend APIs with provided config."""
        super(UpdateAPI, self).__init__(params)
        raise NotImplementedError
