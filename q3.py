# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
x=int (input("number of quantity"))
if x<=10:
    total = x*100
    print("total cost",total)
else:
    y= x*100
    total= y-(y*10/100)
    print("total cost",total)