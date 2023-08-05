# Perform file operations according to input given by user
import sys
from os.path import isfile

def print_lines(line_list: list[str]):
    for i in range(20):
        print(f'{i + 1} : {line_list[i]}')

def count_words(line_list: list[str]):
    word: str = input('Enter a word: ')
    cnt: int = 0
    for line in line_list:
        cnt += line.count(word)
    print(f'The word {word} appears {cnt} times in the file')

def main() -> None:
    fname: str = input("Enter the file name: ")
    if not isfile(fname):
        print(f'File {fname} does not exist')
        sys.exit(0)
    infile = open(fname, 'r')
    line_list: list[str] = infile.readlines()
    print_lines(line_list)
    count_words(line_list)
    infile.close()

if __name__ == '__main__':
    main()
