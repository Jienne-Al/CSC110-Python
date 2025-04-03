'''Write a program that allows the user to guess a random
number from 1 to 50. It should include an enter() function, asking the user: n = int(input(“Guess?”)).
First you will generate a random number from 1 to 50 using the
random() module. Don’t tell the user what the random number is!
Next you will call the function enter() five times = five guesses.
For each guess, there are three possible responses:
“Too high” followed by “Guess?” from the enter() function
“Too low” followed by “Guess?” from the enter() function
“Bingo!”` at which point it exits the program
Write a simple for loop so that the user gets at most 5 guesses.
After 5 wrong guesses, the computer responds: “Sorry - the number was n”'''

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