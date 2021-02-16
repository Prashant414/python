# n=int(input("value of n"))
# fact=1
# for i in range(n,0,-1):
#     if i==0:
#         fact=fact*i
#
#     else:
#         fact=fact*i
# print(fact)

def fact(n):

    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

a=int(input("value of a"))
fact(a)
print(fact(a))