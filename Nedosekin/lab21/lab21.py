import os
import sys
import argparse

def chek_file(filename):
    if not os.path.exists(filename):
        print('File not found')

def generation(filename, num_copies):
    for char in range(1, num_copies + 1):
        new_filename = str(filename) + str(char)
        with open(new_filename, "w") as f:
            pass

def main():
    filename = sys.argv[1]
    num_copies = int(sys.argv[2])
    generation(filename, num_copies)
    chek_file(filename)

if __name__ == "__main__":
    main()

