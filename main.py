import matplotlib as mpl #popular data visualization library
from matplotlib.colors import LinearSegmentedColormap, ListedColormap # for being able to customize the colours
import matplotlib.pyplot as plt # for plotting the perlin noise
from perlin_noise import PerlinNoise 

'''
Creating a perlin noise object, and then creating a 2d grid of perlin noise objects that we are going to plot later in the tutorial
the octave controls the the detail of the noise, higher the octave, 
the finer the details and the seed is a random pattern. 
Try it yourself: try changing the ocatve and the seed and see how the aura changes!
'''
noise = PerlinNoise(octaves=5, seed=8.90)  
xpix, ypix = 150, 150 #defining the resolution of the grid
# creating the grid
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

'''
From the NLP model, we got the top three genres for your goodreads dataset, and stored it in a list 
called t3_genres. We are now going to map each of those genres to a colour.
Try it yourself: change the colours associaited with each genre to your liking!
'''
t3_genres = ["fantasy", "science fiction", "mystery"] #dummy genres for now
genre_colour_map = {'fantasy':'blueviolet', #mapping each core genre to a colour
'science fiction':'cadetblue',
'action/adventure':'powderblue',
'horror/thriller':'greenyellow',
'mystery':'salmon',
'nonfiction':'bisque',
'other':'salmon',
'romance':'pink'}
t3_colours = []

# creating a map of top 3 colours 
for genre in t3_genres: 
    t3_colours.append(genre_colour_map[genre])

'''
Plotting the perlin noise!
'''
my_cmap = ListedColormap(t3_colours)
plt.imshow(pic, cmap = my_cmap)
font1 = {'family':'serif','color':'black','size':18}
plt.title("Goodreads Aura :0", fontdict = font1)
plt.show()