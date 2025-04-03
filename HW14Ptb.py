'''Draw two different faces of dice in one (1) window. They should be arranged in a row like this (see the sample picture on Wamap):
5, 3
You may pick any two numbers from 1 to 6 that you like. Each face will be square with
the correct number of spots. Google “dice” images to see the correct pattern for each face.
The faces can be perfect squares, you do not need to round the corners. There should be some space between them.
Use colors to set off the spots on each face.'''

from graphics import *

win = GraphWin("My Window", 1000, 500)
win.setBackground("white")
win.setCoords(0, 0, 20, 10)

rec1 = Rectangle(Point(2, 2), Point(8, 8))
rec1.setFill("pink")
rec1.setOutline("black")
rec1.setWidth(1)

rec2 = Rectangle(Point(12, 2), Point(18, 8))
rec2.setFill("#ffd166")
rec2.setOutline("black")
rec2.setWidth(1)

rec1.draw(win)
rec2.draw(win)

dot1 = Circle(Point(7, 7), 0.5)
dot1.setFill("black")
dot1.draw(win)

color=["thistle","papayawhip", "mintcream"]
for a in range(3):
    dot_clone = dot1.clone()
    dot_clone.setFill(color[a])
    dot_clone.move(-a*2,-a *2)
    dot_clone.draw(win)

dot2 = Circle(Point(13.5, 7), 0.5)
dot2.setFill("black")
dot2.draw(win)

colors=["lightgreen", "lightsalmon", "lightblue"]
for b in range(3):
    dot2_clone = dot2.clone()
    dot2_clone.setFill(colors[b])
    dot2_clone.move(0,-b*2)
    dot2_clone.draw(win)

colors1=["lightpink", "lavender", "peachpuff"]
for c in range(3):
    dot3_clone = dot2.clone()
    dot3_clone.setFill(colors[c])
    dot3_clone.move(3,-c*2)
    dot3_clone.draw(win)

win.getMouse()
win.close()
