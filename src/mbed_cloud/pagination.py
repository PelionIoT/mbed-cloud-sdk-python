# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Pagination"""
from itertools import islice


class PaginatedResponse(object):
    """Represents a sequence of results from the API

    To represent the potentially large number of results
    returned from an API query, the PaginatedResponse provides
    a lazily-evaluated generator which can be used to step through
    the full result set, fetching new pages of results as needed.

    response = PaginatedResponse(api_function)
    response.first()              {} first item
    response.all()                [{}, ...] all items
    list(response)                [{}, ...] all items from generator
    [item for item in response]   [{}, ...] iteration over generator
    """

    def __init__(self, func, lwrap_type=None, _results_cache=True, **kwargs):
        """Initialize wrapper by passing in object with metadata structure.

        :param func: API function called to obtain a page of results
        :param lwrap_type: Wrapper called for each returned result object
        :param _results_cache: Retains a copy of all returned results to reduce API calls
                               Set to None to disable (for use as a pure generator)
        """
        self._func = func
        self._lwrap_type = lwrap_type
        self._kwargs = {}
        self._kwargs.update(kwargs)

        # Initial values, will be updated in first response
        self._total_count = None
        self._next_id = None
        self._has_more = True
        self._is_exhausted = False
        self._results_cache = [] if _results_cache else None
        self._current_data_page = []
        self._current_count = 0
        self._limit = kwargs.get('limit')

    @property
    def _is_caching(self):
        return self._results_cache is not None

    @property
    def _is_at_query_limit(self):
        # we track query limit ourselves in case the API is too lenient
        return self._limit is not None and self._current_count >= self._limit

    def _get_total_concrete(self):
        # total number of results seen for certain, ignoring 'total_count' responses
        return self._current_count + len(self._current_data_page)

    def _get_next_page(self):
        query = {}
        query.update(self._kwargs)
        if self._next_id is not None:
            query.update(dict(after=self._next_id))

        resp = self._func(**query)

        for item in resp.data or []:
            self._current_data_page.append(self._lwrap_type(item) if self._lwrap_type else item)
        self._has_more = resp.has_more
        self._total_count = getattr(resp, 'total_count', None)
        if self._current_data_page:
            self._next_id = self._current_data_page[-1].id

    def _get_total_count(self):
        len_query = {}
        len_query.update(dict(include='total_count'))
        len_query.update(self._kwargs)
        len_query.update(dict(limit=2))
        resp = self._func(**len_query)
        return getattr(resp, 'total_count', 0)

    def count(self):
        """Approximate number of results, according to the API"""
        if self._total_count is None:
            self._total_count = self._get_total_count()
        return self._total_count

    def all(self):
        """All results"""
        all = list(self)
        if self._results_cache:
            return iter(self._results_cache)
        return all

    def first(self):
        """Returns the first item from the query, or None if there are no results"""
        if self._results_cache:
            return self._results_cache[0]

        query = PaginatedResponse(func=self._func, lwrap_type=self._lwrap_type, **self._kwargs)
        try:
            return next(query)
        except StopIteration:
            return None

    def next(self):
        """Next item in sequence (Python 2 compatibility)"""
        return self.__next__()

    def __next__(self):
        """Get the next element"""
        if not self._current_data_page and self._has_more:
            self._get_next_page()

        if not self._current_data_page or self._is_at_query_limit:
            self._is_exhausted = True
            raise StopIteration()

        self._current_count += 1
        result = self._current_data_page.pop(0)
        if self._is_caching:
            self._results_cache.append(result)
        return result

    def __iter__(self):
        """This instance can be iterated"""
        if not self._is_exhausted:
            return self
        if self._is_caching:
            return iter(self._results_cache)
        raise StopIteration()

    def __len__(self):
        """Most accurate known number of results"""
        return self._get_total_concrete() if self._is_exhausted else self.count()

    def __repr__(self):
        """First few elements of a query result"""
        limit = 3
        some = list(islice(self.all(), limit + 1))
        return '<%s %s%s>' % (
            self.__class__.__name__,
            ','.join(str(s) for s in some[:limit]),
            '...' if len(some) > limit else ''
        )

    def to_dict(self):
        """Internal state"""
        return dict(
            data=list(self),
            has_more=self._has_more,
            total_count=self.count(),
            limit=self._limit,
            after=self._kwargs.get('after'),
            order=self._kwargs.get('order', 'ASC')
        )

    @property
    def data(self):
        """Deprecated. Returns the data as a `list`"""
        import warnings
        warnings.warn(
            '`data` attribute is deprecated and will be removed in a future release, '
            'use %s as an iterable instead' % (PaginatedResponse,),
            category=DeprecationWarning,
            stacklevel=2  # log wherever '.data' is referenced, rather than this line
        )
        return list(self)
