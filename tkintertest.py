#!/usr/bin/python

import Tkinter
import tkMessageBox

# ==
top = Tkinter.Tk()

width = 15
height = 12
size = 20

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "YOLO#SWAG")

def noCallBack():
   tkMessageBox.showinfo( "Pyro", "Turon")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210

rect = [[0 for x in xrange(width)] for x in xrange(height)] 
for n in range (0, height):
	for i in range (0, width):
		rect[n][i] = C.create_rectangle(i * size, n * size, (i + 1) * size, (n + 1) * size, fill="gray")

for n in range (0, height):
	for i in range (0, width):
		print str(n) + "," + str(i) + ": " + str(rect[n][i])
# ==
B.pack()
C.pack()
top.mainloop()

##################