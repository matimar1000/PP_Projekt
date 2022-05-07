import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
from matplotlib.animation import FuncAnimation
from tkinter import *
from tkinter import filedialog
import filtry

obrazOrg = 0
output = 0
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files", "*.png*"),("all files", "*.*")))
    global obrazOrg
    global output
    obrazOrg = plt.imread(filename).astype(np.float)/255.
    output = plt.imread(filename).astype(np.float)/255.

def zapiszOutput():
    #filename = filedialog.asksavefilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.png*"), ("all files", "*.*")))
    filename = "output.png"
    mpimg.imsave(filename, output)

def pokazOutput():
    fig, (axL, axR) = plt.subplots(ncols=2, tight_layout=True)
    fig.suptitle('oryginal vs po filtrach')
    axL.imshow(obrazOrg)
    axR.imshow(output)
    plt.show()

def blurClick():
    global output
    output = filtry.blur(output)

root = Tk()
root.title('Edytor zdjec')
root.config(background = "white")

widget = Label(root, text='Filtry', fg = "red3").grid(row=0,column=0)

explore_btn = Button(root, text="Browse Files", command=browseFiles).grid(row=2,column=0)


blur_btn = Button(root, text="blur", command = blurClick).grid(row=1,column=0)
lustropo_btn = Button(root, text="lustro poziome").grid(row=1,column=1)
lustropi_btn = Button(root, text="lustro pionowe").grid(row=1,column=2)
revers_btn = Button(root, text="revers").grid(row=1,column=3)
krawedzie_btn = Button(root, text="krawedzie").grid(row=1,column=4)
cb_btn = Button(root, text="czarno-bialy").grid(row=1,column=5)
ostrosc_btn = Button(root, text="ostrosc").grid(row=1,column=6)

pokaz_btn = Button(root, text="pokaz output", command = pokazOutput).grid(row=2,column=1)
pokaz_btn = Button(root, text="zapisz output", command = zapiszOutput).grid(row=2,column=2)

root.mainloop()
