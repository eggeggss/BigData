#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk

def event1():
    label1.set("123")
	#print(entry1.get())

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



