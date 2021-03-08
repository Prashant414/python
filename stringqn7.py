# Write a Python program to remove the nth index character from a nonempty string.
a=input("string")
n=int(input("nth value"))
x=a[:n]
y=a[n+1:]
z=x+y
print(z)
