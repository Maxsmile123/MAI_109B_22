import os
import argparse

# The function accepts and returns the specified suffix.
def args():
    ParserSuf = argparse.ArgumentParser(description = "Suffix")
    ParserSuf.add_argument("suffix", type = str, help = "Suffix of file")
    args = ParserSuf.parse_args()
    return args
    
# A function that filters files by suffix and number of links and gets filtered_files - a list of files suitable for creating a synonym
def filtr_files():
    # Get a list of all files in the current directory
    files = os.listdir()
    filtered_files = [f for f in files if f.endswith(args().suffix) and os.stat(f).st_nlink <= 1]
    return filtered_files
    
def main():
    for f in filtr_files():
        # We get the new filename by concatenating args().suffix[1:] - creates the suffix text without the dot and f.replace(args().suffix, '') - replaces the suffix in the original filename with "".
        new_name = args().suffix[1:] + f.replace(args().suffix, '')
        os.symlink(f, new_name)
if __name__ =='__main__':
    main()

