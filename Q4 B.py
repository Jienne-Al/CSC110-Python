'''Write a program that generates a random number X from 1 to 100.
Your program will print out a running sum of the random numbers X under the following conditions:
Add X to sum if and only if (X+sum) is not a multiple of 5
Stop when the sum is greater than 1000
Print out a running list of two different numbers: X and sum.
X is 63, sum is 63
X is 8, sum is 71
X is 29, sum is still 71 (do not add 29 because 71+29 = 100 is a multiple of 5)
X is 50, sum is 121
X is 78, sum is 199…
…and so on until sum reaches sum>1000. You may have difficulty getting a print-out of every X and every sum, do what you can for partial credit.'''

import random

total=0
while total < 1000:
    x=random.randint(1,100)
    total+=x
    if total % 5 != 0:
        total-=x
        print(f"x is {x}, sum is {total}")