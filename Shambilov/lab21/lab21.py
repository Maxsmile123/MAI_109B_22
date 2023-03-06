import os
import codecs
import argparse

def convert_encoding(path_to_file, source_encoding, target_encoding):
    with codecs.open(path_to_file, 'r', encoding=str(source_encoding)) as f:
        content = f.read()
    with codecs.open(path_to_file, 'w', encoding=str(target_encoding)) as f:
        f.write(content)

def bypass(dir, source_encoding, target_encoding):
    for root, dirs, files in os.walk(str(dir)):
        for file in files:
            path = os.path.join(root, file)
            if os.path.splitext(path)[-1] == '.txt':
                convert_encoding(path, str(source_encoding), str(target_encoding))
        for d in dirs:
            bypass(d, str(source_encoding), str(target_encoding))

def getdir():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-d', '--dir', type=str, help='The directory to start')
    parser.add_argument('-s', '--src', type=str, help='Source encoding')
    parser.add_argument('-t', '--trg', type=str, help='Target encoding')
    args = parser.parse_args()
    return args.dir, args.src, args.trg

def main():
    dir, source_encoding, target_encoding = getdir()
    bypass(dir, source_encoding, target_encoding)

if __name__ == '__main__':
    main()
    
