#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x440")
root.configure(bg="white")

label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

button = tk.Button(root, text="Hello", command=helloCallBack)
button.pack()

root.mainloop()
