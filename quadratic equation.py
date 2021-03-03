import cmath
a=int(input("value of a "))
b=int(input("value of b"))
c=int(input("value of c"))

d=(b**2)-(4*a*c)
x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)
print(x1,x2)