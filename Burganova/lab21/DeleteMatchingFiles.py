import argparse
import filecmp
import os


def readArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--inputFileName", type=str, help="input file name", required=True
    )
    parser.add_argument(
        "-suf", "--suffix", type=str, help="End of file name", required=True
    )

    args = parser.parse_args()

    return args.suffix, args.inputFileName


def checkSuffix(suffix, inputFileName):
    suffixLength = len(suffix)
    baseFileName = inputFileName.split(".")[0]
    beginOfCut = len(baseFileName) - suffixLength
    endOfCut = len(baseFileName)

    return suffix == baseFileName[beginOfCut:endOfCut]


def checkFileExsist(inputFileName):
    return os.path.isfile(inputFileName)


def checkReadPermission(inputFileName):
    return os.access(inputFileName, os.R_OK)


def deleteMatchingFiles(suffix, inputFileName):
    fileList = os.listdir()

    for file in fileList:
        try:
            if (
                checkFileExsist(file)
                and file != inputFileName
                and checkSuffix(suffix, inputFileName)
                and filecmp.cmp(file, inputFileName, shallow=True)
            ):
                os.remove(file)
        except PermissionError as err:
            print(err)


def main():
    suffix, inputFileName = readArgs()

    if not checkFileExsist(inputFileName):
        raise FileNotFoundError(f'File {inputFileName} not found!')

    if not checkReadPermission(inputFileName):
        raise PermissionError(f'Permission denied for input file: {inputFileName}')
       
    if not checkSuffix(suffix, inputFileName):
        raise Exception("File's suffix doesn't match entered suffix!")

    deleteMatchingFiles(suffix, inputFileName)


if __name__ == "__main__":
    main()
