from argparse import ArgumentParser
import os

total_lines = 0

def count_lines(file):
    if os.path.isfile(file):
        file_ext = os.path.splitext(file)[1]
        if (file_ext == '.h') or (file_ext == '.cpp'):
            with open(file, 'r') as f:
                lines = len(f.readlines())
                print(f'{file} : {lines}')
                global total_lines
                total_lines += lines

    elif os.path.isdir(file):
        for subfile in os.listdir(file):
            count_lines(os.path.join(file, subfile))

def main():
    parser = ArgumentParser(description='Count lines in *.h and *.cpp files in directory recursively.')
    parser.add_argument('dir', type=str, help='Directory to search files in')
    args = parser.parse_args()

    count_lines(args.dir)
    print(f'Total: {total_lines}')

if __name__ == '__main__':
    main()
