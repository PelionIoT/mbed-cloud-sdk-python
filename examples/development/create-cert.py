"""Generate certficate header file."""
from ecdsa import NIST256p
from ecdsa import SigningKey
from six.moves import zip_longest
from mbed_cloud.access import AccessAPI


def _generate_cert_header_file(key_obj):
    return """
//----------------------------------------------------------------------------
//   The confidential and proprietary information contained in this file may
//   only be used by a person authorised under and to the extent permitted
//   by a subsisting licensing agreement from ARM Limited or its affiliates.
//
//          (C) COPYRIGHT 2013-2016 ARM Limited or its affiliates.
//              ALL RIGHTS RESERVED
//
//   This entire notice must be reproduced on all copies of this file
//   and copies of this file may only be made by a person if such person is
//   permitted to do so under the terms of a subsisting license agreement
//   from ARM Limited or its affiliates.
//----------------------------------------------------------------------------
/*
{publicPem}
{privatePem}*/
#ifndef __IDENTITY_DEV_SECURITY_H__
#define __IDENTITY_DEV_SECURITY_H__
#include <inttypes.h>
const char gIdcDevSecurityAccountId[33] = "{accountId}";
const uint8_t gIdcDevSecurityPrivateSignKey[32] = {{
{privateHex}
}};
""".format(**key_obj).strip()


def _grouper(n, iterable, padvalue=None):
    return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)


def _get_key():
    sk = SigningKey.generate(curve=NIST256p)
    vk = sk.verifying_key
    privHexGroups = [", ".join(g) for g in _grouper(8, [hex(i) for i in bytearray(sk.to_string())])]
    return {
        'privatePem': sk.to_pem().decode('utf-8'),
        'publicPem': vk.to_pem().decode('utf-8'),
        'privateHex': "\t" + ",\n\r\t".join(privHexGroups)
    }


def _main():
    # Get ECDSA private & public key
    k = _get_key()
    # Get the account ID of the current user
    api = AccessAPI()
    k['accountId'] = api.get_account_details().id
    print(_generate_cert_header_file(k))

if __name__ == "__main__":
    _main()
