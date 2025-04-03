import random

total = 0
game_ended = False

while not game_ended:
    random_number = random.randint(1, 10)
    print(f"Generated number: {random_number}")
    total += random_number if random_number != 7 else 0

    if random_number == 7 or total >= 50:
        game_ended = True

print(f"Total equals {total}")

if total >= 50:
    print("Congratulations - You won!")
else:
    print("Sorry - You lost!")


#MY GAME SCORE
'''import random

x = random.randint(1, 10)
total = 0

while x != 7:
    x = random.randint(1, 10)
    if x != 7:
        total += x
        print(f"Generated number: {x}")

    if total >= 50:
        print("Congratulations! You won")
        break

    if x == 7: a
    print(f"Generated number: {x}")
    print("Sorry you lost")
    break

print(f"Total: {total}")'''
