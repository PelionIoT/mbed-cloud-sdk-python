# python 2 / 3 compatible tlv parser
from binascii import a2b_base64
import itertools


def b64decoder(input):
    return bytearray(a2b_base64(input))


type_mask = 0b11000000
id_length_mask = 0b00100000
length_type_mask = 0b00011000
length_mask = 0b00000111


class Types(object):
    OBJECT = 0b00000000  # Object Instance with one or more TLVs
    RESOURCE = 0b01000000  # Resource Instance with Value in multi Resource TLV
    MULTI = 0b10000000  # Multiple Resource, Value contains one or more Resource Instance
    VALUE = 0b11000000  # Resource with Value


class LengthTypes(object):
    ONE_BYTE = 0b00001000  # Length is 8-bits
    TWO_BYTE = 0b00010000  # Length is 16-bits
    THR_BYTE = 0b00011000  # Length is 24-bits
    SET_BYTE = 0b00000000  # Length is specified in bits 2-0

    to_ints = {
        ONE_BYTE: 1,
        TWO_BYTE: 2,
        THR_BYTE: 3,
    }


def get_id_length(byte):
    return 2 if byte & id_length_mask == id_length_mask else 1


def get_value_length(byte):
    length_value = byte & length_type_mask
    return LengthTypes.to_ints.get(length_value, byte & length_mask)


def combine_bytes(bytearr):
    """
    given some bytes
    join them together to make one long binary
    (e.g. 00001000 00000000   ->    0000100000000000)
    :param bytearr:
    :return:
    """
    bytes_count = len(bytearr)
    result = 0b0
    for index, byt in enumerate(bytearr):
        offset_bytes = bytes_count - index - 1
        result += byt << (8 * offset_bytes)
    return result


def binary_tlv_to_python(binary_string, result=None, path=tuple()):
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
    new_path = tuple(itertools.chain(path, (item_id,)))

    # get length of payload from specifier
    value_length = payload_length
    if byte & length_type_mask != LengthTypes.SET_BYTE:
        value_length = combine_bytes(binary_string[offset:offset + payload_length])
        offset += payload_length

    if kind == Types.MULTI:
        binary_tlv_to_python(binary_string[offset:offset + value_length], result, new_path)
    else:
        value_binary = binary_string[offset: offset + value_length]
        result[new_path] = combine_bytes(value_binary) if not all(value_binary) else value_binary.decode('utf8')

    offset += value_length
    binary_tlv_to_python(binary_string[offset:], result, path)
    return result


def maybe_decode_payload(payload, content_type='application/nanoservice-tlv'):
    """
    if the payload is tlv, decode it, otherwise passthrough
    :param payload:
    :param content_type:
    :return:
    """
    if 'tlv' in content_type.lower():
        binary = b64decoder(payload)
        return binary_tlv_to_python(binary)
    return payload
