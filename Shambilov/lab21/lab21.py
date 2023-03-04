import os
import codecs
import argparse

def convert_encoding(file):
    with codecs.open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    with codecs.open(file, 'w', encoding='utf-16') as f:
        f.write(content)
        print("File changed")

def obxod(dir):
    print("Content:", os.listdir(dir))
    for i in os.listdir(dir):
        if os.path.isdir(str(dir) + '\\' + i):
            print("Down", str(dir) + '\\' + i)
            obxod(str(dir) + '\\' + i)
            print("Back to", str(dir))
        if os.path.splitext(str(dir) + '\\' + i)[1] == '.txt':
            assert os.path.isfile(str(dir) + '\\' + i)
            convert_encoding(str(dir) + '\\' + i)

def getargs():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-d', '--dir', type=str, help='Input dir for lab')
    args = parser.parse_args()
    return args.dir

def main():
    dir = getargs()
    obxod(dir)

if __name__ == '__main__':
    main()
    
