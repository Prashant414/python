# #write a program that takes a string with multiple words and then capitalises the first
# # letter of each words and forms a string out
# #of it
#
# a=input("string ")
# # b=a.capitalize()
# # print(b)
# b=a.title()
# print(b)
a=input("write anything")
b=a.split()
c=""
for i in b:
    c=c+ " " +i.capitalize()
print(c[1:])


