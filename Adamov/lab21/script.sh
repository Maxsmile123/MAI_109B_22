#!/bin/bash

total_lines=0

count_lines() {
    local file="$1"
    if [[ -f "$file" ]]; then
        if [[ ($file == *.h) || ($file = *.cpp) ]]; then
            lines=$(wc -l < "$file")
            echo "$file: $lines"
            total_lines=$((total_lines + lines))
        fi

    elif [[ -d "$file" ]]; then
        for subfile in "$file"/*; do
            count_lines "$subfile"
        done
    fi
}

count_lines $1
echo "Total: $total_lines"
