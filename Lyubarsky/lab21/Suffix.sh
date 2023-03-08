#!/usr/bin/bash

helpstr="usage: Suffix.py [-h] [-s S] [-n N] [-d D] [-f F]

This command writes the names and sizes of all executable files to the specified file.

options:
  -h, --help show this help message and exit
  -s S Write only files with the given STR suffix. Disabled by default.
  -n N Write to a file, the size of which must not exceed NUM bytes. The default value is 1024 bytes.
  -d D Search in the DIR directory. By default, the search occurs in the current directory.
  -f F Write to FIL file. By default, the recording goes to the Output_file."

number=1024
suffix=" "
directory="."
outputFile="Output_file"

for parameter in $*
do
    case "$parameter" in

        "--help" ) echo "$helpstr"; exit 0;;

        "-s" | "-n" | "-d" | "-f" ) flag=$var ;;

        * )
            if [ "$flag" = "-n" ]; then
                number=$var
            fi
            if [ "$flag" = "-d" ]; then
                directory="$var"
            fi
            if [ "$flag" = "-s" ]; then
                suffix="$var"
            fi
            if [ "$flag" = "-f" ]; then
                outputFile="$var"
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

sizeOfOutputFile=$(wc -c $v | cut -d ' ' -f1)

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