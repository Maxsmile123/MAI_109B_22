#!/bin/bash

if [[ $# -ne 1 ]]
   then
	echo "Pleace,insert exactly 1 argument -size"
        echo ". [scriptname].sh [size]"
elif [[ $1 = '?' ]]
   then
        echo "this script implements a replacement for all files in the directory with a size less than the specified postfix by the first character of the file name."
        echo "[size] -max size of files in current directory to to consider them suitable"
else
   for file in $(find -maxdepth 1 -type f -size -$1c)
            do
             file_name=$(echo $file|rev|cut -d '/' -f1|rev)
             file_suff=$(echo $file|rev|cut -d '.' -f1|rev)
             size_of_file=$(echo $file_name|wc -c)
             size_of_suf=$(echo $file_suff|wc -c)
             pref_file=$(echo $file_name|rev|cut -c $size_of_suf-|rev)
             echo $pref_file
             fl=$(echo $file_name|cut -c 1)
             echo $file
             not_an_abs_path=$(echo $file|rev|cut -c  $size_of_file- |rev)
             echo $not_an_abs_path$pref_file$fl
             $(mv --force -n $file $not_an_abs_path$pref_file$fl) 
           done
           echo "Done"
fi
