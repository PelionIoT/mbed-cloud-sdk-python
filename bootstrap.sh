#!/bin/bash
# Configuration
LIB_NAME="mbed_cloud_sdk"

echoerr() {
  echo "$@" 1>&2;
}

create_module() {
  mkdir -p mbed_cloud_sdk/$1;
  touch $LIB_NAME/$1/__init__.py;
}

move_module() {
  # $1: git directory for generated SDK
  # $2: api name in generated SDK
  # $3: module to place the api under in library
  # Example: 
  #     move_module $TMP_DIR iam devices
  SDK="$1/generated/python";
  cp -rp $SDK/$2/$2 $LIB_NAME/$3/

  # Ensure we get the documentation included too, for good measure.
  cp -rp $SDK/$2/README.md $LIB_NAME/$3/$2
  cp -rp $SDK/$2/docs $LIB_NAME/$3/$2
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
create_module devices;
create_module access;

# Create __init__.py file for top-level module
touch $LIB_NAME/__init__.py;

# Fetch generated code to tmp directory
TMP_DIR=$(mktemp -d);
git clone git@github.com:ARMmbed/mbed-cloud-sdk-codegen.git $TMP_DIR;

# Run the code generator for Python. First setup environment, then generate.
run_codegen $TMP_DIR

# Copy the different APIs into correct modules
move_module $TMP_DIR iam access
move_module $TMP_DIR mds devices

# Cleanup
rm -rf $TMP_DIR;
