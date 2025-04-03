import string
#UNICODE
#In this version, you have to know the unicode table
message=input("Give me the message")
'''
c=[]
for a in message.split():
    code=int(a)
    c.append(chr(code))

print(c)
message=" ".join(c)
print(message)'''

#BABY VERSION
##UNICODE

c=[]
for a in message:
    c.append(ord(a))
print(c)

f=""
for d in c:
    e=chr(d)
    f=f+e
print(f)

print()

#ROMAN NUMERALS
a=string.ascii_lowercase+" "

L=[]
for b in message:
    pos = a.find(b)
    n_pos = pos + 1
    L.append(n_pos)
print(L)

for c in L:
    d=c-1
    print(a[d], end="")
