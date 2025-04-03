'''“Doubling time” is the time it takes for an investment to double in value.
Write a program that calculates the doubling time in years for an initial
investment P_o at an annual interest rate of R percent. Recall the compound interest formula:
P(t)=P_o(1 + R/100)^t
where R is entered as a percent by the user, for example 5%. A couple of suggestions:
Set P_o to $100 for simplicity, the initial investment doesn’t affect the doubling time.
Ask the user for a straight percent R. I’ve inserted a while loop for you but you’re free to write your own.
Your program should ask for an interest rate and should return the doubling time in the minimum number of whole years.
Be sure to check your results against some realistic values.'''

def formula(R):
    P_o = 100
    P = P_o
    years= 0
    while P<2*P_o:
        P *= (1 + (R/100))
        years += 1
    return years

def main():
    R = float(input("Enter annual interest rate"))
    ans = formula(R)
    return f"With interest rate {R}, it will double in {ans} years"

print(main())

def formula():
    R = R/100
    final = 100*(1+(R/100))**(t)