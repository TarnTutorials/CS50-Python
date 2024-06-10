# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# Writes Large print text using FIGlet fonts

import sys
import pyfiglet
import random


def main():
    
    font_choice = get_font()
    if font_choice != None:
        convert_text = input()
        result = pyfiglet.figlet_format(convert_text, font = font_choice)
        print(result)
    else:
        sys.exit("Invalid usage")
        
def get_font():
    figfonts = pyfiglet.FigletFont.getFonts()
    if len(sys.argv) == 1:
        return random.choice(figfonts)
    elif len(sys.argv) == 3:
        if sys.argv[2] in figfonts:
            if "-f" in sys.argv[1][0:2]:
                return sys.argv[2]
            elif "--font" in sys.argv[1][0:6]:
                return sys.argv[2]
    return None

if __name__ == "__main__" :
    main()
    