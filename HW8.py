value_1=input("Name of item: ")
value_2=float(input("Price of the item:"))
value_3=int(input("Quantity:"))
value_4= float(input("Weight per item (in pounds):"))

subtotal=value_2*value_3
weight=value_3*value_4
shipping=(0.25*weight)+5
tax=(subtotal+shipping)*0.085
total=subtotal+shipping+tax

print("You have purchased: {} x {}".format(value_1,value_3))
print("Subtotal is ${:.2f}".format(subtotal))
print("Total Weight is {:.2f} pounds".format(weight))
print("Shipping and handling costs are ${:.2f}".format(shipping))
print("Tax is ${:.2f}".format(tax))
print("Total is ${:.2f}".format(total))