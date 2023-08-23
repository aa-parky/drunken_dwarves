#!/bin/bash

# Source and destination file paths
source_file="2023-08-23_07-31-48_generated_names.txt"
destination_file="input.txt"

# Check if the source file exists
if [ -f "$source_file" ]; then
    # Copy the contents of the source file to the destination file
    cp "$source_file" "$destination_file"
    echo "Contents of $source_file copied to $destination_file"
else
    echo "$source_file does not exist."
fi

