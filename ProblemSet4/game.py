# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# Chooses a number between 1 and user input, the user then guesses the number


import random

def main():
    level = valid_int("Level: ")
    if level == 1:
        rand_num = 1
    else:
        rand_num = random.randrange(1, level, 1)
    play_game(rand_num)
    
    
def play_game(rand_num):
    guess = 0
    while guess != rand_num:
        guess = valid_int("Guess: ")
        if guess < rand_num:
            print("Too small!")
        elif guess > rand_num:
            print("Too large!")
    print("Just right!")

def valid_int(prompt):
    while True:
        try:
            user_input =  int(input(prompt))
            if user_input < 1:
                continue
            else:
                return user_input            
        except ValueError:
            continue

if __name__ == "__main__":
    main()