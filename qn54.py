#
# 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
# where n is a positive integer and input by user.
n=int(input("value of n"))
s=0

for i in range (1,n+1):
    if i%2==0:
        s = (s - 1 / i)
        # print(s)
    else:
        s = (s + 1 / i)
print(s)




