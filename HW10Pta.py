'''Write a program to generate a list that contains numbers divisible by 4,
but not divisible by 3 and not divisible by 7. The numbers should all fall between 1 and n, where n=input by the user.

Example output: 4, 8, 16, 20, 32 when n=37

Write the output to a text file named HW10.txt where the output appears on the page as
a vertical column of numbers. When someone opens HW10.txt with notepad
they should see a single vertical list of numbers, no commas or letters.'''

out=open("HW10.txt","w")

n=int(input("Give me a number"))

for a in range(1,n+1):
    if a%4==0:
        if a%3!=0:
            if a%7!=0:
                print(str(a), file=out)

out.close()
