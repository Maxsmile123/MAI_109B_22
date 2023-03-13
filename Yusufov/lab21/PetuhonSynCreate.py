import os
import argparse

# The function accepts and returns the specified suffix.
def args():
    ParserSuf = argparse.ArgumentParser(description = "Suffix")
    ParserSuf.add_argument("--suffix", "-s", type = str, help = "Suffix of file")
    args = ParserSuf.parse_args()
    return args

def get_files():
    files = os.listdir()
    filtered_files = [f for f in files if f.endswith(args().suffix) and os.stat(f).st_nlink <= 1]
    return filtered_files
    
def main():
    for f in get_files():
        suff_without_dot = args().suffix[1:]
        filename_without_suff = f.replace(args().suffix, "")
        new_name = suff_without_dot + filename_without_suff
        os.symlink(f, new_name)
if __name__ =='__main__':
    main()

