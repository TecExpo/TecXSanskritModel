#!/bin/bash

# Define directories
INPUT_FOLDER="./raw_sanskrit"
OUTPUT_FOLDER="./tokenized_sanskrit"

# Create output folder if missing
mkdir -p "$OUTPUT_FOLDER"

echo "Batch processing starting..."

# Iterate through every .txt file
for file in "$INPUT_FOLDER"/*.txt; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")
        echo "Processing: $filename"
        
        # Execute the Python validator for each file
        python3 sanskrit_processor.py "$file" "$OUTPUT_FOLDER/$filename"
    fi
done

echo "Successfully processed all files. Results in $OUTPUT_FOLDER."

