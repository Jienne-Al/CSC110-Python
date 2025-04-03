'''Draw 6 rectangles in a graphics window. Make the rectangles a different color
from the background. The tops of your rectangles should conform to the linear function y=x,
creating a diagonal pattern up-and-to-the-right (see the sample picture on Wamap).
In order to receive full credit you must use a for loop, a clone command,
and a .move(dx,dy) command. Do not simply paste six different rectangles in six different places.'''

from graphics import*
def main():
    win = GraphWin("Canvas", 600,600)
    win.setBackground("Pink")

    rect = Rectangle(Point(600,0),Point(500,100))
    rect.setFill("Yellow")
    rect.setWidth(1)
    rect.draw(win)

    for a in range(6):
        rect2 = rect.clone()
        rect2.move(-a*100,a*100)
        rect2.draw(win)

    win.getMouse()
    win.close()

main()

