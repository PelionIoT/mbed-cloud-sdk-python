#!/bin/bash
set -o pipefail
IFS=$'\n\t'

TRUNNER_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'tmprunner');
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
ROOT_DIR=$(dirname "$DIR");
BACKEND_URL="${BACKEND_URL:-"http://localhost:5000"}";

cleanup() {
  echo "Test run finished. Cleaning up. Deleting tmp directory: $TRUNNER_DIR";
  if is_running $BACKEND_PID; then
    echo "Killing backend SDK server: $BACKEND_PID";
    kill $BACKEND_PID;
  fi
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
git clone -b dockerise https://${GITHUB_TOKEN:-git}@github.com/ARMmbed/mbed-cloud-sdk-testrunner.git "$TRUNNER_DIR"
pip install -r $ROOT_DIR/requirements.txt
pip3 install -r $ROOT_DIR/requirements.txt
export PYTHONPATH="$ROOT_DIR:$PYTHONPATH"

# Start the Python SDK test backend server. Send to background.
CMD="python $DIR/server.py"
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

docker build -t trunner . && docker run --rm -it --name runner --net="host" -p 5000:5000 trunner
RET_CODE=$?

# Kill the backend server & cleanup
cleanup

if [ $RET_CODE -eq 0 ]; then
  # Run server in python3
  CMD="python3 $DIR/server.py"
  eval "$CMD &"
  echo "Backend server in python 3 started. PID: $!"
  BACKEND_PID=$!
  # Sleep for a second whilst the server starts up
  sleep 1
  if ! is_running $BACKEND_PID; then
    >&2 echo "Backend server did not start successfully."
    cleanup
    exit 1
  fi
  # Start the test runner
  python -u $TRUNNER_DIR/bin/trunner ${PARAMS[@]}
  RET_CODE=$?
fi
# Kill the backend server & cleanup
cleanup
# Remove temp folder
rm -rf "$TRUNNER_DIR";

exit $RET_CODE
