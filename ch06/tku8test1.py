#!/usr/bin/python
try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
  from tkinter import StringVar

def event1():
    myinput=entry1.get()
    myinput=int(myinput) * 3
    v.set(myinput)

win = tk.Tk()
entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
v = StringVar()
label1 =tk.Label(win,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")
win.mainloop()



