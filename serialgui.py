
#!usr/bin/python3
import tkinter as tk
from tkinter import *
import os
from main import listen, wake, rs232
#import serial.tools.list_ports

root = tk.Tk()
root.geometry('500x500')
root.title('serial communication')


port1 = Entry(root, width= 10, bg='black', fg='white')
port1.pack()

a = str(port1.get())


# ports = serial.tools.list_ports.comports()
# default =StringVar(root, 'Please select port')
# OptionMenu(root, default, *ports).pack()



def li():
    listen(str(a))

def wa():
    wake(str(a))

def tes():
    rs232(str(a))





hear = Button(root, text='listen', command= li)
hear.pack()
awake = Button(root, text='wake', command = wa)
awake.pack()
test = Button(root, text = 'Test connection', command = tes)
test.pack()
Button(root, text='exit', command = lambda : root.destroy()).pack()



root.mainloop()
