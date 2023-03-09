import argparse
import filecmp
import os


def getArgs():
    parser = argparse.ArgumentParser()  
    parser.add_argument("-f", "--inputFileName", type=str, help='input file name', required=True)
    parser.add_argument("-suf", "--suffix", type=str, help='End of file name', required=True)

    args = parser.parse_args()

    return args.suffix, args.inputFileName


def checkSuffix(suffix, inputFileName):
    suffixLength = len(suffix)
    baseFileName = inputFileName.split('.')[0]
    beginOfCut = len(baseFileName) - suffixLength
    endOfCut = len(baseFileName)

    if suffix == baseFileName[beginOfCut:endOfCut]:
        return True

    return False


def checkFileExsist(inputFileName):
    return os.path.isfile(inputFileName)


def deleteMatchingFiles(suffix, inputFileName):
    lisOfFiles = os.listdir()

    for file in lisOfFiles:
        if checkFileExsist(file) and file != inputFileName:
            if checkSuffix(suffix, inputFileName) and filecmp.cmp(file, inputFileName, shallow=True):
                os.remove(file)


def main():
    suffix, inputFileName = getArgs()

    if not checkFileExsist(inputFileName):
        return print("File not found!")

    if not checkSuffix(suffix, inputFileName):
        return print("File's suffix doesn't match entered suffix")

    deleteMatchingFiles(suffix, inputFileName)


if __name__ == "__main__":
    main()
