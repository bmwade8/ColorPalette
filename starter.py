# starter.py

from PIL import Image
import sys

image_name = sys.argv[1]
img = Image.open(image_name)

width, height = img.size
rgb_img = img.convert('RGB')

for y in range(height):
    for x in range(width):
        r, g, b = rgb_img.getpixel((x, y))
        print('[', x, ', ', y, '] :: ', 'R: ', r, ' G: ', g, ' B: ', b)