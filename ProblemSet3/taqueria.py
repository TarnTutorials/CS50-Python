# CS50P - Problem set 3 - 2022 course
# Tarn Montgomery 2024/06/07
# Orders off a menu and increments price

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    add_item()
    

def add_item():
    total_cost = 0
    while True:
        try:
            item = input("Item: ").title().strip()
            if item in menu:
                total_cost += menu[item]
                total_formatted = "{:.2f}".format(total_cost)
                print(f"Total: ${total_formatted}")
        except EOFError:
            print("")
            break
        except KeyboardInterrupt:
            print("")
            break

if __name__ == "__main__" :
    main()
    