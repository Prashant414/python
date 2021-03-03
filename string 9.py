# Write a Python program to remove the characters which have odd index values of a given string.
a=input("give value:")

n=""
for i in range (len(a)):
    if i%2==0:
        n=n+a[i]
c=n[1:]
print(n)
print(c)