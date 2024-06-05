# CS50P - Problem set 0 - 2022 course
# Tarn Montgomery 2024/06/05
# Changes :) or :( into an emoticon
def main():
    userInput = input("Enter an input that has :) or :( in it. \n")
    convertedInput = convert(userInput)
    print(convertedInput)

def convert(inputString):
    inputString = inputString.replace(":)", "🙂")
    inputString = inputString.replace(":(", "🙁")
    return inputString

main()