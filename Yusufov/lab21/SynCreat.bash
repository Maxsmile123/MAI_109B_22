#!/bin/bash
# Get suffix from command line arguments
suffix=$1

for file in *$suffix; do
    link_count=$(stat -c %h $file)
    if [ $link_count -le 1 ]; then
    filename=${file%.$suffix}
    # We get a new file name with a rearranged suffix
    new_filename=${suffix//./}${filename}
    touch $file $new_filename
    fi
done

echo "Done!"
