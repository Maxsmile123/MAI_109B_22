import argparse
import os
def Parser_setup():
    parser=argparse.ArgumentParser(description='this script implements a replacement for all files in the directory with a size less than the specified postfix by the first character of the file name');
    parser.add_argument("size",type=int,action='store',help='max size of files in current directory to to consider them suitable');
    args=parser.parse_args();
    return args.size
    
def Name_changer(size,path):
    for paath, dirs, files in os.walk(path):
      for file in files:
        not_an_abs_path = os.path.join(paath, file);
        filesize = os.path.getsize(not_an_abs_path);
        if size >= filesize:
            new_file = os.path.join(paath, file[: file.find(".") + 1] + file[0:1])
            os.rename(not_an_abs_path, new_file)
            
def main():
    size=Parser_setup()
    path="./"
    Name_changer(size,path)
    print("Done")
    
if __name__ == "__main__":
    main()
