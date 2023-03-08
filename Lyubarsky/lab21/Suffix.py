import os
import argparse
import sys

def getParameters():
    parser = argparse.ArgumentParser(
        description="This command writes the names and sizes of all executable files to the specified file.")
    parser.add_argument('-s',
                        type=str,
                        default=' ',
                        help="Write only files with the given STR suffix. Disabled by default.")
    parser.add_argument('-n',
                        type=int,
                        default=1024,
                        help="Write to a file, the size of which must not exceed NUM bytes. The default value is 1024 bytes.")
    parser.add_argument('-d',
                        type=str,
                        default=os.getcwd(),
                        help="Search in the DIR directory. By default, the search occurs in the current directory.")
    parser.add_argument('-f',
                        type=str,
                        default='Output_file',
                        help="Write to FIL file. By default, the recording goes to the Output_file.")
    args = parser.parse_args()
    return args.s, args.n, args.d, args.f


def file_analysis(_suffix: int, _directory: str, _file: str):
    olddir = os.getcwd()
    for root, dirs, files in os.walk(_directory):
        os.chdir(root)
        for file in files:
            if os.access(file, os.X_OK):
                if (file[-len(_suffix):] == _suffix  or _suffix == ' '):
                    size = os.stat(file).st_size
                    os.chdir(olddir)
                    outputFile = open(_file, 'a+')
                    outputFile.write('Размер: '+str(size)+'b Название: '+file+'\n')
                    outputFile.close()
                    os.chdir(root)



s, n, d, f = getParameters() #Letters stands for name of each parameter
startFile = open(f, "a+")
startFile.close()
if (os.stat(f).st_size > n):
    print("Заданный файл слишком большой!")
    sys.exit()
file_analysis(s, d, f)