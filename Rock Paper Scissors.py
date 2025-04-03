import random

def guess():
    x = random.randrange(3)
    if x == 0:
        return "Rock"
    if x == 1:
        return "Paper"
    if x == 2:
        return "Scissors"

def game():
    ans = input("Rock, Paper or Scissors?").capitalize()
    val = guess()

    if ans == "Rock" and val == "Scissors":
        print("You win!")
    elif ans == "Scissors" and val == "Paper":
        print("You win!")
    elif ans == "Paper" and val == "Rock":
        print("You win!")
    elif ans == val:
        print("Tie")

    ask = input("Play again? Y/N")
    if ask == 'Y':
        game()

game()
