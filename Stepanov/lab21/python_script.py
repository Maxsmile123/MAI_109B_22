import argparse
import os


def parser_get_arguments():
    parser = argparse.ArgumentParser(
        description = "this script implements a replacement \
        for all files in the \
        directory with a size less than\
        the specified postfix\
        by the first character \
        of the file name"
     )
    parser.add_argument(
        "-s",
        "--size",
        required = True,
        type = int,
        action = "store",
        help = "max size of files \
        in current directory\
        to consider them \
        suitable",
     )
    parser.add_argument(
        "-rp",
        "--relative_path",
        required = True,
        type = str,
        action = "store",
        help = "path to the directory,\
        where user want to\
        use this python script",
     )
    args = parser.parse_args()
    return args.size, args.relative_path


def name_changer(maximum_size_for_find : int, path: str):
    for path, dirs, files in os.walk(path):
        for file in files:
            relative_path = os.path.join(path, file)
            filesize = os.path.getsize(relative_path)
            if maximum_size_for_find >= filesize:
                file_prefix = file[: file.find(".") + 1]
                file_first_char = file[0]
                new_file = os.path.join(path, file_prefix + file_first_char)
                os.rename(relative_path, new_file)


def main():
    size, relative_path = parser_get_arguments()
    name_changer(size, relative_path)
    print("Done")


if __name__ == "__main__":
    main()
