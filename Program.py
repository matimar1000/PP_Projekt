import tkinter
import subprocess
root = tkinter.Tk()

def filtr_blur():
    subprocess.call("blur.py", shell=True)
def filtr_czarno_bialy():
    subprocess.call("czarno_bialy.py", shell=True)
def filtr_krawedzie():
    subprocess.call("krawedzie.py", shell=True)
def filtr_lustro():
    subprocess.call("lustro.py", shell=True)
def filtr_ostrosc():
    subprocess.call("ostrosc.py", shell=True)
def filtr_revers():
    subprocess.call("revers.py", shell=True)
blur = tkinter.Button(root, text='blur', command=filtr_blur)
blur.pack()

czarno_bialy = tkinter.Button(root, text='czarno_bialy', command=filtr_czarno_bialy)
czarno_bialy.pack()

krawedzie = tkinter.Button(root, text='krawedzie', command=filtr_krawedzie)
krawedzie.pack()

lustro = tkinter.Button(root, text='lustro', command=filtr_lustro)
lustro.pack()

ostrosc = tkinter.Button(root, text='ostrosc', command=filtr_ostrosc)
ostrosc.pack()

revers = tkinter.Button(root, text='revers', command=filtr_revers)
revers.pack()


root.mainloop()
