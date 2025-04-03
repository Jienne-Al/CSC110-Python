from graphics import *
win = GraphWin("Canvas", 600, 400)
win.setBackground("White")
win.setCoords(0,0,30,20)

def main_layout():
    title = Text(Point(15,15.5),"Currency Converter")
    title.setTextColor("black")
    title.setSize(30)
    title.setStyle("bold")
    ln = Line(Point(8.1,14.6),Point(22,14.6))
    ln.setWidth(2)
    subtitle=Text(Point(15,14),"Currency Exchange Rate USD$1 = €0.92")
    subtitle.setTextColor("black")
    subtitle.setSize(12)
    prompt = Text(Point(15, 12), "Enter the amount you wish to convert:")
    prompt.setTextColor("black")
    prompt.setSize(12)
    prompt.draw(win)
    subtitle.draw(win)
    title.draw(win)
    ln.draw(win)

def exit_prompt():
    exit_text = Text(Point(26.5, 2.5), "Exit")
    exit_text.setStyle("bold")
    exitbox = Rectangle(Point(24, 1), Point(29, 4))
    exitbox.setFill("#FE5858")
    exitbox.draw(win)
    exit_text.draw(win)
    return exitbox

def main_prompt():
    inputBox = Entry(Point(15, 10.5), 30)
    inputBox.setFill("white")
    inputBox.setSize(18)
    inputBox.setStyle("italic")
    inputBox.setTextColor("grey")
    inputBox.draw(win)
    return inputBox

def calc(val):
    result = val*0.92
    return result

def convert_prompt():
    convert_text = Text(Point(15, 8), "Click to convert")
    convert_text.setTextColor("white")
    convert_text.setStyle("bold")
    convert_text.setOutline("black")
    convertbox = Rectangle(Point(12, 7), Point(18, 9))
    convertbox.setFill("#58D6FE")
    convertbox.draw(win)
    convert_text.draw(win)
    return convertbox

def output_prompt():
    output_text = Text(Point(15, 5), "")
    output_text.setSize(18)
    output_text.setTextColor("red")
    output_text.draw(win)
    return output_text

main_layout()
exit_button = exit_prompt()
inputBox = main_prompt()
convert_button = convert_prompt()
output_text = output_prompt()

while True:
    mouse = win.getMouse()
    x = mouse.getX()
    y = mouse.getY()
    if 12<x<18 and 7<y<9:
        val = inputBox.getText()
        amount = float(val)
        converted = calc(amount)
        output_text.setText(f"€{converted:.2f}")
    elif 24<x<29 and 1<y<4:
        break
win.close()
