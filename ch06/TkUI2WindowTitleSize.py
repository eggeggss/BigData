#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk 
win = tk.Tk()
# Python 2.x name # Python 3.x name
win.wm_title("Hello, Powenko")
win.minsize(width=200, height=200)
win.maxsize(width=800, height=800)
win.resizable(width=True, height=True)
win.mainloop()
