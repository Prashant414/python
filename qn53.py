# Write a program to calculate the sum of following series where n is input by user.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n
n=int(input("value of n"))
s=0
for i in range (1,n+1):
    s=s+1/i
print(s)
