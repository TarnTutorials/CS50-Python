# CS50P - Problem set 2 - 2022 course
# Tarn Montgomery 2024/06/06
# Checks the nutritional value of a fruit from the FDA

# Define all fruits in dictionary
# Loop through fruits - compare string to input
# Output calories

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew ": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

def main():
    fruit_input = input("Item: ").strip().lower()
    check_fruit(fruit_input)

def check_fruit(fruit):
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    
if __name__ == "__main__" :
    main()