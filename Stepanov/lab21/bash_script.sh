#!/bin/bash

if [[ $# -ne 2 ]]
   then
	echo "Please , insert exactly argument with flag -s or --size: -s [SIZE]"
        echo ". [scriptname].sh --size [SIZE]"
        echo "Use flag -? with ? to get info about script"
elif [[ $2 == '?' && $1 == '-?' ]] ; then
        echo "this script implements a replacement for all files in the directory with a size less than the specified postfix by the first character of the file name."
        echo "[size] -max size of files in current directory to to consider them suitable"
        echo ". [scriptname].sh --size [SIZE]"
        echo "Use flag -? with ? to get info about script"
elif [[ $1 == '-s'|| $1 == '--size' ]] ; then
   for file in $(find -maxdepth 1 -type f -size -$2c)
            do
             file_name=$(echo $file | rev | cut -d '/' -f1 | rev)
             file_suffix=$(echo $file | rev | cut -d '.' -f1 | rev)
             size_of_file=$(echo $file_name | wc -c)
             size_of_suffix=$(echo $file_suffix | wc -c)
             file_prefix=$(echo $file_name | rev | cut -c $size_of_suffix- | rev)
             echo $file_prefix
             first_char_of_file=$(echo $file_name | cut -c 1)
             echo $file
             relative_path=$(echo $file | rev | cut -c  $size_of_file-  | rev)
             echo $relative_path$file_prefix$first_char_of_file
             $(mv --force -n $file $relative_path$file_prefix$first_char_of_file) 
           done
           echo "Done"
else 
   echo "Something went wrong, if  you need help, please, use that script with -? ?"
   echo ". [scriptname].sh --size [SIZE]"
   echo "Use flag -? with ? to get info about script"

fi
