# CS50P - Problem set 1 - 2022 course
# Tarn Montgomery 2024/06/05
# Simple math interpreter

def main():
    mathInput = input("Math Expression: ")
    answer = calculateAnswer(mathInput)
    print(answer)

def calculateAnswer(mathInput):
    equation = mathInput.split(" ")
    x = int(equation[0])
    function = equation[1]
    y = int(equation[2])
    match function:
        case "+":
            return float(x + y)
        case "-":
            return  float(x - y)
        case "x":
            return  float(x * y)
        case "*":
            return  float(x * y)
        case "/":
            return  float(x / y)
        case _:
            return "Invalid input, please use x operator z. 1 + 1"

main()