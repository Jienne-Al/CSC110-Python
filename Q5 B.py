from graphics import *
import random

win = GraphWin("Canvas", 750, 850)
win.setBackground("white")
win.setCoords(-4, -10, 14, 50)

x_axis = Line(Point(0, 0), Point(12, 0)).draw(win)
y_axis = Line(Point(0, 0), Point(0, 42)).draw(win)

for i in range(0, 11):
    Text(Point(i + 0.5, -1.5), i).draw(win)

for i in range(0, 401, 50):
    Text(Point(-0.75, i * 0.1), i).draw(win)


def count(A, B):
    c = 0
    lenA = len(A)
    lenB = len(B)
    if lenA < lenB:
        mini = lenA
    else:
        mini = lenB

    index = 0
    while index < mini:
        if A[index] == B[index]:
            c += 1
        index += 1
    return c


def experiment():
    M = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1000):
        A = str(random.random())
        A = A[2:14]
        B = str(random.random())
        B = B[2:14]
        matches = count(A, B)
        if matches < len(M):
            M[matches] = M[matches] + 1
    return M


def histogram(M):
    for a in range(11):
        height = M[a] * 0.1
        bar = Rectangle(Point(a, 0), Point(a + 1, height))
        bar.setFill("light blue")
        bar.setWidth(1)
        bar.draw(win)


def main_layout():
    title = Text(Point(5, 45), "Matching Random Digits")
    title.setTextColor("black")
    title.setSize(20)
    title.setStyle("bold")
    D = Text(Point(5, -4.5), "Number of Matches")
    D.setStyle("bold")
    D.setSize(10)
    F = Text(Point(-2.5, 25), "Frequency")
    F.setStyle("bold")
    F.setSize(10)
    F.draw(win)
    D.draw(win)
    title.draw(win)


M = experiment()
histogram(M)
main_layout()
print(M)

win.getMouse()
win.close()
