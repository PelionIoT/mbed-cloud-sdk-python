from mbed_cloud_sdk.development.certificate import CertificateAPI

def print_certificate(cert):
    body = "* %s (%s) *" % (cert.pub_key, cert.created_at)
    print "*" * len(body)
    print body
    print "*" * len(body)

def main():
    api = CertificateAPI()
    cert = api.get_certificate()
    if cert:
        print_certificate(cert)
    else:
        print "No certificate found"

if __name__ == "__main__":
    main()
