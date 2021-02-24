# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. Go to the editor
n=int(input("value of n"))
s=0
for i in range (1,n+1):
    s=s+i
a=s/n
print(s,a)


