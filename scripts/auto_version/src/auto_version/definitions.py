from collections import namedtuple

SemVerFields = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVer = SemVerFields(*SemVerFields._fields)
