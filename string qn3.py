# Write a Python program to get a string from a given
# string where all occurrences of its first char have been changed to '$',
# except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

a=input("give string:")
b=a[0]
z=a.replace(b,"$")
c=b+z
print(c[0:1]+c[2:])
