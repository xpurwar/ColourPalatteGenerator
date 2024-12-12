import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3, seed=8.90)
xpix, ypix = 150, 150
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
t3_genres = ["fantasy", "science fiction", "mystery"]
genre_colour_map = {'fantasy':'blueviolet',
'science fiction':'cadetblue',
'action/adventure':'powderblue',
'horror/thriller':'greenyellow',
'mystery':'salmon',
'nonfiction':'bisque',
'other':'salmon',
'romance':'pink'}
t3_colours = []
for genre in t3_genres:
    t3_colours.append(genre_colour_map[genre])


my_cmap = ListedColormap(t3_colours)
plt.imshow(pic, cmap = my_cmap)
font1 = {'family':'serif','color':'black','size':18}
plt.title("Goodreads aura :0", fontdict = font1)
plt.show()