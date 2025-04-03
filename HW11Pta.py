'''Read the first half of Chapter 8 in Zelle, then write a program that accepts a
list of quiz scores between 0 and 20, separated by commas. Your program should allow the
user to enter as many scores as they like. Drop the lowest score, then calculate the average and print out a grade as follows:
18<= x <=20    "A"
16<= x < 18    "B"
14<= x < 16    "C"
12<= x < 14    "D"
 x < 12       "F"
Example: “Enter your scores “ —> 15, 8, 19, 15.5 / drops the 8, avg = 16.5 —> prints out “B”.'''

raw=input("Your scores separated by commas:")
string_marks=raw.split(",")

int_marks=[]
for a in string_marks:
    int_marks.append(float(a))

s=int_marks[0]
for b in range(len(int_marks)):
    if int_marks[b]<s:
        s=int_marks[b]

new_marks=[]
count = 0
for c in int_marks:
    if s == c:
        count+=1
        if count == 1:
            continue
    new_marks.append(c)

total=0
for d in new_marks:
    total=total+d

average=total/len(new_marks)

if average >= 18:
    if average <= 20:
        print("A")
if average >= 16:
    if average < 18:
        print("B")
if average >= 14:
    if average < 16:
        print("C")
if average >= 12:
    if average < 14:
        print("D")
if average < 12:
    print("F")