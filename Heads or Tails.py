import random

def guess():
    x = random.randrange(1,2)
    if x == 1:
        return 'H'
    if x == 2:
        return 'T'

def game():
    ans = input("H or T?")
    val = guess()
    if val == ans:
        print("You are right!")
    if val != ans:
        print(f"You are wrong. It was {val}")
    ask = input("Play again? (Y or N)")
    if ask == "Y":
        game()

game()