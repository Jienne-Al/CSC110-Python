'''The user enters two strings with input items separated by commas. Example:
A = 10,20,30,40
B = w,x,y,z
The program outputs two columns in partially reversed order. The left column is in regular order, the right column is in reverse order.
10  z
20  y
30  x
40  w
Your code must work for any two strings the user chooses
to enter, of any length so long as items are separated by commas
and both strings contain the same number of items.'''

first=input("Give me a string separated by commas")
second=input("Give me a string separated by commas")

a=first.split(",")
b="".join(a)
c=str(b)

d=second.split(",")
e="".join(d)
f=str(e)
g=f[::-1]

h=list(c)
i=list(g)

for j in range(len(a)):
    k=str(a[j])+" "+str(i[j])
    print(k,"\n")

