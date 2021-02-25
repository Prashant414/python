# Write a program that reads a set of integers, and then prints the sum of the even and odd integers.
x=[111,12,3,14,15,6,7]
y=0
z=0
for i in x:
    if i%2==0:
        y=i+y


    elif i==1 or i%2==1:
        z=i+z

print(" sum even integers are",y)
print("odd odd integers are",z)



