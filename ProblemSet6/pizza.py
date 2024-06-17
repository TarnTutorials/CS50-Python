# CS50P - Problem set 6 - 2022 course
# Tarn Montgomery 2024/06/17
# Takes a CSV and makes it into a readable table

import sys
from tabulate import tabulate

def main():
    file = get_file()
    table = make_table(file)
    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))

def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:].lower()  != ".csv":
        sys.exit("Not a CSV file")
    else:
        try:
            return open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")

def make_table(file):
    table = []
    for line in file:
        item = line.strip().split(",")
        table.append(item)
    return table

if __name__ == "__main__":
    main()