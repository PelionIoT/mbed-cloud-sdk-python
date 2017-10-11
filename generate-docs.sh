#!/bin/bash
set -eo pipefail
IFS=$'\n\t'

OUTPUT_FORMAT="${1:-html}";
CONFIG_DIR="docs/";
SOURCE_DIR="docs/";
OUTPUT_DIR="docs/build/${OUTPUT_FORMAT}";

# Build Sphinx docs
sphinx-build -a -b $OUTPUT_FORMAT -c $CONFIG_DIR $SOURCE_DIR $OUTPUT_DIR;
