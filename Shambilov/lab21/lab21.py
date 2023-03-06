import os
import codecs
import argparse

def convert_encoding(path_to_file):
    with codecs.open(path_to_file, 'r', encoding='utf-8') as f:
        content = f.read()
    with codecs.open(path_to_file, 'w', encoding='utf-16') as f:
        f.write(content)

def bypass(dir):
    for root, dirs, files in os.walk(str(dir)):
        for file in files:
            path = os.path.join(root, file)
            if os.path.splitext(path)[1] == '.txt':
                convert_encoding(path)
        for d in dirs:
            bypass(d)

def getdir():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-d', '--dir', type=str, help='Input dir for start')
    args = parser.parse_args()
    return args.dir

def main():
    dir = getdir()
    bypass(dir)

if __name__ == '__main__':
    main()