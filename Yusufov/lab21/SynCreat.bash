#!/bin/bash
# Get suffix from command line arguments
suffix=$1

for file in *$suffix; do # iterate over all files with the specified suffix
    link_count=$(stat -c %h $file) # get the number of links in a file
    if [ $link_count -le 1 ]; then # check that the number of connections is greater than 1
    # Get filename without suffix
    filename=${file%.$suffix}
    # We get a new file name with a rearranged suffix
    new_filename=${suffix//./}${filename}
    # Create a new synonym file
    touch $file $new_filename
    fi
done

echo "Done!"
