# CS50P - Problem set 6 - 2022 course
# Tarn Montgomery 2024/06/17
# Splits [last, first name] into [first], [last] 

import sys
import csv

def main():
    file = get_file()
    convert_data(file)

def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:].lower() != ".csv":
        sys.exit("Not a CSV file")
    else:
        try:
            return open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")

def convert_data(file):
    with open(sys.argv[2], "w", newline="") as output_file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in file:
            tmp_item = line.replace('"',"").split(",")
            if len(tmp_item) > 2:
                item = {
                    "first" : tmp_item[1].strip(), 
                    "last" : tmp_item[0].strip(), 
                    "house": tmp_item[2].strip()
                }
                writer.writerow(item)

if __name__ == "__main__":
    main()