# CS50P - Problem set 0 - 2022 course
# Tarn Montgomery 2024/06/05

# Changes " " into "..."

userInput = input("Please input a sentence. \n").strip()

userInput = userInput.replace(" ", "...")
print(userInput)