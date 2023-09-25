from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')


def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)


label = Label(root, font=('arial', 80), background='black', foreground='white')
label.pack(anchor='center')
clock()
mainloop()
