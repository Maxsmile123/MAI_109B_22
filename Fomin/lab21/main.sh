#!/bin/bash

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--prefix)
            prefix="$2"
            shift 2;;
        -s|--suffix)
            suffix="$2"
            shift 2;;
        -root|--root)
            root="$2"
            shift 2;;
        -i|--insensitive)
            case_insensitive=true
            shift;;
        *)
            echo "Unknown argument: $1"
            exit 1;;
    esac
done

if [[ -z $prefix ]]; then
    prefix=""
fi

if [[ -z $suffix ]]; then
    suffix=""
fi

if [[ -z $root ]]; then
    root="./"
fi

get_files() {
    for file in $(find $root -type f); do
        if [[ $case_insensitive == true ]]; then
            if [[ $(echo $file | grep -i $suffix) ]]; then
                mv $file $(dirname $file)/$prefix$(basename $file)
            fi
        else
            if [[ $(echo $file | grep $suffix) ]]; then
                mv $file $(dirname $file)/$prefix$(basename $file)
            fi
        fi
    done
}

get_files