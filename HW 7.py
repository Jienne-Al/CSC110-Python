import math


x = input("Enter an int, a float, and a string (no quotation marks) separated by commas: ")
y = x.split(",")


a = int(y[0]) ** 2

b = math.sqrt(float(y[1]))
re=round(b,2)

word=y[2]
result=""
for i in word:
    result=result + str(ord(i)) +" "
print("The square of {} is {}\nThe square root of {} is {}\nThe ASCII code for {} is {}".format(y[0],a,y[1],re,y[2],result))