#!/bin/bash

dir=""
while getopts ":d:" ARG; do
	case "$ARG" in
	d) dir=$OPTARG ;;
	esac
done

evade() {
	for file in "$1"/*; do
		if [ -d "$file" ]; then
			evade "$file"
		elif [[ "$file" == *.txt ]]; then
			iconv -f utf-8 -t utf-16 "$file" > "$file_1"
			rm "$file"
			mv "$file_1" "$file"
		fi
	done
}

evade "$dir*"
