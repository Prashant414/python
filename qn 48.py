# # # Write a program to calculate HCF of Two given number.
# import math
# a=7
# b=5
# c=math.gcd(a,b)
# print(c)
#

a=25
b=50
for i in range (2,a+1):
    if (a%i==0) and (b%i==0):
        hcf=i
        break
    else:
        hcf=1
    

print(hcf)
