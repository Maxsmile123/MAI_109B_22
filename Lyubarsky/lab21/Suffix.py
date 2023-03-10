import os
import argparse

def getParameters():
    parser = argparse.ArgumentParser(
        description="This command writes the names and sizes of all executable files to the specified file.")
    parser.add_argument('-s',
                        '--suffix',
                        type=str,
                        default=' ',
                        help="Write only files with the given STR suffix. Disabled by default.")
    parser.add_argument('-n',
                        '--number',
                        type=int,
                        default=1024,
                        help="Write to a file, the size of which must not exceed NUM bytes. The default value is 1024 bytes.")
    parser.add_argument('-d',
                        '--directory',
                        type=str,
                        default=os.getcwd(),
                        help="Search in the DIR directory. By default, the search occurs in the current directory.")
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        default='Output_file',
                        help="Write to FIL file. By default, the recording goes to the Output_file.")
    args = parser.parse_args()
    return args.s, args.n, args.d, args.f


def check_output_file(_file: str, _file_size: int, _directory:str):
    _files = os.listdir(_directory[:-len(_file)])
    if _file in _files:
        try:
            if (os.stat(_directory).st_size > _file_size):
                raise Exception("Заданный файл слишком большой!")
        except Exception as _exception:
            print(_exception)
            raise SystemExit


def record_file_with_suffix(_suffix: int, _directory: str, _file: str, _file_size: int):
    _file_path = os.getcwd() + '/' + _file
    check_output_file(_file, _file_size, _file_path)
    os.chdir(_directory)
    for root, dirs, files in os.walk(os.getcwd()):
        os.chdir(root)
        for file in files:
            if os.access(file, os.X_OK):
                _lenght_of_suffix = len(_suffix)
                if (file[-_lenght_of_suffix:] == _suffix  or _suffix == ' '):
                    size = os.stat(file).st_size
                    with open(_file_path, 'a+') as output_File:
                        output_File.write('Размер: '+str(size)+'b Название: '+file+'\n')


def main():
    suffix, file_size, search_directory, output_file = getParameters()

    record_file_with_suffix(suffix, search_directory, output_file, file_size)

if __name__ == '__main__':
    main()