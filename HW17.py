from graphics import *
infilet=open("t.txt", "r")
infilev=open("v.txt", "r")
win=GraphWin("Canvas",600,650)
win.setBackground("white")
win.setCoords(-4,-5,25,40)

x_axis=Line(Point(-0.75,0),Point(25,0)).draw(win)
y_axis=Line(Point(0,-1),Point(0,40)).draw(win)

T=Text(Point(11.5,-3.2),"Time")
T.setStyle("bold")
T.draw(win)
V=Text(Point(-2,23),"Velocity")
V.setStyle("bold")
V.draw(win)

infilet_contents=infilet.read().strip()
infilev_contents=infilev.read().strip()

#X=TIME
#Y=VELOCITY
raw_x=infilet_contents.split("\n")
raw_y=infilev_contents.split(",")

for x in raw_x:
    y=float(raw_y[int(x)])
    x=float(x)
    z=Circle(Point(x,y),0.1)
    z.setFill("red")
    z.draw(win)

for a in range(0,31):
    if a%5==0:
        if a==25:
            continue
        lx = Line(Point(a, 0.5), Point(a, -0.5)).draw(win)
        Text(Point(a,-1.2),str(a)+"s").draw(win)

for i in range(0,41,5):
    if i == 0:
        continue
    if i == 40:
        continue
    ly = Line(Point(-0.5, i), Point(0.55, i)).draw(win)
    Text(Point(-1.50,i),str(i)+"m/s").draw(win)

print("X","Y")
for i in raw_x:
    print(i,raw_y[int(i)])

win.getMouse()
win.close()