# CS50P - Problem set 2 - 2022 course
# Tarn Montgomery 2024/06/06
# Converts camelCase into snake_case

def main():
    camelCase = input("camelCase: ")
    snake_case = convertCase(camelCase)
    print(snake_case)
    
def convertCase(camelCase):
    result = ""
    for c in camelCase:
        if c.isupper():
            result = result + "_" + c.lower()
        else:
            result += c
    return result

main()
