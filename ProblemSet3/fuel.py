# CS50P - Problem set 2 - 2022 course
# Tarn Montgomery 2024/06/06
# Converts fractions into percentages

def main():
    fraction = get_fraction("Fraction: ")
    calc_percent(fraction)

def calc_percent(fraction):
    x = fraction[0]
    y = fraction[1]
    try:
        percent = int((x/y * 100))
    except ValueError:
        get_fraction("Fraction: ")
    except ZeroDivisionError:
        get_fraction("Fraction: ")
    if percent < 2:
            print("E")
    elif percent > 98:
        print("F")
    else:
        print(f"{percent}%")

def get_fraction(prompt):
    while True:
        test = input(prompt)
        test = test.split('/')
        if len(test) > 2:
            continue
        try:    
            x = int(test[0])
            y = int(test[1]) 
            if x <= y:
                return x, y
        except ValueError:
            pass

main()