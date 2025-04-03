import random

def roll():
    number=random.randint(1,6)
    return(number)
def stats():
    a=roll()
    l=[0,0,0,0,0,0]
    for i in range(1000):
        l[a-1]=l[a-1]+1
        a=roll()
    return(l)
print(stats())