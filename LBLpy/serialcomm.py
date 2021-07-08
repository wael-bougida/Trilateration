import tkinter as tk
from tkinter import *
import os
from serial import listen
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


hear = Button(root, text='listen')#, command= listen(a))
hear.pack()


root.mainloop()
