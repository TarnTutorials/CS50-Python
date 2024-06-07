# CS50P - Problem set 3 - 2022 course
# Tarn Montgomery 2024/06/06
# Creates a grocery list with number of items added

groceries = {}

def main():
    add_items()
    print_groceries()

def add_items():
    while True:
        try:
            item = input("Item: ").upper().strip()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except KeyboardInterrupt:
            break
        except EOFError:
            break

def print_groceries():
    print("")
    sorted_list = sorted(groceries.keys(), key=lambda x:x.lower())
    for i in sorted_list:
        value = groceries[i]
        print(f"{value} {i}")

main()