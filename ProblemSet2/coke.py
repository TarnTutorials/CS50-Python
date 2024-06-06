# CS50P - Problem set 2 - 2022 course
# Tarn Montgomery 2024/06/06
# Basic vending machine - inputs money to a limit

def main():
    amount_due = 50
    insert_coins(amount_due)

#Recusive function, input money until amount required is reached.
def insert_coins(amount_due):
    print("Amount Due:", amount_due)
    amount = int(input("Insert a coin: "))
    if amount == 50 or amount == 25 or amount == 10 or amount == 5:
        amount_due -= amount
        if amount_due <= 0:
            return_change = 0 - amount_due
            print("Change Owed: ", return_change)
            return
    insert_coins(amount_due)

main()