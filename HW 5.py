#Write a program that calculates the average of n numbers. The program will have n+1 inputs:
#Enter how many numbers you wish to average: this is “n”
#Enter a number:
#Enter a number:
#Enter a number…(repeat n times)
#Output should be a statement of the form “The average of your [n] numbers is [average]”. Your average must be a float rounded to 2 decimal places (see section 3.5 in Zelle).
'''
total = 0
n = int(input("Enter how many numbers you wish to average: "))
for i in range(n):
    num = float(input("Give a number: "))
    total += num
print("The average of your", n, "numbers is", round(total / n, 2))
'''

#total = 0
#n = int(input("Enter how many numbers you wish to average: "))
#for i in range(n):
#    num = float(input("Give a number: "))
#    total += num
#print("The average of your", n, "numbers is", round(total / n, 2))
'''
word=input("Give me a word: ")
for i in word:
    print(i*3)
'''

#Write a program that calculates the steps from a to b. The inputs are integers entered by the user of your program.
#Ask user to enter the first integer, this is a
#Ask for a second integer, this is b
#Now calculate the steps from a to b using a counter, a for loop and a range expression. Do not use the formula b - a, you must use a counter to count the steps from a to b.
#Example: a = 21, b = 27. Output would be a statement of the form “There are 6 steps from 21 to 27”.
'''
c=0
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))
for i in range(a,b):
    c=c+1
print("There are", c,"steps from", a,"to", b)
'''