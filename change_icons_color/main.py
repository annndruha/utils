import os
import numpy as np
from PIL import Image
FROM_PATH = "icons"
TO_PATH = "icons_out"

with open("from_color.txt") as from_file:
    line = from_file.read()
    R_OLD, G_OLD, B_OLD = map(int, line.split())
    if (type(R_OLD) is not int) or (type(G_OLD) is not int) or (type(B_OLD) is not int):
        raise Exception("Colors in from_color.txt unreadable.\n Change it to 3 int values separated by space")

with open("to_color.txt") as from_file:
    line = from_file.read()
    R_NEW, G_NEW, B_NEW = map(int, line.split())
    if (type(R_NEW) is not int) or (type(G_NEW) is not int) or (type(B_NEW) is not int):
        raise Exception("Colors in to_color.txt unreadable.\n Change it to 3 int values separated by space")
            
if not os.path.exists(FROM_PATH):
    os.makedirs(FROM_PATH)

if not os.path.exists(TO_PATH):
    os.makedirs(TO_PATH)

for root, dirs, files in os.walk(FROM_PATH):
    files = [filename for filename in files if filename.endswith('.png')]
    for filename in files:
        im = Image.open(os.path.join(FROM_PATH, filename))
        pixels = im.load()
        data = np.array(im)

        width, height = im.size
        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if (r, g, b) == (R_OLD, G_OLD, B_OLD):
                    pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)

        im.save(os.path.join(TO_PATH, filename))
