#Write a program that asks the user for two numbers:
#m = max
#s = step size
#where m and s are both positive integers. Your program will print out all of the multiples of s less than m+1, for example:
#If m = 20 and s = 3, program prints “3, 6, 9, 12, 15, 18”
#if m = 20 and s = 4, program prints “4, 8, 12, 16, 20”
#The output should print horizontally, all on one line, as a list of numbers separated by commas. Try to get rid of the last comma as well.
m = int(input("Max: "))
s = int(input("Steps: "))
result = ""
for i in range(s, m+1, s):
    result = result + str(i) + ", "
print(result[:-2])