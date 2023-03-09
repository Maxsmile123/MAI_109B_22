#!/bin/bash

dir=""
src=""
trg=""
while getopts ":d:" ARG; do
    case "$ARG" in
d) dir=$OPTARG ;;
s) src=$OPTARG ;;
t) trg=$OPRARG ;;
    esac
done

bypass() {
    for file in "$1"/*; do
        if [ -d "$file" ]; then
            bypass "$file"
	elif [[ "$file" == *.txt ]]; then
	    iconv -f -name "$src*" -t -name "$trg" "$file" > "$file_1"
	    rm "$file"
	    mv "$file_1" "$file"
	fi
    done
}

bypass -name "$dir*"
