#!/bin/bash
set -eo pipefail
IFS=$'\n\t'

OUTPUT_FORMAT="${1:-html}";
CONFIG_DIR="docs/";
SOURCE_DIR="docs/";
OUTPUT_DIR="docs/build/${OUTPUT_FORMAT}";

# Build Sphinx docs
sphinx-build -a -b $OUTPUT_FORMAT -c $CONFIG_DIR $SOURCE_DIR $OUTPUT_DIR;

# If AWS_ID and SECRET is defined, we push to S3
if [[ -n $AWS_ID && -n $AWS_SECRET ]]; then
  export AWS_ACCESS_KEY_ID=$AWS_ID;
  export AWS_SECRET_ACCESS_KEY=$AWS_SECRET;
  export AWS_DEFAULT_REGION=us-west-2;
  aws s3 sync --delete --cache-control max-age=3600 $OUTPUT_DIR s3://mbed-cloud-sdk-python;
fi
