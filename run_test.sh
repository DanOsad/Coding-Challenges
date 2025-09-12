#!/bin/bash

search_pattern="$1"

if [[ -z "$search_pattern" ]]; then
    echo "Usage: $(basename $(readlink -f "$0")) <search_pattern>"
    echo "Examples:"
    echo "  ./run_test.sh 83          # Find and run problem 83"
    echo "  ./run_test.sh anagram     # Find and run problems containing 'anagram'"
    exit 1
fi

SCRIPT_DIR=$(dirname $(readlink -f "$0"))
TESTCASE_DIR="$SCRIPT_DIR/tests/testcase.py"
if [[ ! -f "$TESTCASE_DIR" ]]; then
    echo "testcase.py not found in the script directory"
    exit 1
fi

if [[ -f "$search_pattern" ]]; then
    "$selected_file" = "$search_pattern"
else
    # Find all Python files in src directories that match the pattern
    mapfile -t matching_files < <(find "$SCRIPT_DIR/src" -type f -name "*.py" | grep -i "$search_pattern")
    num_matches=${#matching_files[@]}

    if [ "$num_matches" -eq 0 ]; then
        echo "No matching files found for pattern: $search_pattern"
        exit 1
    elif [ "$num_matches" -eq 1 ]; then
        selected_file="${matching_files[0]}"
        echo "Found one matching file: $selected_file"
    else
        echo "Found multiple matching files:"
        for i in "${!matching_files[@]}"; do
            echo "[$((i+1))] ${matching_files[$i]}"
        done

        while true; do
            echo -n "Select a file number (1-$num_matches): "
            read selection
            if [[ "$selection" =~ ^[0-9]+$ ]] && [ "$selection" -ge 1 ] && [ "$selection" -le "$num_matches" ]; then
                selected_file="${matching_files[$((selection-1))]}"
                break
            else
                echo "Invalid selection. Please enter a number between 1 and $num_matches"
            fi
        done
    fi
fi

echo -e "\nRunning tests for: $selected_file\n"

source "$SCRIPT_DIR/.venv/bin/activate"
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH" 
python3 "$selected_file"
exit_code=$?
deactivate

if [[ $exit_code -ne 0 ]]; then
    echo -e "\nError running the script: $selected_file"
    exit 1
fi