# CS50P - Problem set 7 - 2022 course
# Tarn Montgomery 2024/06/20
# Checks if an IP address is valid using regex

import re

def main():
    print(validate(input("IPv4 Address: ")))

# Input: String, Output: True/False
# Uses regex to determine string format, then splits the string and checks each number
def validate(ip):
    valid_format=re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)
    if valid_format == None:
        return False
    else:
        try:
            numbers = ip.split(".")
            for number in numbers:
                if 0 < int(number) > 255:
                    return False
            return True                    
        except TypeError:
            return False
    

if __name__ == "__main__":
    main()