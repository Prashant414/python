# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing' then add 'ly'
# instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

a=input("string")
b=len(a)
if b<3:
    print(a)
elif "ing" in a:
    print(a+"ly")
else:
    print(a+"ing")
