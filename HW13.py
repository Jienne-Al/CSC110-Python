import random

def enter():
    return input("Guess?")

x = random.randint(1, 51)

while True:
    play = enter()
    if play == "":
        print(f"Sorry - the number was {x}")
        break
    play = int(play)
    if play == x:
        print("Bingo!")
        break
    elif play > x:
        print("Too high")
    elif play < x:
        print("Too low")