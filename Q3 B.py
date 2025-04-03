'''Write a function that takes four integers as inputs and prints out the biggest one.
Do not use built-in functions like ‘max’ or ‘sort’, you may only use ‘if/elif/else’
statements in your code or you will get no credit.'''

def biggest(a, b, c, d):
    L=[a,b,c,d]
    B=L[0]
    for a in range(len(L)):
        if L[a] > B:
            B=L[a]
    print(B)

    