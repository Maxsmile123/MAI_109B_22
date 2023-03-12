#!/usr/bin/python3

import os
import sys


def help():
    print('usage: ./script --input=[]')
    print('--input - source directory with subdirectories')


def encoding(directory):
    if len(sys.argv) != 2:
        help()
    else:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    print('File encoding:', file_path)
                    with open(file_path, 'r') as f:
                        content = f.read()
                        new_content = content.translate(
                            str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                          'DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc'))
                    with open(file_path, 'w') as f:
                        f.write(content)
                        print('File content:', content)
                    with open(file_path, 'w') as f:
                        f.write(new_content)
                        print('New file content:', new_content)
        print('Done!')


def parse_args():
    for arg in sys.argv[1:]:
        if arg.startswith('--input='):
            flag = arg.split('=')[1]
            encoding(flag)
        elif arg == '--help':
            help()
            sys.exit()
        else:
            print('Unknown parameter:', arg)
            help()
            sys.exit()


if __name__ == '__main__':
    parse_args()
