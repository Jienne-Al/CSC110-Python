from graphics import *

win = GraphWin("House", 800, 800)
win.setBackground("blue")

#House frame
A = win.getMouse()
B = win.getMouse()

frame = Rectangle(A,B)
frame.setFill('red')
frame.draw(win)

#Door is 1/5 as wide as house frame
x = A.getX()
y = B.getX()
w = A.getY()
z = B.getY()
L=y-x

C = win.getMouse()
Cx = C.getX()
Cy = C.getY()


doorA = Point(Cx-L/10,Cy)
doorB = Point(Cx+L/10,Cy)

doorC = Point(Cx-L/10,A.getY())
doorD = Point(Cx+L/10,A.getY())

#door
door = Polygon(doorA,doorB,doorD,doorC)
door.setFill('yellow')
door.draw(win)

#window
E = win.getMouse()
Ex = E.getX(); Ey = E.getY()
s = L/10
windowLo = Point(Ex-s,Ey-s)
windowHi = Point(Ex+s,Ey+s)
window = Rectangle(windowLo,windowHi)
window.setFill('turquoise')
window.draw(win)

#roof
F = win.getMouse()
roof = Polygon(Point(x,z),F,B)
roof.setFill('gray')
roof.draw(win)
