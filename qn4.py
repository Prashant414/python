# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
a=int(input("year of service"))
b=int(input("salary"))
if a<=5:
    print("salary is",b)
else:
    x=b*5/100
    y=b+x
    print("salary is",y)
