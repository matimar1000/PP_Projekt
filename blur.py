import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

def konwolucja_RGB (zdjecie, blu):
    zdjecie2 = np.empty_like(zdjecie)
    for dim in range(zdjecie.shape[-1]):
        zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim],blu, mode="same", boundary="symm")
    return zdjecie2

plt.rcParams["figure.figsize"]=(11, 7)

nazwa_zd = "pies.jpg"

dane = plt.imread(nazwa_zd)
x = [[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144],[1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144,1/144]]
blur = {"Blur 12x12": np.array(x)}

blur_nazwa = "Blur 12x12"
b = blur[blur_nazwa]

zaladuj = plt.imread(nazwa_zd).astype(np.float)/255.
zaladuj_filtr = konwolucja_RGB(zaladuj, b)

fig, (axL, axR) = plt.subplots(ncols = 2, tight_layout = True)
fig.suptitle(blur_nazwa)

axL.imshow(zaladuj)
axR.imshow(zaladuj_filtr)

plt.show()