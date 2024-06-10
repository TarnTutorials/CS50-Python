# CS50P - Problem set 1 - 2022 course
# Tarn Montgomery 2024/06/05
# Returns what meal time it is. Breakfast, Lunch or Dinner

def main():
    timeInput = input("Please enter the time. \n").lower().strip()
    mealTime = convert(timeInput)
    if mealTime >= 7 and mealTime < 8:
        print("breakfast time")
    elif mealTime >= 12 and mealTime < 13:
        print("lunch time")
    elif mealTime >= 18 and mealTime < 19:
        print("dinner time")
    else:
        return

#Converts the time into a floating point number
def convert(timeInput):
    timeFormat = timeInput.split(":")
    hours = float(timeFormat[0])
    minutes = timeFormat[1]
    #Checks if there is a pm/am format 
    if "p" in minutes:
        minutes = minutes.split("p")[0].strip()
        minutes = float(minutes)
        if hours != 12:
            hours = hours + 12.0
    elif "a" in minutes:
        minutes = minutes.split("a")[0].strip()
        minutes = float(minutes)
        if hours == 12:
            hours = hours - 12
    else:
        minutes = float(minutes)
    minutes = minutes/60
    time = hours + minutes
    return time

if __name__ == "__main__" :
    main()