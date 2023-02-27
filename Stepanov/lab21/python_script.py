import argparse
import os


def parser_get_size():
    parser = argparse.ArgumentParser(
        description = "this script implements a replacement \
        for all files in the \
        directory with a size less than\
        the specified postfix\
        by the first character \
        of the file name"
     )
    parser.add_argument(
        "size",
        type = int,
        action = "store",
        help = "max size of files \
        in current directory\
        to consider them \
        suitable",
     )
    args = parser.parse_args()
    return args.size


def name_changer(size, path):
    for path, dirs, files in os.walk(path):
        for file in files:
            not_an_abs_path = os.path.join(path, file)
            filesize = os.path.getsize(not_an_abs_path)
            if size >= filesize:
                file_preff = file[: file.find(".") + 1]
                file_first_char = file[0:1]
                new_file = os.path.join(path, file_preff + file_first_char)
                os.rename(not_an_abs_path, new_file)


def main():
    size = parser_get_size()
    CONST_PATH = "./"
    name_changer(size, CONST_PATH)
    print("Done")


if __name__ == "__main__":
    main()
