'''Homework 9 part a
You are to write a function, call it price(a,b,c) where a=integer, b=string, c=float.
The first parameter a will be the quantity of the item, b will be the name of the item, and c is the price per item. The function will print out the total price for the quantity of items purchased.
Example: price(3,”bananas”,0.50) will print out the message “3 bananas cost $1.50”.
Make sure you format your price to print two decimal places.'''

def price(a,b,c):
    print("{} {} cost ${:.2f}".format(a,b,a*c))

'''Homework 9 part b
You are to write a function, call it main(). When a user runs this function,
the computer will ask the user to input a word of arbitrary length. Put the input command inside the function,
it has to run once the function is called. The function then returns the sum of the ASCII codes for that word,
so your function body must end with a return statement. Finally, add the line print(main()).
You’ll need to use a container variable and a for loop. HINT: The container itself will be a local variable,
so it must be defined inside (and only inside) the function definition.'''

def main():
    word=input("Give me a word")
    a=0

    for b in word:
        a=a+ord(b)

    return a
print(main())