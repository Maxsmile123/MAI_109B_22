import os
import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-f', '--filename', type=str, help='Filename to new files')
    parser.add_argument('-n', '--num_copies', type=int, help='number of copies')
    args = parser.parse_args()
    return str(args.filename), int(args.num_copies)

def check_file(filename):
    try:
        os.path.exists(filename)
    except:
           print('Error:file not found')


def generation(filename, num_copies):
    for i in range(1, num_copies + 1):
        new_filename = filename + str(i)
        with open(new_filename, "w") as f:
            pass

def main():
    filename, num_copies = get_arguments()
    generation(filename, num_copies)
    check_file(filename)

if __name__ == "__main__":
    main()

