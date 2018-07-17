"""Shorthand definitions for SemVer objects"""
from collections import namedtuple

SemVer = namedtuple('SemVerFields', ['major', 'minor', 'patch'])
SemVerSigFig = SemVer(*SemVer._fields)
