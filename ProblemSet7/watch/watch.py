# CS50P - Problem set 7 - 2022 course
# Tarn Montgomery 2024/07/01
# takes strings containing youtube addresses, and converts them into shorter links

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    found = re.search('src="([^"\s]*?)youtube\.com/embed/([^"]+)"', s)
    if found:
        link = "https://youtu.be/" + found.group(2)
        return link
    else:
        return None 


if __name__ == "__main__":
    main()