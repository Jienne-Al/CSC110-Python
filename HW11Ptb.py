'''First write a short program (could be a function, does not have to be)
using the random module that generates 15 random numbers from 1 to 50 and prints out that list.
Next, modify the program to do the following: print the list of 15 random numbers from 1 to 50
then write the even ones to a file named evens.txt and the odd ones to odds.txt.
Now comes the tricky part: the random number generator can produce duplicates.
Go back and modify your code once more to eliminate any duplicates in the output files. No number appears more than once..'''

E=open("evens.txt","w")
O=open("odds.txt","w")

import random

L=[]
for a in range(15):
    n=random.randint(1, 50)
    L.append(n)

new_L=[]
for b in L:
    if b not in new_L:
        new_L.append(b)

for c in new_L:
    if c%2==0:
        print(str(c).strip(), file=E)
    else:
        print(str(c).strip(), file=O)

E.close()
O.close()