import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

def konwolucja_RGB (zdjecie, kra):
    zdjecie2 = np.empty_like(zdjecie)
    for dim in range(zdjecie.shape[-1]):
        zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim],kra, mode="same", boundary="symm")
    return zdjecie2

plt.rcParams["figure.figsize"]=(11, 7)

nazwa_zd = "pies2.jpg"

dane = plt.imread(nazwa_zd)

krawedzie = {"Krawędź 3x3": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])}

krawedzie_nazwa = "Krawędź 3x3"
k = krawedzie[krawedzie_nazwa]

zaladuj = plt.imread(nazwa_zd).astype(np.float)/255.
zaladuj_filtr = konwolucja_RGB(zaladuj, k)

fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout = True)
fig.suptitle(krawedzie_nazwa)

axL.imshow(zaladuj)
axR.imshow(zaladuj_filtr)

plt.show()