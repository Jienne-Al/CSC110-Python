'''Write a script that generates the integers 1-50 then processes them as follows:

Picks out multiples of 3 but not multiples of 5 and concatenates them to a string named T for Three.
Commas separate values in the string T. Strip off the last comma in T. Do not use and, do not use or in your code or you will not get any credit. You must code using if and else statements.

Picks out multiples of 5 but not multiples of 3, appends them to a list named F for Five. Same thing -
Do not use and, do not use or in your code or you will not get any credit.

Picks out common multiples of both 3 and 5, writes them vertically in a column in a text file named B.txt for Both.
Use the Runestone convention for writing text to a file –> outfile.write(“stuff you’re writing”). Again, no and, no or commands.

Print out the string T and the list F at the end of your code to check your work. The text file B.txt will print itself.'''

outfile=open("B.txt","w")

L=[]
for a in range(1,51):
    L.append(a)

T=""
for b in L:
    if b % 3 == 0:
        if b % 5 !=0:
            T+=str(b)+","
F=[]
for c in L:
    if c % 5 == 0:
        if c % 3 !=0:
            F.append(c)
for d in L:
    if d % 3 ==0:
        if d % 5==0:
            outfile.write(str(d)+"\n")
print(T[:-1]) #1
print(F) #2
outfile.close()
