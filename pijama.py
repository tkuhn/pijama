#!/usr/bin/python3

import os
import subprocess
import tkinter as tk
from functools import partial
from tkinter import *
import tkinter.font as font

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
pixel_img = os.path.join(dname, 'aux/pixel.png')
images[pixel_img] = PhotoImage(file=pixel_img)
exit_img = os.path.join(dname, 'aux/exit.png')
images[exit_img] = PhotoImage(file=exit_img)
back_img = os.path.join(dname, 'aux/back.png')
images[back_img] = PhotoImage(file=back_img)

buttonfont = font.Font(size=20)

def chosen(d):
  srunfile = os.path.join(d, 'run.sh')
  prunfile = os.path.join(d, 'run.py')
  if os.path.isfile(srunfile):
    subprocess.Popen(["bash", srunfile])
  elif os.path.isfile(prunfile):
    subprocess.Popen(["python", prunfile])
  else:
    clear()
    show(d)

def clear():
  for child in frame.winfo_children():
    child.destroy()

def mkbutton(textOrImage, command, bg, row, col):
  abg = bg;
  if bg == "#ee6":
    abg = "#ff8"
  if bg == "#f88":
    abg = "#fbb"
  if bg == "#88f":
    abg = "#bbf"
  if textOrImage in images:
    text = ""
    image = images[textOrImage]
  else:
    text = textOrImage
    image = images[pixel_img]
  button = tk.Button(frame,
      text=text, wraplength=100,
      image=image,
      compound="c",
      command=command,
      height=120, width=120,
      borderwidth=0, highlightthickness=0,
      bg=bg, activebackground=abg,
      padx=0, pady=0
    )
  button['font'] = buttonfont
  button.grid(row=row, column=col, padx=8, pady=8)
  return button

def runnable(dir):
  if os.path.isfile(os.path.join(dir, 'run.py')):
    return True
  if os.path.isfile(os.path.join(dir, 'run.sh')):
    return True
  return False

def show(path):
  clear()
  if path == 'menu':
    button = mkbutton(exit_img, exit, "#f88", 0, 0)
  else:
    button = mkbutton(back_img, partial(show, os.path.dirname(path)), "#f88", 0, 0)
  col = 1
  row = 0
  subdirs = [n for n in os.listdir(path) if os.path.isdir(os.path.join(path, n))]
  for d in sorted(subdirs):
    if d.startswith(".") or d.startswith("__"):
      continue
    chosenDir = os.path.join(path, d)
    if runnable(chosenDir):
      bg_color = "#88f"
    else:
      bg_color = "#ee6"
    img = os.path.join(chosenDir, 'img.png')
    if os.path.isfile(img):
        images[img] = PhotoImage(file=img)
        button = mkbutton(img, partial(chosen, chosenDir), bg_color, row, col)
    else:
        d = re.sub(r'^[0-9]+_', '', d)
        d = re.sub(r'_', ' ', d)
        button = mkbutton(d, partial(chosen, chosenDir), bg_color, row, col)
    col = col + 1
    if col == 5:
      row = row + 1
      col = 0

show('menu')

root.mainloop()
