import tkinter as tk
from tkinter import Button, Entry, filedialog, Text
import os
from  trilat import trilat
import matplotlib.pyplot as plt
from matplotlib.patches import Circle 

from trilat import *
from geo import *
#import geopy.distance



root = tk.Tk()


root.geometry('500x500')
root.title('Positioning system')


x1 = Entry(root, width= 10, bg='black', fg='white')
#x1.pack()
x1.grid(row=2, column=0)

x2 = Entry(root, width= 10, bg='black', fg='white',)
#x2.pack()
x2.grid(row=3, column=0  )


x3 = Entry(root, width= 10, bg='black', fg='white',)
#x3.pack()
x3.grid(row=4, column=0)


y1 = Entry(root, width= 10, bg='black', fg='white',)
y1.grid(row=2, column=1  )

#y1.pack()

y2 = Entry(root, width= 10, bg='black', fg='white',)
y2.grid(row=3, column=1 )
#y2.pack()

y3 = Entry(root, width= 10, bg='black', fg='white',)
y3.grid(row=4, column=1  )
#y3.pack()




gx1 = Entry(root, width= 10, bg='black', fg='white')
#x1.pack()
gx1.grid(row=2, column=3)

gx2 = Entry(root, width= 10, bg='black', fg='white',)
#x2.pack()
gx2.grid(row=3, column=3  )

gx3 = Entry(root, width= 10, bg='black', fg='white',)
#x3.pack()
gx3.grid(row=4, column=3)


gy1 = Entry(root, width= 10, bg='black', fg='white',)
gy1.grid(row=2, column=4  )

#y1.pack()

gy2 = Entry(root, width= 10, bg='black', fg='white',)
gy2.grid(row=3, column=4 )
#y2.pack()

gy3 = Entry(root, width= 10, bg='black', fg='white',)
gy3.grid(row=4, column=4  )
#y3.pack()

gxb = Entry(root, width= 10, bg='green', fg='white',)
#x3.pack()
gxb.grid(row=3, column=5)


gyb = Entry(root, width= 10, bg='green', fg='white',)
gyb.grid(row=3, column=6  )

#y1.pack()



def tri(): 
    xa = float(x1.get())
    xb = float(x2.get())
    xc = float(x3.get())
    ya = float(y1.get())
    yb = float(y2.get())
    yc = float(y3.get())
    A, B =trilat(xa, ya, xb, yb, xc, yc)

    plt.plot([xa, xb, xc], [ya, yb, yc], 'bo')
    plt.plot(A ,B, 'ro')

    r1 = float(D1[4])
    r2 = float(D2[4])
    r3 = float(D3[4])

    range1 = Circle((xa, ya), r1, fill = False)
    range2 = Circle((xb, yb), r2, fill = False)
    range3 = Circle((xc, yc), r3, fill = False)
    
    plt.gca().add_patch(range1)
    plt.gca().add_patch(range2)
    plt.gca().add_patch(range3)


    plt.show()

    #plt.plot(ans, 'go')
    print(A, B)
    return A, B 

def geolook():
    lona = float(gx1.get())
    lonb = float(gx2.get())
    lonc = float(gx3.get())
    lata = float(gy1.get())
    latb = float(gy2.get())
    latc = float(gy3.get())

    baselon = float(gxb.get())
    baselat = float(gyb.get())

    xa, ya = geo2cart(lata, lona, baselon, baselat)
    xb , yb = geo2cart(latb, lonb, baselon ,baselat)
    xc, yc = geo2cart(latc, lonc, baselon, baselat)

    plt.plot([xa, xb, xc], [ya, yb, yc], 'bo')

    A, B = trilat(xa, ya, xb, yb, xc, yc)

    plt.plot([xa, xb, xc], [ya, yb, yc], 'bo')
    plt.plot([A, B, 'ro'])
    plt.show()

    return A, B

    




start = Button(root, text='Start', command= tri, bg='black', fg='white', )
start.grid(row=5, column=0)

Convert_to_local =Button(root, text='Convet_to_local', command= geolook, bg = 'green', fg = 'black')
Convert_to_local.grid(row=5, column=5 )

root.mainloop()