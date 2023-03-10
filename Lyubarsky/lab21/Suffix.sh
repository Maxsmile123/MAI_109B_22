#!/usr/bin/bash

helpstr="usage: Suffix.py [-h] [-s SUFFIX] [-n NUMBER] [-d DIRECTORY] [-f FILE]

This command writes the names and sizes of all executable files to the specified file.

options:
  -h, --help            show this help message and exit
  -s SUFFIX, --suffix SUFFIX
                        Write only files with the given STR suffix. Disabled by default.
  -n NUMBER, --number NUMBER
                        Write to a file, the size of which must not exceed NUM bytes. The default value is 1024 bytes.
  -d DIRECTORY, --directory DIRECTORY
                        Search in the DIR directory. By default, the search occurs in the current directory.
  -f FILE, --file FILE  Write to FIL file. By default, the recording goes to the Output_file.
"

number=1024
suffix=" "
directory="."
outputFile="Output_file"

for parameter in $*
do
    case "$parameter" in

        "--help" ) echo "$helpstr"; exit 0;;

        "-s" | "-n" | "-d" | "-f" | "--number" | "--directory" | "--suffix" | "--file") flag=$parameter ;;

        * )
            if [ "$flag" = "-n" ] || [ "$flag" = "--number" ]; then
                number=$parameter
            fi
            if [ "$flag" = "-d" ] || [ "$flag" = "--directory" ]; then
                directory="$parameter"
            fi
            if [ "$flag" = "-s" ] || [ "$flag" = "--suffix" ]; then
                suffix="$parameter"
            fi
            if [ "$flag" = "-f" ] || [ "$flag" = "--file" ]; then
                outputFile="$parameter"
            fi
            ;;
    esac
done

olddir=$(pwd)
cd $directory
dirname=$(pwd)

list=$(ls -Rla | grep ^-)

cd $olddir
echo -n "" >> $outputFile

sizeOfOutputFile=$(wc -c $outputFile | cut -d ' ' -f1)

if [ $sizeOfOutputFile -gt $number ]; then
    echo "Заданный файл слишком большой!"
    exit 0
fi

IFS=$(printf '\n.'); IFS=${IFS%.}

for file in $list
do
    typeOfFile=$(echo $file | cut -c1-10 | grep x)
    if [ "$typeOfFile" != "" ]; then

        start=$(expr ${#file} - ${#suffix})
        start=$(expr $start + 1)

        sizeOfFile=$(echo $file | awk '{print $5}')
        suffixOfFile=$(echo $file | cut -c$start-${#file})

        if [ $suffixOfFile = $suffix ] || [ "$suffix" = " " ]; then
            echo "Размер: "$sizeOfFile"b Название: $(echo $file | awk '{print $9}')" >> $outputFile
        fi
    fi
done