import random
def play():
    return random.randint(1,100)

def stats():
    odd=0
    even=0
    for i in range(1000):
        x=play()
        if x % 2 == 0:
            even+=1
        else:
            odd+=1
    freq_e=even/100
    freq_o=odd/100

    print(f"The probability for even numbers is {freq_e*10:.1f}%")
    print(f"The probability for odd numbers is {freq_o*10:.1f}%")

stats()