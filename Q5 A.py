#Jienne Alegre
from graphics import *
win = GraphWin("The 5-Click House", 800, 800)
win.setBackground("skyblue")
win.setCoords(0, 0, 8, 8)

def myhouse():
    A = win.getMouse()
    B = win.getMouse()

    frame = Rectangle(A, B)
    frame.setFill("orange")
    frame.draw(win)

    frame_width= B.getX()- A.getX()

    C = win.getMouse()
    door_width = frame_width/5
    door_bottom_left = Point(C.getX() - door_width / 2, A.getY())
    door_upper_right = Point(C.getX() + door_width / 2, C.getY())
    door = Rectangle(door_bottom_left, door_upper_right)
    door.setFill("green")
    door.draw(win)

    D = win.getMouse()
    Dx = D.getX()
    Dy = D.getY()

    window_width = frame_width / 5
    window_height = window_width

    window = Rectangle(Point(Dx - window_width / 2, Dy - window_height / 2),
                       Point(Dx + window_width / 2, Dy + window_height / 2))
    window.setFill("pink")
    window.draw(win)

    E = win.getMouse()
    roof = Polygon(Point(A.getX(), B.getY()), Point(B.getX(), B.getY()), E)
    roof.setFill("brown")
    roof.draw(win)

    win.getMouse()
    win.close()

myhouse()
