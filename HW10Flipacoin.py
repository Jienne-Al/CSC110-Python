'''Write a program that flips a coin ten times. It should include a function flip()
that simulates a single flip of a coin: it randomly prints either H or T for Heads or Tails.
Accomplish this by choosing 0 or 1 arbitrarily with random.randrange(2), and use an if-else
statement to print H (Heads) when the result is 1, T (Tails) when it’s 0. Review section 5.4 on the Random Module.

Now add a function main() to your program that calls flip() 10 times, so main() prints
out a random sequence HTTHTTHTHH every time you invoke it. Add the line main() to the end of your code.'''

import random

def flip():
    play = random.randrange(2)
    if play == 1:
        return "H"
    else:
        return "T"

def main():
    output = ""
    for a in range(10):
        output+=flip()
    print(output)

main()
