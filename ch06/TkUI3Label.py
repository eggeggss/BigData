#!/usr/bin/python
try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
win = tk.Tk()
# Python 2.x name # Python 3.x name
#win = tk.Tk()
'''
label1 =tk.Label(win,text="Hello World!")
label1.pack()
label2 =tk.Label(win,bg="yellow",text="Hello No2!",fg="red")
label2.pack()
label3 =tk.Label(win,text="Hello No3!")
label3.pack(side="top", anchor="w" )
'''
label4 =tk.Label(win,text="Hello No4!")
label4.place(x=120, y=160)

label6=tk.Label(win,text="roger")
label6.grid(row=0 , column=1,padx=2,pady=2)

label7=tk.Label(win,text="roger2")
label7.grid(row=0 , column=0,padx=200,pady=2)
'''
label5 =tk.Label(win,text="Powen Ko",bg="#ff0000")
label5.place(x=120, y=140)
'''

win.mainloop()