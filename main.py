'''
numpy for grid array representation
matplotlib to display simulation output
matplotlib animation to update simulation
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Represent the grid. 255 for ON, 0 for OFF
x = np.array(([0, 0, 255], [255, 255, 0], [0, 255, 0]))
plt.imshow(x, interpolation = 'nearest') #'nearst' to get the sharpest edges of cells
plt.show()
print ("done")

#random distribution of cells
np.random.choice([0, 255], 4*4, p=[0.5, 0.5]).reshape(4, 4)

#Instead of random distribution, can set a pattern by initializing 2D grid to zeros and then replacing particular pixels in chosen rows and cols
def addGlider(i, j, grid):
    #add a glider with top left cells at (i, j)
    glider = np.array([[0, 0, 225],[225, 0, 225],[0, 225, 225]])
    grid[i:i+3, j:j+3]=glider
grid = np.zeros(10*10).reshape(10, 10)
addGlider(1, 1, grid)
