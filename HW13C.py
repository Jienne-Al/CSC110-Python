'''Write a program that adds letters to a word as you type. Example:

Program asks, “What is your first letter?” You type “C”, computer displays “C”
Program asks, “Next letter?” You type “a”, computer displays “Ca”
Program asks, “Next letter?” You type “t”, computer displays “Cat”
Program asks, “Next letter?” You press any button on the keyboard that is not in the alphabet (A-Z or a-z) and the program responds “game over”
Hint: Look up the letters in the ASCII table'''

s= ""
first = input("What is your first letter?")
s+=first
while True:
    ans = input("Next letter?")
    s+=ans
    if ord(ans) < ord('A'):
        break
    elif ord(ans) > ord('Z'):
        if ord(ans) < ord('a'):
            break
    elif ord(ans) > ord('z'):
        break
    print(s)
print("game over")