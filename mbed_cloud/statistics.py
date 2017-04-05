# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Functionality for statistics-related actions in mbed Cloud."""

# Import common functions and exceptions from frontend API
import datetime
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
import re

# Import backend API
import mbed_cloud._backends.statistics as statistics
from mbed_cloud._backends.statistics.models import Metric as MetricData
from mbed_cloud._backends.statistics.rest import ApiException


class StatisticsAPI(BaseAPI):
    """API reference for the Statistics API.

    Exposing functionality for getting statistics data.
    """

    def __init__(self, params={}):
        """Initialise the statistics API."""
        super(StatisticsAPI, self).__init__(params)
        # Set the api_key for the requests
        self.statistics = self._init_api(statistics)
        # This API is a bit weird, so create the "authorization" string
        authorization = self.statistics.configuration.api_key['Authorization']
        self._auth = "Bearer %s" % (authorization,)
        # API requires to send what fields should be returned in response
        self._include_all = "devices,transactions,apikeys,"\
            "bootstraps_successful,bootstraps_failed,bootstraps_pending"

    def _convert_to_UTC_RFC3339(self, time):
        return time.isoformat() + "Z"

    def _verify_arguments(self, interval, kwargs):
        start = None
        end = None
        period = None
        if ('start' in kwargs) and (kwargs['start'] is not None):
            start = kwargs['start']
        if ('end' in kwargs) and (kwargs['end'] is not None):
            end = kwargs['start']
        if ('period' in kwargs) and (kwargs['period'] is not None):
            period = kwargs['period']
        if not start and not end and not period:
            raise ValueError("start and end is mandatory if period is not specified.")
        if start and not end:
            raise ValueError("end is required if start is specified.")
        if end and not start:
            raise ValueError("start is required if end is specified.")
        pattern = re.compile("[0-9]+[h|d|w]$")
        if period and not pattern.match(period):
            raise ValueError("period is incorrect. Sample values: 2h, 3w, 4d.")
        if interval and not pattern.match(interval):
            raise ValueError("interval is incorrect. Sample values: 2h, 3w, 4d.")
        if start:
            if not isinstance(start, datetime.datetime):
                raise ValueError("start should be of type datetime")
            kwargs['start'] = self._convert_to_UTC_RFC3339(start)
        if end:
            if not isinstance(end, datetime.datetime):
                raise ValueError("end should be of type datetime")
            kwargs['end'] = self._convert_to_UTC_RFC3339(end)

    @catch_exceptions(ApiException)
    def get_metric(self, include=None, interval="1d", **kwargs):
        """Get statistics.

        :param str include: What fields to include in response. None will return all.
        :param str interval: Group data by this interval in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
        :param datetime start: Fetch the data with timestamp greater than or equal to this value.
            The parameter is not mandatory, if the period is specified.
        :param datetime end: Fetch the data with timestamp less than this value.
            The parameter is not mandatory, if the period is specified.
        :param str period: Period. Fetch the data for the period in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
            The parameter is not mandatory, if the start and end time are specified
        :returns: a list of :py:class:`Metric` objects.
        """
        if not include:
            include = self._include_all
        self._verify_arguments(interval, kwargs)
        api = self.statistics.StatisticsApi()
        return api.v3_metrics_get(include, interval, self._auth, **kwargs).data

    @catch_exceptions(ApiException)
    def get_account_metric(self, include=None, interval="1d", **kwargs):
        """Get account-specific statistics.

        :param str include: What fields to include in response. None will return all.
        :param str interval: Group data by this interval in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
        :param datetime start: Fetch the data with timestamp greater than or equal to this value.
            The parameter is not mandatory, if the period is specified.
        :param datetime end: Fetch the data with timestamp less than this value.
            The parameter is not mandatory, if the period is specified.
        :param str period: Period. Fetch the data for the period in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
            The parameter is not mandatory, if the start and end time are specified
        :returns: a list of :py:class:`Metric` objects.
        """
        if not include:
            include = self._include_all
        self._verify_arguments(interval, kwargs)
        api = self.statistics.AccountApi()
        return api.v3_metrics_get(include, interval, self._auth, **kwargs).data


class Metric(MetricData):
    """Describes Metric object from statistics."""

    def __init__(self, data_obj):
        """Override __init__ and allow passing in backend object."""
        super(Metric, self).__init__(**data_obj.to_dict())
