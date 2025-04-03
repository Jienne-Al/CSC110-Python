def largest(a, b, c):
    num=[a,b,c]
    l=num[0]

    for i in range(1, len(num)):
        if num[i]>l:
            l=num[i]
    return l

print(largest(1000,90,2))