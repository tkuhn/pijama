#!/usr/bin/python3
import os
import tkinter as tk
from functools import partial
from tkinter import *

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

root = tk.Tk()
root.geometry("800x440")
root.configure(bg="white")
frame = Frame(root, bg="white")
frame.pack(fill='both')

images = {}
pixelimgfile = os.path.join(dname, 'aux/pixel.png')
images[pixelimgfile] = PhotoImage(file=pixelimgfile)

def chosen(d):
  prunfile = os.path.join(d, 'run.py')
  srunfile = os.path.join(d, 'run.sh')
  if (os.path.isfile(prunfile)):
    exec(open(prunfile).read())
  if (os.path.isfile(srunfile)):
    os.system(srunfile)
  else:
    clear()
    show(d)
def clear():
  for child in frame.winfo_children():
    child.destroy()

def show(path):
  if (path == 'menu'):
    button = tk.Button(frame, text="EXIT", image=images[pixelimgfile], compound="c", command=exit, height=120, width=120, borderwidth=0,
          bg="#88f", activebackground="#bbf").grid(row=0, column=0, padx=5, pady=5)
  else:
    button = tk.Button(frame, text="<", image=images[pixelimgfile], compound="c", command=partial(show, os.path.dirname(path)), height=120, width=120, borderwidth=0,
          bg="#88f", activebackground="#bbf").grid(row=0, column=0, padx=5, pady=5)
  col = 1
  row = 0
  for d in sorted([n for n in os.listdir(path) if os.path.isdir(os.path.join(path, n))]):
    chosenDir = os.path.join(path, d)
    button = tk.Button(frame, text=d, image=images[pixelimgfile], compound="c", command=partial(chosen, chosenDir), height=120, width=120, borderwidth=0,
        bg="#88f", activebackground="#bbf")
    imgfile = os.path.join(chosenDir, 'img.png')
    if (os.path.isfile(imgfile)):
        images[imgfile] = PhotoImage(file=imgfile)
        button = tk.Button(frame, text="xxx", image=images[imgfile], command=partial(chosen, chosenDir), height=120, width=120, borderwidth=0,
            bg="#88f", activebackground="#bbf")
    button.grid(row=row, column=col, padx=5, pady=5)
    col = col + 1
    if (col == 5):
      row = row + 1
      col = 0

show('menu')

root.mainloop()
