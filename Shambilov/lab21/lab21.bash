#!/bin/bash

dir=""
while getopts ":d:" ARG; do
    case "$ARG" in
d) dir=$OPTARG ;;
    esac
done

bypass() {
    for file in "$1"/*; do
        if [ -d "$file" ]; then
            bypass "$file"
	elif [[ "$file" == *.txt ]]; then
	    iconv -f UTF-8 -t UTF-16 "$file" > "$file_1"
	    rm "$file"
	    mv "$file_1" "$file"
	fi
    done
}

bypass "$dir*"
