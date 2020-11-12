#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
try:
	from picamera import PiCamera
	camera = PiCamera()
except:
	print("no picamera")
from time import sleep

root = tk.Tk()
root.geometry("800x440")
root.configure(bg="white")

label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

button = tk.Button(root, text="Hello", command=helloCallBack)
button.pack()

def photoCallBack():
   camera.start_preview()
   sleep(5)
   camera.stop_preview()

photoButton = tk.Button(root, text="Photo", command=photoCallBack)
photoButton.pack()

root.mainloop()
