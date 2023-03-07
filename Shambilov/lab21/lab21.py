import os
import codecs
import argparse

def convert_encoding(path_to_file, source_encoding, target_encoding):
    try:
        with codecs.open(path_to_file, 'r', encoding=source_encoding) as f:
            content = f.read()
    except Exception:
        raise Exception('Incorrect encoding')
    with codecs.open(path_to_file, 'w', encoding=target_encoding) as f:
        f.write(content)

def bypass(dir, source_encoding, target_encoding):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            if os.path.splitext(path)[-1] == '.txt':
                convert_encoding(path, source_encoding, target_encoding)
        for d in dirs:
            bypass(d, source_encoding, target_encoding)

def get_dir_and_encoding():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-d', '--dir', type=str, help='The directory to start')
    parser.add_argument('-s', '--src', type=str, help='Source encoding')
    parser.add_argument('-t', '--trg', type=str, help='Target encoding')
    args = parser.parse_args()
    return args.dir, args.src, args.trg

def main():
    Dir, Source_encoding, Target_encoding = get_dir_and_encoding()
    dir = str(Dir)
    source_encoding = str(Source_encoding)
    target_encoding = str(Target_encoding)
    if os.path.isdir(dir):
        bypass(dir, source_encoding, target_encoding)
    else:
        raise Exception('Incorrect dir')

if __name__ == '__main__':
    main()
    