import random

def enter():
    return int(input("Guess?"))

x = random.randint(1, 51)

c = 5
for i in range(5):
    play = enter()
    if play == x:
        print("Bingo!")
        break
    elif play > x:
        print("Too high")
    elif play < x:
        print("Too low")
    c -= 1

if c == 0:
    print(f"Sorry - the number was {x}")