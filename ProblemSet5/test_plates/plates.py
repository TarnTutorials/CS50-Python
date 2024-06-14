# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Checks if a custom license plate is valid


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_length(s):
        if check_start(s):
            if check_numbers(s):
                return True
    return False

def check_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True

def check_start(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def check_numbers(s):
    has_num = False
    for c in s:
        if c.isalpha() and has_num == False:
            has_num = False
        elif c.isnumeric():
            if c == "0" and has_num == False:
                return False
            has_num = True
        else:
            return False
    return True
        
if __name__ == "__main__" :
    main()