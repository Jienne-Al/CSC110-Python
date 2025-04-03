'''Write a function main() that generates a random number x from 1 to 10, then determines
if that number is closer to zero or 10. There are three possible outputs:
“The number x is closer to zero”
“The number x is closer to ten”
“The number x is equally close to zero and ten”
X should be replaced by whatever random number your code generates from 1 to 10.
Use the line import random at the start of your code to call random.randint(a,b). Finish with the line main() to execute the program.'''

import random
def main():
    x=random.randint(1,10)
    if x < 5:
        print(f"The number {x} is closer to zero")
    elif x > 5:
        print(f"The number {x} is closer to ten")
    elif x == 5:
        print(f"The number {x} is equally closer to zero and ten")
main()