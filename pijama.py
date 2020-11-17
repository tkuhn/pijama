#!/usr/bin/python3
import os
import tkinter as tk
from functools import partial
from tkinter import messagebox
try:
	from picamera import PiCamera
	camera = PiCamera()
except:
	print("no picamera")
from time import sleep
import webbrowser

root = tk.Tk()
root.geometry("800x440")
root.configure(bg="white")

def chosen(d):
  runfile = os.path.join(d, 'run.py')
  if (os.path.isfile(runfile)):
    exec(open(runfile).read())

def photoCallBack():
   camera.start_preview()
   sleep(5)
   camera.stop_preview()

col = 0
row = 0
for d in sorted([n for n in os.listdir('menu') if os.path.isdir(os.path.join('menu', n))]):
  chosenDir = os.path.join('menu', d)
  button = tk.Button(root, text=d, command=partial(chosen, chosenDir), height=7, width=13, borderwidth=0,
      bg="#88f", activebackground="#bbf").grid(row=row, column=col, padx=5, pady=5)
  col = col + 1
  if (col == 5):
    row = row + 1
    col = 0

#for row in range(0, 4):
#  button = tk.Button(root, text="Hello", command=helloCallBack, height=7, width=13, borderwidth=0, bg="#f88", activebackground="#f88").grid(row=row, column=0, padx=5, pady=5)
#  #button.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
#  photoButton = tk.Button(root, text="Photo", command=photoCallBack, height=7, width=13, borderwidth=0).grid(row=row, column=1, padx=5, pady=5)
#  #photoButton.pack(padx=20, pady=20, side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
#
#  button = tk.Button(root, text="Hello", command=helloCallBack, height=7, width=13, borderwidth=0, bg="#8f8", activebackground="#8f8").grid(row=row, column=2, padx=5, pady=5)
#  button = tk.Button(root, text="Hello", command=helloCallBack, height=7, width=13, borderwidth=0, bg="#f88", activebackground="#f88").grid(row=row, column=3, padx=5, pady=5)
#  button = tk.Button(root, text="Hello", command=helloCallBack, height=7, width=13, borderwidth=0, bg="#f88", activebackground="#f88").grid(row=row, column=4, padx=5, pady=5)

root.mainloop()
