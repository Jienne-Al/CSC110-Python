'''
Write a short program that prints the odd numbers from 50 down to 40 in a vertical column. 
You must start with the FOR loop for i in [1,2,3,4,5], do not change Line 1 below. 
A simple print-out of the odd numbers will receive zero credit. 
This is a very easy program that can be accomplished in 2 or 3 lines, do not use more than 3.
'''
for i in [1, 2, 3, 4, 5]:  ## do not change this line
    result = 51 - 2 * i
    print(result) if result >= 40 else None