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
import re
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions

# Import backend API
import mbed_cloud._backends.statistics as statistics
from mbed_cloud._backends.statistics.models import Data
from mbed_cloud._backends.statistics.rest import ApiException

class StatisticsAPI(BaseAPI):
    """API reference for the Statistics API.
    Exposing functionality for getting statistics data.
    """
    def __init__(self, params={}):
        """Initialise the development API, optionally passing in overriding config."""
        super(StatisticsAPI, self).__init__(params)
        # Set the api_key for the requests
        self.statistics = self._init_api(statistics)
        # This API is a bit weird, so create the "authorization" string
        self._auth = "Bearer %s" % (self.statistics.configuration.api_key['Authorization'],)
        self._include_all = "devices"
        #self._include_all = "devices, transactions, bootstraps_successful, bootstraps_failed, bootstraps_pending, " \
        #"bootstrap_certificate_create, bootstrap_certificate_delete, connector_certificate_create, " \
        #"connector_certificate_delete, bootstrap_credentials_get, bootstrap_full_credentials_get, " \
        #"connector_credentials_get, connector_full_credentials_get, connector_ca_rest_api_count, " \
        #"connector_ca_rest_api_error_count"

    def _verify_arguments(self, start, end, period, interval):
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

    def _convert_to_UTC_RFC3339(self, time):
        return time.isoformat("T") + "Z"

    @catch_exceptions(ApiException)
    def get_metric(self, include=None, start=None, end=None, period="30d", interval="1d", **kwargs):
        """Get statistics.
        :param str include: What fields to include in response. None will return all.
        :param datetime start: UTC time/year/date in RFC3339 format. 
            Fetch the data with timestamp greater than or equal to this value. 
            Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.
            The parameter is not mandatory, if the period is specified.
        :param datetime end: UTC time/year/date in RFC3339 format. 
            Fetch the data with timestamp less than this value.
            Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.
            The parameter is not mandatory, if the period is specified.
        :param str period: Period. Fetch the data for the period in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
            The parameter is not mandatory, if the start and end time are specified
        :param str interval: Group data by this interval in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
        :returns: a list of :py:class:`Metric` objects.
        """
        if not include:
            include = self._include_all
        self._verify_arguments(start, end, period, interval)
        if start:
            start = self._convert_to_UTC_RFC3339(start)
            kwargs['start'] = start
        if end:
            end = self._convert_to_UTC_RFC3339(end)
            kwargs['end'] = start
        if period:
            kwargs['period'] = period
        api = self.statistics.StatisticsApi()
        return api.v3_metrics_get(include, interval, self._auth, **kwargs)
    
    @catch_exceptions(ApiException)
    def get_account_metric(self, include=None, start=None, end=None, period="30d", interval="1d", **kwargs):
        """Get account-specific statistics.
        :param str include: What fields to include in response. None will return all.
        :param datetime start: UTC time/year/date in RFC3339 format. 
            Fetch the data with timestamp greater than or equal to this value. 
            Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.
            The parameter is not mandatory, if the period is specified.
        :param datetime end: UTC time/year/date in RFC3339 format. 
            Fetch the data with timestamp less than this value.
            Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.
            The parameter is not mandatory, if the period is specified.
        :param str period: Period. Fetch the data for the period in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
            The parameter is not mandatory, if the start and end time are specified
        :param str interval: Group data by this interval in days, weeks or hours.
            Sample values: 2h, 3w, 4d.
        :returns: a list of :py:class:`Metric` objects.
        """
        if not include:
            include = self._include_all
        self._verify_arguments(start, end, period, interval)
        if start:
            start = self._convert_to_UTC_RFC3339(start)
            kwargs['start'] = start
        if end:
            end = self._convert_to_UTC_RFC3339(end)
            kwargs['end'] = start
        if period:
            kwargs['period'] = period
        api = self.statistics.AccountApi()

        return api.v3_metrics_get(include, interval, self._auth, **kwargs)

class Metric(Data):
    """Describes Metric object from statistics."""

    def __init__(self, data_obj):
        """Override __init__ and allow passing in backend object."""
        super(Metric, self).__init__(**data_obj.to_dict())

        