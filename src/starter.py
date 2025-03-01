# starter.py

from PIL import Image
import sys
import numpy as np
import matplotlib.pyplot as plt

image_name = sys.argv[1]
img = Image.open(image_name)

width, height = img.size
rgb_img = img.convert('RGB')
r = []
g = []
b = []
for y in range(height):
    for x in range(width):
        r_i, g_i, b_i = rgb_img.getpixel((x, y))
        print('[', x, ', ', y, '] :: ', 'R: ', r_i, ' G: ', g_i, ' B: ', b_i)
        r.append(r_i)
        g.append(g_i)
        b.append(b_i)

fig = plt.figure()

#syntax for 3-D projection
ax = plt.axes(projection ='3d')

x = np.array(r)
y = np.array(g)
z = np.array(b)
C = np.transpose([x])

ax.scatter(r, g, b, c=np.transpose([x/255,y/255,z/255]))
ax.set_title ('3d Scatter plot for RGB values')
plt.show()