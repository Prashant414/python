# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

a=input("string:")
b=input("string")
c=a[:2]+b[2:]
d= b[:2]+a[2:]
e=d+" "+c
print(e)
