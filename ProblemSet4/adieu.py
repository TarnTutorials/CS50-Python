# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# adds commas and "and" to a list in the correct places


import inflect

def main():
    name_list = get_names()
    name_list = inflect.engine().join(name_list)
    print(f"Adieu, adieu, to {name_list}", end="")
    
    
def get_names():
    temp_list = []
    while True:
        try:
            temp_list.append(input().strip())
        except KeyboardInterrupt:
            break
        except EOFError:
            break
    return temp_list

        
    
if __name__ == "__main__":
    main()