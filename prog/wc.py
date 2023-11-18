import argparse
import sys
import os


def wc(fileName):
    lines = 0
    words = 0
    characters = 0
    fileNames = fileName

    with open(fileName, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters, fileNames


# def wc_stdin(file):
#     lines = 0
#     words = 0
#     characters = 0
#     for line in file:
#             lines += 1
#             words += len(line.split())
#             characters += len(line)
#     return lines, words, characters

def main():
    parser = argparse.ArgumentParser(prog="wc",
        description="Counts words, lines and characters of input files.")
    parser.add_argument("allFiles", type=str, nargs="*",
                        help="Takes file path to be processed")
    parser.add_argument("-c", "--characters", action="store_true",
                        help="Only counts number of characters")
    parser.add_argument("-w", "--words", action="store_true",
                        help="Print the word counts.")
    parser.add_argument("-l", "--lines", action="store_true",
                        help="Print the line counts.")

    args = parser.parse_args()

    totalLines = 0
    totalWords = 0
    totalCharacters = 0

    for file in args.allFiles:
        try:
            if not os.path.isfile(file):
                raise ValueError(f"'{file}' File not found")

            else:
                if not any([args.characters, args.words, args.lines]):
                    args.characters = args.words = args.lines = True

                lines, words, characters, fileNames = wc(file)

                totalLines += lines
                totalWords += words
                totalCharacters += characters

                if args.lines:
                    print(f" {lines}", end="")
                if args.words:
                    print(f" {words}", end="")
                if args.characters:
                    print(f" {characters}", end="")
                if True:
                    print(f" {fileNames}")
        except Exception as e:
            print(e)
            sys.exit(1)

    if len(args.allFiles) > 1:
            if args.lines:
                print(f" {totalLines}", end="")
            if args.words:
                print(f" {totalWords}", end="")
            if args.characters:
                print(f" {totalCharacters} total")
        
    sys.exit(0)

if __name__ == "__main__":
    main()
