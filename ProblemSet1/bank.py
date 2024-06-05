# CS50P - Problem set 1 - 2022 course
# Tarn Montgomery 2024/06/05
# Checks if a string starts with Hello, or Starts with an H.

def main():
    userInput = input("Greeting: ").lower().strip()
    reward = checkGreeting(userInput)
    print(f"$ {reward}")

# returns the required reward based on the greeting
def checkGreeting(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

main()