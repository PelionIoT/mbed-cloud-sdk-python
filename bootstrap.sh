#!/bin/bash
# Configuration
LIB_NAME="mbed_cloud_sdk"

echoerr() {
  echo "$@" 1>&2;
}

move_modules() {
  # $1: git directory for generated SDK
  # Example: 
  #     move_module $TMP_DIR
  SDK="$1/generated/python";
  for d in $SDK/*/; do 
    DIR=$(basename "$d");
    cp -rp $SDK/$DIR/$DIR $LIB_NAME/_backends/$DIR;

    # Ensure we get the documentation included too, for good measure.
    cp -rp $SDK/$DIR/README.md $LIB_NAME/_backends/$DIR;
    cp -rp $SDK/$DIR/docs $LIB_NAME/_backends/$DIR;
  done
}

run_codegen() {
  virtualenv $1/venv/
  $1/venv/bin/pip install -r $1/requirements.txt
  $1/venv/bin/python $1/runner.py python
}

# Ensure we call the script from script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
CURRENT_DIR=$(pwd);
if [ $SCRIPT_DIR != $CURRENT_DIR ]; then
  echoerr "Script should be executed from script directory ($SCRIPT_DIR). Aborting.";
  exit 1;
fi

# Create structure, per the docs
# See: https://github.com/ARMmbed/mbed-cloud-sdk-codegen/docs/high-level-structure.md
# create_module devices;
# create_module access;

# Create __init__.py file for top-level module and backends
touch $LIB_NAME/__init__.py;
mkdir -p $LIB_NAME/_backends;
touch $LIB_NAME/_backends/__init__.py;

# Fetch generated code to tmp directory
TMP_DIR=$(mktemp -d);
git clone git@github.com:ARMmbed/mbed-cloud-sdk-codegen.git $TMP_DIR;

# Run the code generator for Python. First setup environment, then generate.
run_codegen $TMP_DIR

# Copy the different APIs into correct modules
move_modules $TMP_DIR

# Cleanup
rm -rf $TMP_DIR;
