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
file="Output_file"

for var in $*
do
    case "$var" in

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
                file="$var"
            fi
            ;;
    esac
done

olddir=$(pwd)
cd $directory
dirname=$(pwd)

list=$(ls -Rla | grep ^-)

cd $olddir
echo -n "" >> $file

sizeOfFile=$(wc -c $file | cut -d ' ' -f1)

IFS=$(printf '\n.'); IFS=${IFS%.}

if [ $sizeOfFile -gt $number ]; then
    echo "Заданный файл слишком большой!"
    exit 0
fi

for var in $list
do
    typeOfFile=$(echo $var | cut -c1-10 | grep x)
    if [ "$typeOfFile" != "" ]; then

        start=$(expr ${#var} - ${#suffix})
        start=$(expr $start + 1)

        sizeOfFile=$(echo $var | awk '{print $5}')
        suffixOfFile=$(echo $var | cut -c$start-${#var})

        if [ $suffixOfFile = $suffix ] || [ "$suffix" = " " ]; then
            echo "Размер: "$sizeOfFile"b Название: $(echo $var | awk '{print $9}')" >> $file
        fi
    fi
done