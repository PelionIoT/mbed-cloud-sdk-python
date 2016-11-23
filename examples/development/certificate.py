import sys
from mbed_cloud_sdk.development.certificate import CertificateAPI

DUMMY_PUB_KEY = """
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENVRAgPj7Ra2K/BqejIhY+oSRylHS
CdV7NZ9yEDGifNYYi0nZVpHwmbepoMbBW7jTJKjNDHaf8MhBsKPd0yyI4Q==
"""

def print_certificate(cert):
    body = "* %s (%s) *" % (cert.pub_key, cert.created_at)
    print "*" * len(body)
    print body
    print "*" * len(body)

def main():
    api = CertificateAPI()
    cert = api.get_certificate()

    if cert:
        print "Current certificate:"
        print_certificate(cert)

        api.revoke_certificate()
        print "Revoked current certificate. Creating new one..."

    # Get public key from first argument on command line
    pub_key = DUMMY_PUB_KEY.strip().replace("\n","")
    if len(sys.argv) == 2:
        pub_key = sys.argv[1]

    api.create_certificate(pub_key)
    print "Created new certificate!"
    print_certificate(api.get_certificate())

if __name__ == "__main__":
    main()
