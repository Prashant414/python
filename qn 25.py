# # # find factorial
# # def fact(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #
# #         return n*fact(n-1)
# # x=int(input("value"))
# # a=fact(x)
# # print(a)
x=5
y=1
if x<0:
    print("not valid")
elif x==0 or x==1:
    print("1")
else:
    for i in range (2,x+1):
        y=y*i
print(y)


