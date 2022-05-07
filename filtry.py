import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation
from tkinter import *

def identiti(zdj):
    return zdj
def lustropoziom(zaladuj):
    shape = zaladuj.shape

    output = np.empty_like(zaladuj)

    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            rgb =  zaladuj[i][j]
            output[shape[0] - i - 1][j] = rgb

    return output

def lustropion(zaladuj):
    shape = zaladuj.shape

    output = np.empty_like(zaladuj)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            rgb = zaladuj[i][j]
            output[i][shape[1] - j - 1] = rgb

    return output

def revers(zaladuj):
    print(zaladuj.shape)

    shape = zaladuj.shape

    output = np.empty_like(zaladuj)

    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            rgb = zaladuj[i][j]
            output[i][j] = [1 - rgb[0], 1 - rgb[1], 1 - rgb[2]]

    return output

def blur(zaladuj):
    def konwolucja_RGB(zdjecie, blu):
        zdjecie2 = np.empty_like(zdjecie)
        for dim in range(zdjecie.shape[-1]):
            zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim], blu, mode="same", boundary="symm")
        return zdjecie2

    x = [[1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144],
         [1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144, 1 / 144]]
    blur = {"Blur 12x12": np.array(x)}

    blur_nazwa = "Blur 12x12"
    b = blur[blur_nazwa]

    zaladuj_filtr = konwolucja_RGB(zaladuj, b)
    return zaladuj_filtr

def krawedzie(zaladuj):
    def konwolucja_RGB(zdjecie, kra):
        zdjecie2 = np.empty_like(zdjecie)
        for dim in range(zdjecie.shape[-1]):
            zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim], kra, mode="same", boundary="symm")
        return zdjecie2

    krawedzie = {"Krawędź 3x3": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])}

    krawedzie_nazwa = "Krawędź 3x3"
    k = krawedzie[krawedzie_nazwa]

    zaladuj_filtr = konwolucja_RGB(zaladuj, k)
    return zaladuj_filtr

def cb(zaladuj):
    shape = zaladuj.shape

    output = np.empty_like(zaladuj)

    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            rgb = zaladuj[i][j]
            avg = (rgb[0] + rgb[1] + rgb[2]) / 3
            output[i][j] = [avg, avg, avg]

    return output

def ostrosc(zaladuj):
    def konwolucja_RGB(zdjecie, kra):
        zdjecie2 = np.empty_like(zdjecie)
        for dim in range(zdjecie.shape[-1]):
            zdjecie2[:, :, dim] = sp.signal.convolve2d(zdjecie[:, :, dim], kra, mode="same", boundary="symm")
        return zdjecie2

    krawedzie = {"Krawędź 3x3": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])}

    krawedzie_nazwa = "Krawędź 3x3"
    k = krawedzie[krawedzie_nazwa]

    zaladuj_filtr = konwolucja_RGB(zaladuj, k)

    return zaladuj_filtr