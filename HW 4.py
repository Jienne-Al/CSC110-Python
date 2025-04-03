x = input("How much currency would you like to convert?")
dollars = float(x)
conversion_rate = 0.97
euros = dollars*conversion_rate
print("$" + str(dollars) + " converts to €" + str(euros) + " Euros.")