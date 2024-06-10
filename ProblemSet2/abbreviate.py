# CS50P - Problem set 2 - 2022 course
# Tarn Montgomery 2024/06/06
# Removes vowels from words to help abbreviate 

def main():
    user_input = input("Input: ")
    abbreviated = abbreviate_string(user_input)
    print("Output: ", abbreviated)

def abbreviate_string(user_input):
    new_string = ""
    for c in user_input:
        if c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u":
            new_string += ""
        else:
            new_string += c
    return new_string
            
if __name__ == "__main__" :
    main()