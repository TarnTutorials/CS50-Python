# CS50P - Problem set 1 - 2022 course
# Tarn Montgomery 2024/06/05
# Answers the meaning of life

def main():
    userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n").lower().strip()
    if userInput == "42" or userInput == "forty two" or userInput == "forty-two":
        print("Yes")
    else:
        print("No")

main()