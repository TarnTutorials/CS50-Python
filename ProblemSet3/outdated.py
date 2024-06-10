# CS50P - Problem set 3 - 2022 course
# Tarn Montgomery 2024/06/06
# Converts dates from MM/DD/YYYY or Month Day, Year format to YYYY-MM-DD

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = convert_date()
    print_date(date)

def convert_date():
    while True:
        s = input("Date: ").strip().title()
        # Checks for the MM/DD/YYYY format
        if "/" in s:
            parts = s.split("/")
            if len(parts) == 3:
                try:
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])
                    if month >= 1 and month <= 12:
                        if day >= 1 and day <= 31:
                            return day, month, year
                except ValueError:
                    continue
        # Checks for the Month Day, Year format
        elif " " in s:
            parts = s.split(" ")
            if(len(parts)) == 3:
                month = parts[0]
                if month in months:
                    month = months.index(parts[0]) + 1
                    if ',' in parts[1]:
                        parts[1] = parts[1].replace(',', "")
                        try:
                            day = int(parts[1])
                            if day >= 1 and day <= 31:
                                try:
                                    year = int(parts[2])
                                    try:
                                        return day, month, year
                                    except NameError:
                                        continue
                                except ValueError:
                                    continue
                        except ValueError:
                            continue

# Prints the [day, month, year] list into the correct order
def print_date(date_list):
    day = date_list[0]
    month = date_list[1]
    year = date_list[2]
    print(f"{year:04}-{month:02}-{day:02}")

if __name__ == "__main__" :
    main()




