# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# Asks basic math questions, similar to the Little Professor calculator


import random

def main():
    level = get_level()
    final_score = play_game(level)
    print(f"Score: {final_score}")

#Default gameplay loop
def play_game(level):
    score = 0
    num_of_questions = 0
    while num_of_questions < 10:
        x = generate_int(level)
        y = generate_int(level)
        score += guess_answer(x, y)
        num_of_questions += 1
    return score
    
#Plays a single round for 1 question        
def guess_answer(x, y):
    guesses = 0
    z = x + y
    while guesses < 3:
        print(f"{x} + {y} = ", end="")
        try:
            guess = int(input())
            if guess == z:
                return 1
            else:
                print("EEE")
                guesses += 1
        except ValueError:
            print("EEE")
            guesses += 1
    print(f"{x} + {y} = {z}")
    return 0
            
#Generates random numbers for values based on the level
def generate_int(digits):
    match digits:
        case 1:
            x = random.randint(0,9)
            return x
        case 2:
            x = random.randint(10,99)
            return x
        case 3:
            x = random.randint(100,999)
            return x
#Gets the valid input for level, [1, 2, 3]
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in (1, 2, 3):
                raise ValueError
        except ValueError:
            pass
        else:
            return level   
        
if __name__ == "__main__":
    main()