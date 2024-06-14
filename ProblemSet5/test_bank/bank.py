# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Checks if a string starts with Hello, or Starts with an H.

def main():
    userInput = input("Greeting: ")
    reward = value(userInput)
    print(f"$ {reward}")

# returns the required reward based on the greeting
def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__" :
    main()