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
root.title("Pijama")
frame = Frame(root, bg="white")
frame.pack(fill='both')

images = {}
pixelimgfile = os.path.join(dname, 'aux/pixel.png')
images[pixelimgfile] = PhotoImage(file=pixelimgfile)
exitimgfile = os.path.join(dname, 'aux/exit.png')
images[exitimgfile] = PhotoImage(file=exitimgfile)
backimgfile = os.path.join(dname, 'aux/back.png')
images[backimgfile] = PhotoImage(file=backimgfile)

def chosen(d):
  srunfile = os.path.join(d, 'run.sh')
  prunfile = os.path.join(d, 'run.py')
  if (os.path.isfile(srunfile)):
    os.system(srunfile)
  elif (os.path.isfile(prunfile)):
    exec(open(prunfile).read())
  else:
    clear()
    show(d)

def clear():
  for child in frame.winfo_children():
    child.destroy()

def show(path):
  if (path == 'menu'):
    button = tk.Button(frame, text="", image=images[exitimgfile], compound="c", command=exit, height=120, width=120, borderwidth=0, highlightthickness = 0,
          bg="#f88", activebackground="#fbb", padx=0, pady=0).grid(row=0, column=0, padx=8, pady=8)
  else:
    button = tk.Button(frame, text="", image=images[backimgfile], compound="c", command=partial(show, os.path.dirname(path)), height=120, width=120, borderwidth=0, highlightthickness = 0,
          bg="#f88", activebackground="#fbb", padx=0, pady=0).grid(row=0, column=0, padx=8, pady=8)
  col = 1
  row = 0
  for d in sorted([n for n in os.listdir(path) if os.path.isdir(os.path.join(path, n))]):
    chosenDir = os.path.join(path, d)
    bg_color = "#ee6"
    abg_color = "#ff8"
    if (os.path.isfile(os.path.join(chosenDir, 'run.py')) or os.path.isfile(os.path.join(chosenDir, 'run.sh'))):
      bg_color = "#88f"
      abg_color = "#bbf"
    imgfile = os.path.join(chosenDir, 'img.png')
    if (os.path.isfile(imgfile)):
        images[imgfile] = PhotoImage(file=imgfile)
        button = tk.Button(frame, image=images[imgfile], text="", compound="c", command=partial(chosen, chosenDir), height=120, width=120, borderwidth=0, highlightthickness = 0,
            bg=bg_color, activebackground=abg_color, padx=0, pady=0).grid(row=row, column=col, padx=8, pady=8)
    else:
        button = tk.Button(frame, image=images[pixelimgfile], text=d, compound="c", command=partial(chosen, chosenDir), height=120, width=120, borderwidth=0, highlightthickness = 0,
    	    bg=bg_color, activebackground=abg_color, padx=0, pady=0).grid(row=row, column=col, padx=8, pady=8)
    col = col + 1
    if (col == 5):
      row = row + 1
      col = 0

show('menu')

root.mainloop()
