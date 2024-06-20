# CS50P - Problem set 6 - 2022 course
# Tarn Montgomery 2024/06/20
# Overlays 2 images, to show muppets in a CS50 chirt

import sys
import PIL 
from PIL import Image
import os

valid_ext = [".jpg", ".jpeg", ".png"]
shirt = Image.open("shirt.png")

def main():
    image = get_file()
    export_shirt(image)


def export_shirt(image):
    image.paste(shirt, shirt)
    image.save(sys.argv[2])
    

def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() not in valid_ext:
        sys.exit("Not a valid file")
    elif os.path.splitext(sys.argv[2])[1].lower() not in valid_ext:
        sys.exit("Not a valid file")
    elif os.path.splitext(sys.argv[2])[1].lower() != os.path.splitext(sys.argv[1])[1].lower():
        sys.exit("Import/Export needs to be the same file type")
    else:
        try:
            image = Image.open(sys.argv[1])
            return PIL.ImageOps.fit(image, shirt.size)
        except FileNotFoundError:
            sys.exit("File does not exist")
            
if __name__ == "__main__":
    main()