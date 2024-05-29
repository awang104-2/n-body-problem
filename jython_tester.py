from processing_py import *

x = 0
y = 0

app = App(600, 400)  # create window: width, height
app.background(0, 0, 0)  # set background:  red, green, blue
app.fill(255, 255, 0)  # set color for objects: red, green, blue
app.rect(x, y, 200, 100)  # draw a rectangle: x0, y0, size_x, size_y
app.fill(0, 0, 255)  # set color for objects: red, green, blue
app.ellipse(300, 200, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y
app.draw()
app.mousePressed()

def mousePressed(self):
    print("mouse pressed")
    self.redraw()
