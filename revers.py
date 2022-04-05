import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

nazwa_zd = "pies.jpg"

zaladuj = plt.imread(nazwa_zd).astype(float)/255.

print(zaladuj.shape)

shape = zaladuj.shape

output = np.empty_like(zaladuj)

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        rgb =  zaladuj[i][j]
        output[i][j]=[1 - rgb[0], 1 - rgb[1], 1 - rgb[2]]


fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout = True)
fig.suptitle('czarnobialy')

axL.imshow(zaladuj)
axR.imshow(output)

plt.show()