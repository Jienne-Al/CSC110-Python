'''Begin your program by generating a list of 10 random numbers from 1 to 50, then ask the user
for a number N, any number. Determine which number X from your random list is closest to N.
You can ignore ties for this assignment. Finally, print out your random list along with a
statement like: The closest number to N on this list is X.'''

import random

L = []
for a in range(10):
    L.append(random.randint(1, 50))

N = int(input("Give me a number: "))
x_index = L[0]

for b in L:
    for c in L:
        if abs(b- N) < abs(x_index- N):
            x_index= b

print(f"Random list: {L}")
print(f"The closest number to {N} on this list is {x_index}.")
