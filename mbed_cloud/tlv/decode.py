# python 2 / 3 compatible tlv parser
from base64 import b64decode
from binascii import a2b_base64
from functools import partial
from functools import reduce

b64decoder = a2b_base64

type_mask = int("11000000", 2)
id_length_mask = int("00100000", 2)
length_type_mask = int("00011000", 2)
length_mask = int("00000111", 2)

path_sep = '/'


class Types(object):
    OBJECT = int("00000000", 2)  # Object Instance with one or more TLVs
    RESOURCE = int("01000000", 2)  # Resource Instance with Value in multi Resource TLV
    MULTI = int("10000000", 2)  # Multiple Resource, Value contains one or more Resource Instance
    VALUE = int("11000000", 2)  # Resource with Value


class LengthTypes(object):
    ONE_BYTE = int("00001000", 2)  # Length is 8-bits
    TWO_BYTE = int("00010000", 2)  # Length is 16-bits
    THR_BYTE = int("00011000", 2)  # Length is 24-bits
    SET_BYTE = int("00000000", 2)  # Length is specified in bits 2-0

    to_ints = {
        ONE_BYTE: 1,
        TWO_BYTE: 2,
        THR_BYTE: 3,
    }


def get_id_length(byte):
    return 2 if byte & length_type_mask == id_length_mask else 1


def get_value_length(byte):
    length_value = byte & length_mask
    return LengthTypes.to_ints.get(length_value, length_value)


def combine_bytes(bytearr):
    """
    given some bytes
    join them together to make one long binary
    (e.g. 00001000 00000000   ->    0000100000000000)
    :param bytearr:
    :return:
    """
    # FIXME: if this is terrible, do the bitshifting stuff instead
    return int(''.join(['{0:08b}'.format(b) for b in bytearr]), 2)


def binary_tlv_to_python(binary_string, result=None, path=''):
    """
    recursively decode a binary string and store output in result object
    :param binary_string:
    :param result:
    :param path:
    :return:
    """
    result = {} if result is None else result

    if not binary_string:
        return result

    byte = binary_string[0]
    kind = byte & type_mask
    id_length = get_id_length(byte)
    payload_length = get_value_length(byte)

    # start after the type indicator
    offset = 1
    item_id = combine_bytes(binary_string[offset:offset + id_length])
    offset += id_length
    new_path = path_sep.join((path, item_id))

    # get length of payload from specifier
    value_length = payload_length
    if byte & length_type_mask != LengthTypes.SET_BYTE:
        value_length = combine_bytes(binary_string[offset:offset + payload_length])
        offset += payload_length

    if kind == Types.MULTI:
        binary_tlv_to_python(binary_string[offset:offset + value_length], result, new_path)
    else:
        value_binary = binary_string[offset, offset + value_length]
        value = combine_bytes(value_binary)
        # TODO has_zero = ??
        result[new_path] = value

    offset += value_length
    binary_tlv_to_python(binary_string[offset:], result, path)
    return result


def maybe_decode_payload(payload, content_type='application/nanoservice-tlv'):
    if 'tlv' in content_type.lower():
        binary = a2b_base64(payload)
        return binary_tlv_to_python(binary)
    return payload
