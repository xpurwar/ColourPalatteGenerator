import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3, seed=8.90)
xpix, ypix = 150, 150
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
my_cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
plt.imshow(pic, cmap = my_cmap)
font1 = {'family':'serif','color':'black','size':18}
plt.title("Goodreads aura :0", fontdict = font1)
plt.show()