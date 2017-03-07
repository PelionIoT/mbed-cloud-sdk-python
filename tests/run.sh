#!/bin/bash
set -o pipefail
IFS=$'\n\t'

TMPDIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'tmprunner');
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
ROOT_DIR=$(dirname "$DIR");
BACKEND_URL="${BACKEND_URL:-"http://localhost:5000"}";

cleanup() {
  echo "Test run finished. Cleaning up. Deleting tmp directory: $TMPDIR";
  if is_running $BACKEND_PID; then
    echo "Killing backend SDK server: $BACKEND_PID";
    kill $BACKEND_PID;
  fi
  rm -rf "$TMPDIR";
}

is_running() {
  if ps -p $1 >/dev/null; then
    return 0;
  fi
  return 1;
}

# Ensure we have API key
API_KEY="${MBED_CLOUD_API_KEY}"
if [ -z $API_KEY ]; then
  >&2 echo "API Key needs to be set using MBED_CLOUD_API_KEY env var";
  exit 1;
fi

# Clone the test runner repo and install virtual environment
git clone https://${GITHUB_TOKEN:-git}@github.com/ARMmbed/mbed-cloud-sdk-testrunner.git "$TMPDIR"
virtualenv $TMPDIR/venv
$TMPDIR/venv/bin/pip install -r $ROOT_DIR/requirements.txt
TRUNNER_DIR=$TMPDIR;

# Start the Python SDK test backend server. Send to background.
export FLASK_APP=$DIR/server.py
CMD="$TRUNNER_DIR/venv/bin/flask run"
eval "$CMD &"
echo "Backend server started. PID: $!"
BACKEND_PID=$!

# Sleep for a second whilst the server starts up
sleep 1
if ! is_running $BACKEND_PID; then
  >&2 echo "Backend server did not start successfully."
  cleanup
  exit 1
fi

# Start the test runner
export PYTHONPATH="$TRUNNER_DIR:$PYTHONPATH"
$TRUNNER_DIR/venv/bin/python $TRUNNER_DIR/bin/trunner -s $BACKEND_URL -k $API_KEY
RET_CODE=$?

# Kill the backend server & cleanup
cleanup
exit $RET_CODE
