# CS50P - Problem set 6 - 2022 course
# Tarn Montgomery 2024/06/17
# Counts the number of lines in a python file

import sys

def main():
    file = get_file()
    lines = check_lines(file)
    print(len(lines))

#Checks if each line is a comment, or blank
def check_lines(file):
    lines = []
    for line in file:
        if line.strip() == "" or line.strip().startswith("#"):
            continue
        else:
            lines.append(line.strip())
    return lines
        
def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:].lower() != ".py":
        sys.exit("Not a Python file")
    else:
        try:
            return open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")
     
if __name__ == "__main__":
    main()