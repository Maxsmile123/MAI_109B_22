#!/bin/bash

function help {
    echo "usage: ./script --input=[]"
    echo "--input - source directory with subdirectories"
}

function encoding {
    if [[ $# -ne 1 ]]; then
        help
    else
        for file in $(find "$1" -type f -name "*.txt"); do
            echo "File encoding: $file"
            echo "File content: $(cat "$file")"
            cat "$file" | tr '[A-Z]' '[D-ZA-C]' | tr '[a-z]' '[d-za-c]' | tee "$file"
            echo "New file content: $(cat "$file")"
        done
        echo "Done!"
    fi
}

function parse_args {
    for arg in "$@"; do
        case $arg in
            --input=*)
                flag="${arg#*=}"
                encoding "${flag}"
                ;;
            --help)
                help
                exit
                ;;
            *)
                echo "unknown parameter: $arg"
                help
                exit
                ;;
        esac
    done
}

parse_args "$@"
