#!/bin/bash

while [ -n "$1" ]
do
case "$1" in
    -suf) suffix="$2"
    shift;;
    -f) fileName="$2"
    shift;;
    --) shift
    break;;
    *) echo "Option $1 isn't correct. Please enter options correctly"
    exit;;
esac
shift
done

entranceCheck_1=0
baseName="${fileName%%.*}"

if [[ !(-f "$fileName") ]];
then
    echo "File not found"
    exit
fi

if [[ $baseName != *"$suffix" ]];
then
    echo "File's suffix doesn't match entered suffix"
    exit
fi

for file in *;
do
    if [[ -f "$file" ]] && [[ "$file" != "$fileName" ]];
    then 
        baseName="${file%%.*}"
        if [[ $baseName == *"$suffix" ]] && cmp -s "$fileName" "$file";
        then         
            rm "$file"
            entranceCheck_1=1
        fi
    fi
done
     
if [[ $entranceCheck_1 == 0 ]];
then
    echo "No matches found"
fi