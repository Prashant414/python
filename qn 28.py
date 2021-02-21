# Reverse a given integer number
x=int(input("give value"))
z=0
while x>0:
    y=x%10
    z=(z*10)+y

    x=x//10
    print(z)


