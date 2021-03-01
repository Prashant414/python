# Given a number count the total number of digits in a number
x=int(input("number"))
y=0
while x>0:
    y=y+1
    x=x//10
print("no. of digit is",y)