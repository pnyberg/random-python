from Tkinter import *

class MineArea():
	def __init__(self, x, y, c, number):
		self.x = x
		self.y = y
		self.hidden = True
		self.c = c
		self.number = number

	def paint(self):
		c.create_text(10 + self.x * size, 10 + self.y * size, text=number)

width = 15
height = 12
size = 20
startPosX = 1
startPosY = 1
frameAdjustWidth = 3
frameAdjustHeight = 3

root = Tk()

frame = Frame(root, width=100, height=100)

c = Canvas(frame, bg='white', width = frameAdjustWidth + width * size, height = frameAdjustHeight + height * size)
c.pack()

frame.pack()

rect = [[0 for x in xrange(width)] for x in xrange(height)] 

for n in range (0, height):
	for i in range (0, width):
		rect[n][i] = c.create_rectangle(startPosX + i * size, startPosY + n * size, startPosX + (i + 1) * size, startPosY + (n + 1) * size, fill="gray")

#    print "clicked at", event.x / size, event.y / size
def callback(event):
	frame.focus_set()
	x = event.x / size
	y = event.y / size
	rect[y][x] = c.create_rectangle(startPosX + x * size, startPosY + y * size, startPosX + (x + 1) * size, startPosY + (y + 1) * size, fill="blue")
	mine = MineArea(x, y, c, "1")
	mine.paint()
	print rect[y][x]

c.bind("<Button-1>", callback)

root.mainloop()