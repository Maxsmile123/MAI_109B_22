#!/bin/bash

while getopts ":c:" ARG;
do
        case "$ARG" in 
c) catalog="$OPTARG" ;;
        esac
done

if [[ ! -d "$catalog" ]]; then
        echo "Catalog $catalog doesn't exist"
        exit 1
fi

count_changed_files=0

for file in $(find "$catalog" -type f -name "Makefile*");
do
        sed -i 's/\\/\//' "$file"
        echo "Changed path to file: $file"
        count_changed_files=$((count_changed_files+1))
done

echo "Number of changed files: $count_changed_files"