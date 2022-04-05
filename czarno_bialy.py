import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

def konwolucja_RGB (zdjecie, cb):
    zdjecie2 = np.empty_like(zdjecie)
    for dim in range(zdjecie.shape[-1]):
        zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim],cb, mode="same", boundary="symm")
    return zdjecie2

nazwa_zd = "pies3.jpg"

zaladuj = plt.imread(nazwa_zd).astype(float)/255.

print(zaladuj.shape)

shape = zaladuj.shape

output = np.empty_like(zaladuj)

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        rgb =  zaladuj[i][j]
        avg = (rgb[0]+rgb[1]+rgb[2])/3
        output[i][j]=[avg,avg,avg]

fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout = True)
fig.suptitle('czarnobialy')

axL.imshow(zaladuj)
axR.imshow(output)

plt.show()