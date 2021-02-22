# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
a=0
sum=0
for i in range (0,5):
    a=a+(2*(10**i))
    sum=sum+a
print(sum)
