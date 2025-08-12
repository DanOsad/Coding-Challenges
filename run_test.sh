#!/bin/bash

FILE_TO_TEST="$1"

if [[ -z "$FILE_TO_TEST" ]]; then
    echo "Usage: $(basename $(readlink -f "$0")) path/to/file.py"
    exit 1
fi

FILE_NAME=$(basename "$FILE_TO_TEST")

if [[ ! "$FILE_NAME" =~ \.py$ ]]; then
    echo "File must be a python script"
    exit 1
fi

# import the testcase.py module to system path
SCRIPT_DIR=$(dirname $(readlink -f "$0"))
TESTCASE_DIR="$SCRIPT_DIR/tests/testcase.py"
if [[ ! -f "$TESTCASE_DIR" ]]; then
    echo "testcase.py not found in the script directory"
    exit 1
fi

export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH" 
python3 "$FILE_TO_TEST"
if [[ $? -ne 0 ]]; then
    echo "Error running the script: $FILE_TO_TEST"
    exit 1
fi