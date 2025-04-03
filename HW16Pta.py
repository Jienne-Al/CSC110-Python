import random
from graphics import *
win = GraphWin("Canvas", 1000, 500)
win.setBackground("white")
win.setCoords(0, 0, 20, 10)

rec1 = Rectangle(Point(2, 2), Point(8, 8))
rec1.setFill("pink")
rec1.setOutline("black")
rec1.setWidth(1)
rec1.draw(win)

rec2 = Rectangle(Point(12, 2), Point(18, 8))
rec2.setFill("#ffd166")
rec2.setOutline("black")
rec2.setWidth(1)
rec2.draw(win)

lcenter = Point(5, 5)
rcenter = Point(15, 5)

left_dots = []
right_dots = []

def undraw_l():
    for dot in left_dots:
        dot.undraw()
    left_dots.clear()

def dot1():
    undraw_l()
    dot1 = Circle(lcenter, 0.5)
    dot1.setFill("black")
    dot1.draw(win)
    left_dots.append(dot1)

def dot2():
    undraw_l()
    dot2 = Circle(Point(4, 5), 0.5)
    dot2.setFill("black")
    dot2.draw(win)
    left_dots.append(dot2)
    dot2b = dot2.clone()
    dot2b.move(2, 0)
    dot2b.draw(win)
    left_dots.append(dot2b)

def dot3():
    undraw_l()
    dot3 = Circle(Point(6, 6), 0.5)
    dot3.setFill("black")
    dot3.draw(win)
    left_dots.append(dot3)
    for a in range(3):
        dot3b = dot3.clone()
        dot3b.move(-a, -a)
        dot3b.draw(win)
        left_dots.append(dot3b)

def dot4():
    undraw_l()
    dot4 = Circle(Point(4, 4), 0.5)
    dot4.setFill("black")
    dot4.draw(win)
    left_dots.append(dot4)
    dot2 = dot4.clone()
    dot2.move(2, 2)
    dot2.draw(win)
    left_dots.append(dot2)
    dot3 = dot4.clone()
    dot3.move(0, 2)
    dot3.draw(win)
    left_dots.append(dot3)
    dot4b = dot4.clone()
    dot4b.move(2, 0)
    dot4b.draw(win)
    left_dots.append(dot4b)

def dot5():
    undraw_l()
    dot5 = Circle(lcenter, 0.5)
    dot5.setFill("black")
    dot5.draw(win)
    left_dots.append(dot5)
    dot4()

def dot6():
    undraw_l()
    dot6 = Circle(Point(4, 3.5), 0.5)
    dot6.setFill("black")
    dot6.draw(win)
    left_dots.append(dot6)
    for c in range(2):
        dot6b = dot6.clone()
        dot6b.move(0, (c + 1) * 1.5)
        dot6b.draw(win)
        left_dots.append(dot6b)
        dot6b = dot6.clone()
        dot6b.move(2, (c + 1) * 1.5)
        dot6b.draw(win)
        left_dots.append(dot6b)
        dot6c = dot6.clone()
        dot6c.move(2, 0)
        dot6c.draw(win)
        left_dots.append(dot6c)

def undraw_r():
    for dot in right_dots:
        dot.undraw()
    right_dots.clear()

def rdot1():
    undraw_r()
    rdot1 = Circle(rcenter, 0.5)
    rdot1.setFill("black")
    rdot1.draw(win)
    right_dots.append(rdot1)

def rdot2():
    undraw_r()
    rdot2 = Circle(Point(14, 5), 0.5)
    rdot2.setFill("black")
    rdot2.draw(win)
    right_dots.append(rdot2)
    rdot2b = rdot2.clone()
    rdot2b.move(2, 0)
    rdot2b.draw(win)
    right_dots.append(rdot2b)

def rdot3():
    undraw_r()
    rdot3 = Circle(Point(16, 6), 0.5)
    rdot3.setFill("black")
    rdot3.draw(win)
    right_dots.append(rdot3)
    for a in range(3):
        rdot3b = rdot3.clone()
        rdot3b.move(-a, -a)
        rdot3b.draw(win)
        right_dots.append(rdot3b)

def rdot4():
    undraw_r()
    rdot4 = Circle(Point(14, 4), 0.5)
    rdot4.setFill("black")
    rdot4.draw(win)
    right_dots.append(rdot4)
    rdot2 = rdot4.clone()
    rdot2.move(2, 2)
    rdot2.draw(win)
    right_dots.append(rdot2)
    rdot3 = rdot4.clone()
    rdot3.move(0, 2)
    rdot3.draw(win)
    right_dots.append(rdot3)
    rdot4b = rdot4.clone()
    rdot4b.move(2, 0)
    rdot4b.draw(win)
    right_dots.append(rdot4b)

def rdot5():
    undraw_r()
    rdot5 = Circle(rcenter, 0.5)
    rdot5.setFill("black")
    rdot5.draw(win)
    right_dots.append(rdot5)
    rdot4()

def rdot6():
    undraw_r()
    rdot6 = Circle(Point(14, 3.5), 0.5)
    rdot6.setFill("black")
    rdot6.draw(win)
    right_dots.append(rdot6)
    for c in range(2):
        rdot6b = rdot6.clone()
        rdot6b.move(0, (c + 1) * 1.5)
        rdot6b.draw(win)
        right_dots.append(rdot6b)
        rdot6b = rdot6.clone()
        rdot6b.move(2, (c + 1) * 1.5)
        rdot6b.draw(win)
        right_dots.append(rdot6b)
        rdot6c = rdot6.clone()
        rdot6c.move(2, 0)
        rdot6c.draw(win)
        right_dots.append(rdot6c)

def left():
    x = random.randint(1, 6)
    if x == 1:
        dot1()
    elif x == 2:
        dot2()
    elif x == 3:
        dot3()
    elif x == 4:
        dot4()
    elif x == 5:
        dot5()
    elif x == 6:
        dot6()

def right():
    y = random.randint(1, 6)
    if y == 1:
        rdot1()
    elif y == 2:
        rdot2()
    elif y == 3:
        rdot3()
    elif y == 4:
        rdot4()
    elif y == 5:
        rdot5()
    elif y == 6:
        rdot6()

def main():
    c = 0
    caption = Text(Point(10, 9), "Click to roll the dice")
    caption.setSize(20)
    caption.draw(win)
    while True:
        win.getMouse()
        c += 1
        left()
        right()
        if c == 5:
            caption.undraw()
            end = Text(Point(10, 9), "Click anywhere to exit")
            end.setSize(20)
            end.draw(win)
            win.getMouse()
            win.close()
            break
        else:
            caption.undraw()
            caption = Text(Point(10, 9), "Roll again")
            caption.setSize(20)
            caption.draw(win)
main()
