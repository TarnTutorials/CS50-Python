# CS50P - Problem set 0 - 2022 course
# Tarn Montgomery 2024/06/05

# Calculates a tip, based on user input

def main():
    #takes users input for cost of meal and tip %
    mealCost = dollarsToFloat(input("How much was your meal? \n"))
    tipPercent = percentToFloat(input("what percentage tip would you like to give? \n"))
    tip = mealCost * tipPercent
    print(f"Leave a ${tip:.2f} tip!")

def dollarsToFloat(dollars):
    #function to convert dollars string to float
    dollars = float(dollars.replace("$", ""))
    return dollars


def percentToFloat(percent):
    #function to convert percent string to float
    percent = float(percent.replace("%", ""))
    percent = percent/100
    return percent

if __name__ == "__main__" :
    main()