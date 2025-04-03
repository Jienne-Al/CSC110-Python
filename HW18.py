from graphics import *
import random

win = GraphWin("Canvas", 800, 850)
win.setBackground("white")
win.setCoords(-2, -10, 15, 50)

x_axis = Line(Point(1, 0), Point(13, 0)).draw(win)
y_axis = Line(Point(1.2, -1), Point(1.2, 42)).draw(win)

for a in range(2, 13):
    Text(Point(a, -1.5), str(a)).draw(win)

for b in range(0, 201, 20):
    Text(Point(0.75, b * 0.2), str(b)).draw(win) #also compressed to 0.2

def roll_dice():
    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in range(1000):
        die = random.randint(1, 6) + random.randint(1, 6)
        index = die - 2 #set first value on index 0
        frequency[index] = frequency[index] + 1
    return frequency

def histogram(frequency):
    drawn = []
    for d in range(11):
        R = random.randint(20,80)
        G= random.randint(100,160)
        B = random.randint(20,80)
        height = frequency[d] * 0.2 #compress to smaller value(should be the same for str y's)
        bar = Rectangle(Point(d + 1.5, 0), Point(d + 2.5, height)) #str x's will be on x=2,3,4...12
        bar.setFill(color_rgb(R,G,B))
        bar.setWidth(1)
        bar.draw(win)
        drawn.append(bar)
    return drawn

def undraw(drawn_bars):
    for bar in drawn_bars:
        bar.undraw()

def main_layout():
    title = Text(Point(7, 45), "Two Dice Histogram")
    title.setTextColor("black")
    title.setSize(30)
    title.setStyle("bold")
    D=Text(Point(7, -4.5), "Sum of Two Dice")
    D.setStyle("bold")
    D.setSize(15)
    F=Text(Point(-0.5, 25), "Frequency")
    F.setStyle("bold")
    F.setSize(15)
    F.draw(win)
    D.draw(win)
    title.draw(win)

def exit_prompt():
    exit_text = Text(Point(12.75, -7), "Exit")
    exit_text.setStyle("bold")
    exitbox = Rectangle(Point(11, -4.75), Point(14.5, -9.25))
    exitbox.setFill("#FE5858")
    exitbox.draw(win)
    exit_text.draw(win)

def rollagain_prompt():
    roll_text = Text(Point(0.25, -7), "Roll Again")
    roll_text.setStyle("bold")
    rollbox = Rectangle(Point(-1.5, -4.75), Point(2, -9.25))
    rollbox.setFill("#58D6FE")
    rollbox.draw(win)
    roll_text.draw(win)

main_layout()
exit_prompt()
rollagain_prompt()

frequency = roll_dice()
drawn = histogram(frequency)
print(roll_dice())

current=True
while current:
    mouse = win.getMouse()
    x = mouse.getX()
    y = mouse.getY()
    if 11 < x < 14.5 and -9.25 < y < -4.75:
        current=False
        win.close()
        break
    elif -1.5 < x < 2 and -9.25 < y < -4.75:
        undraw(drawn)
        frequency = roll_dice()
        drawn = histogram(frequency)