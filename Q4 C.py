'''The goal is to draw four concentric circles in a target.
See the example on Wamap. Each circle should have half the radius of the circle surrounding it, for example 1 - 1/2 - 1/4 - 1/8.
The circles should be large and easily visible or you will lose points.
Each must be a different color. In the Wamap example I used black-cyan-red-yellow but you are free to choose your own colors.
This is a straightforward graphics problem; there are no tricky for loops or move commands, just four concentric circles.'''

from graphics import *
win = GraphWin("Canvas",600,600)
win.setBackground("white")

center=Point(300,300)
center.draw(win)

circ3=Circle(center,80)
circ3.setFill("green")
circ3.draw(win)

circ2=Circle(center,60)
circ2.setFill("yellow")
circ2.draw(win)

circ1=Circle(center,40)
circ1.setFill("orange")
circ1.draw(win)

circ=Circle(center,20)
circ.setFill("red")
circ.draw(win)
