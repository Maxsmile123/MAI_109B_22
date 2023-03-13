#!/bin/bash

while [ -n "$1" ]
do
case "$1" in
    -f) filename="$2"
    shift ;;
    -n) num_copies="$2"
    shift ;;
    --) shift
    break ;;
    *) echo "$1 is not an option";;
esac
shift
done


#cheking for file
if [ -f  "$filename" ];
then

#generation
for i in $(seq 1 $num_copies)
do
touch $filename$i
done

else
echo "file not found"
fi

