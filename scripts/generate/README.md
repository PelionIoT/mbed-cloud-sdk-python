# Python SDK Renderer

Renders the Python SDK from an intermediate `yaml` file.

## Install
```
pip install scripts\generate
```

## CLI interface
```
python -m generate --help

usage: generator [-h] --source INPUT_FILE [--output OUTPUT_DIR] [-v] [--clean]

renders SDK foundation

optional arguments:
  -h, --help           show this help message and exit
  --source INPUT_FILE  The location of the input yaml.
  --output OUTPUT_DIR  The output directory.
  -v, --verbosity      increase output verbosity. can be specified multiple
                       times
  --clean              clean top level directory
```

## Usage
```
python -m generate --source=C:\coding\mbed-cloud-api-contract\out\sdk_gen_python.yaml --output=src\mbed_cloud\sdk
```