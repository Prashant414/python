a=153
c=a
sum=0
i=len(str(c))
while (a!=0):
    s=a%10
    a=a//10
    sum=sum+(s**i)
print(sum)
if sum==c:
    print("armstrong")
else:
    print("not armstrong")



