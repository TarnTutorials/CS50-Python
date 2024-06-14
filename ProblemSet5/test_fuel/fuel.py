# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Prints the % remaining in the fuel tank given a fraction.


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    final = gauge(percentage)
    print(final) 


def convert(fraction):
    test = fraction.split('/')
    if len(test) == 2:
        try:
            x = int(test[0])
            y = int(test[1])
            if y == 0:
                raise ZeroDivisionError
            elif x <= y:
                try:
                    return int((x/y)*100)
                except ZeroDivisionError:
                    raise 
        except ValueError:
            raise 


def gauge(percentage):
    try:
        percentage = int(percentage)
    except ValueError:
        raise ValueError
    if percentage < 2:
            return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()