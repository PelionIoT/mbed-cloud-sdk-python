# ---------------------------------------------------------------------------
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
"""Filter logic"""

import copy
import datetime
from six.moves import urllib

from mbed_cloud.exceptions import CloudValueError


class OP:  # noqa
    """Filter Operators"""

    NE = 'ne'
    EQ = 'eq'
    GTE = 'gte'
    LTE = 'lte'


FILTER_OPERATOR_ALIASES = {
    'neq': 'neq',
    OP.NE: 'neq',
    OP.EQ: 'eq',
    OP.GTE: 'gte',
    OP.LTE: 'lte'
}


def _depluralise_filters_key(kwargs):
    """Filter/Filters -> Filter"""
    if 'filters' in kwargs:
        kwargs['filter'] = kwargs.pop('filters')
    return kwargs


def _normalise_value(value):
    if isinstance(value, datetime.datetime):
        value = value.isoformat() + "Z"
    return value


def _normalise_key_values(filter_obj, attr_map=None):
    """Converts nested dictionary filters into django-style key value pairs

    Map filter operators and aliases to operator-land
    Additionally, perform replacements according to attribute map
    Automatically assumes __eq if not explicitly defined
    """
    new_filter = {}
    for key, constraints in filter_obj.items():
        aliased_key = key
        if attr_map is not None:
            aliased_key = attr_map.get(key)
            if aliased_key is None:
                raise CloudValueError(
                    'Invalid key %r for filter attribute; must be one of:\n%s' % (
                        key,
                        attr_map.keys()
                    )
                )
        if not isinstance(constraints, dict):
            constraints = {'eq': constraints}
        for operator, value in constraints.items():
            # FIXME: deprecate this $ nonsense
            canonical_operator = FILTER_OPERATOR_ALIASES.get(operator.lstrip('$'))
            if canonical_operator is None:
                raise CloudValueError(
                    'Invalid operator %r for filter key %s; must be one of:\n%s' % (
                        operator,
                        key,
                        FILTER_OPERATOR_ALIASES.keys()
                    )
                )
            canonical_key = str('%s__%s' % (aliased_key, canonical_operator))
            new_filter[canonical_key] = _normalise_value(value)
    return new_filter


def _get_filter(sdk_filter, attr_map):
    """Common functionality for filter structures

    :param sdk_filter: {field:constraint, field:{operator:constraint}, ...}
    :return: {field__operator: constraint, ...}
    """
    if not isinstance(sdk_filter, dict):
        raise CloudValueError('filter value must be a dictionary, was %r' % (sdk_filter,))
    custom = sdk_filter.pop('custom_attributes', {})
    new_filter = _normalise_key_values(filter_obj=sdk_filter, attr_map=attr_map)
    new_filter.update({
        'custom_attributes__%s' % k: v for k, v in _normalise_key_values(filter_obj=custom).items()
    })
    return new_filter


def legacy_filter_formatter(kwargs, attr_map):
    """Builds a filter for update and device apis

    :param kwargs: expected to contain {'filter/filters': {filter dict}}
    :returns: {'filter': 'url-encoded-validated-filter-string'}
    """
    params = _depluralise_filters_key(copy.copy(kwargs))
    new_filter = _get_filter(sdk_filter=params.pop('filter', {}), attr_map=attr_map)
    if new_filter:
        new_filter = sorted([(k.rsplit('__eq')[0], v) for k, v in new_filter.items()])
        params['filter'] = urllib.parse.urlencode(new_filter)
    return params


def filter_formatter(kwargs, attr_map):
    """Builds a filter according to the cross-api specification

    :param kwargs: expected to contain {'filter': {filter dict}}
    :returns: {validated filter dict}
    """
    params = _depluralise_filters_key(copy.copy(kwargs))
    params.update(_get_filter(sdk_filter=params.pop('filter', {}), attr_map=attr_map))
    return params
