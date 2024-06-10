# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# Adds emoji's to a string using the emoji library

import emoji


def main():
    user_input = input("Input: ").strip().lower()
    print(emoji.emojize(f"Output: {user_input}", language="alias"))
    
        
if __name__ == "__main__" :
    main()