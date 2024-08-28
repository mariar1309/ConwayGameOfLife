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