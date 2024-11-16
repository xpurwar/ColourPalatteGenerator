import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=9)
xpix, ypix = 150, 150
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

plt.imshow(pic, cmap='Paired')
font1 = {'family':'serif','color':'black','size':18}
plt.title("Goodreads aura :0", fontdict = font1)
plt.show()