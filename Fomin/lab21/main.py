import re
import os
import argparse

# Renaming all the files with suffix by adding prefix


def get_arguments():
    """Returns prefix and suffix (both can be set using regexp)"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix", type=str, help="new file prefix", required=True)
    parser.add_argument("-s", "--suffix", type=str, help="current filename ending", default="")
    parser.add_argument("-root", "--root", type=str, help="root directory", default="./")
    parser.add_argument("-i", "--insensitive", action="store_true", default=False)

    args = parser.parse_args()

    return args.prefix, args.suffix, args.insensitive, args.root


def get_and_rename_files(prefix, suffix, case_insensitive, root):
    """Gets all the files and through changes their names"""
    for rootDir, dirs, files in os.walk(root):
        for file in files:
            if re.match(rf".*({suffix})(\..+)*", file, re.IGNORECASE if case_insensitive else 0):
                os.rename(os.path.join(rootDir, file), os.path.join(rootDir, prefix + file))


def main():
    get_and_rename_files(*get_arguments())


if __name__ == "__main__":
    main()