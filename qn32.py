# Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range (6):
    for j in range (1,i+1):
        print("*",end= " ")
    print()
for i in range (6):
    for j in range (2,6-i):
        print("*",end=" ")
    print()