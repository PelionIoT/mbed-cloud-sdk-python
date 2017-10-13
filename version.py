# Version number is composed based on API backend version and SDK version.
# Breaking changes in SDK will increment major version number.
# API version number will follow Mbed release schedule (~quarterly releases).
API_VERSION = "1.2"
SDK_MAJOR_MINOR = "2"
SDK_SUFFIX = ""
VERSION = "%s.%s%s" % (API_VERSION, SDK_MAJOR_MINOR, SDK_SUFFIX)
