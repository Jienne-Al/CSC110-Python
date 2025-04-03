import math

# Get user input
x = input("Enter an int, a float, and a string (no quotation marks) separated by commas: ")
y = x.split(",")

# Integer: Square the first value
a = int(y[0]) ** 2
print("The square of",y[0],"is",a)

# Float: Square root of the second value
b = math.sqrt(float(y[1]))
re=round(b,2)
print("The square root of",y[1],"is",re)

# String: Get the ASCII code of the first character of the third value
print("The ASCII code for", y[2], "is", " ".join(str(ord(i)) for i in y[2]))
