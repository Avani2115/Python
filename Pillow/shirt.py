import sys
from PIL import Image,ImageOps
import os

def main():
    checkerror_len()
    checkerror_num()
    checkerror_ext()
    i, o = sys.argv[1], sys.argv[2]
    try:
        with Image.open(i) as img:
            shirt = Image.open("shirt.png")
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, shirt)
            img.save(o)

    except FileNotFoundError:
        sys.exit("Input does not exist")

def checkerror_len():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def checkerror_num():
    if not sys.argv[1].lower().endswith((".png",".jpg",".jpeg")):
        sys.exit("Invalid input")
    elif not sys.argv[2].lower().endswith((".png",".jpg",".jpeg")):
        sys.exit("Invalid output")

def checkerror_ext():
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()

