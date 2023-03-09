#!/bin/bash

#cheking for file
if [ -f  "$1" ];
then
#generation
for i in $(seq 1 $2)
do
touch file$i.txt
done
else
echo "file not found"
fi
