# # Write a program to find the factorial value of any number entered through the keyboard.
# def fact (n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("value of n"))
# fact(n)
# print(fact(n))
#
n=3
fact=1
for i in range(n,0,-1):
    if n==0:
        fact=fact*1
    else:
        fact=fact*i
print(fact)