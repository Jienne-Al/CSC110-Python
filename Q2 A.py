'''Your computer science instructor gives scores from zero to five on quizzes,
where score=grade
0 = F
1 = F
2 = D
3 = C
4 = B
5 = A
Write a program that allows the user to input a score from
0 to 5 and prints out the correct grade. The output should look like this:
‘’Your quiz score was X, your grade is Y’’.'''


n=int(input("Score from 0-5"))
system=["F","F","D","C","B","A"]
print("Your quiz was",n,",","your grade is",system[n])