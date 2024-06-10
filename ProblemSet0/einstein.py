# CS50P - Problem set 0 - 2022 course
# Tarn Montgomery 2024/06/05
# Converts mass into Energy using E=mc^2
def main():
    userInput = int(input("What is the mass in kilograms you wish to convert? \n"))
    convertedEnergy = convertToEnergy(userInput)
    print(convertedEnergy)
    
def convertToEnergy(mass):
    c = 300000000
    energy = mass*(pow(c, 2))
    return energy

if __name__ == "__main__" :
    main()