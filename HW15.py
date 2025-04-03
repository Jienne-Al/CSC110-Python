'''A window opens with a color-filled square inside of it, similar to the dice drawing.
A text box below the square reads “Click anywhere inside the square”.
Anywhere the user clicks, a white dot appears. Subsequently, every time the user
clicks inside the square the old dot disappears and a new dot is drawn. Repeat this pattern
until the user clicks outside the square, at which point the graphics window closes and the program terminates.'''

from graphics import *
win = GraphWin("Canvas", 600, 600)
win.setCoords(0,0,5,5)
win.setBackground("#cf3f3f")

center=Point(2.5,2.5)
center.draw(win)

small_sqrt=Rectangle(Point(1.5,1.5),Point(3.5,3.5))
small_sqrt.setFill("#5edc26")
small_sqrt.draw(win)

txt=Text(Point(2.5,1),"Click anywhere inside the square")
txt.setTextColor("white")
txt.setSize(20)
txt.draw(win)

drawn = False
while True:
    mouse = win.getMouse()
    x = mouse.getX()
    y = mouse.getY()
    if drawn:
        circ.undraw()
    circ = Circle(mouse, 0.2)
    circ.setFill("#ffd966")
    circ.draw(win)
    drawn = True
    if x < 1.5 or x > 3.5 or y < 1.5 or y > 3.5:
        win.close()
        break