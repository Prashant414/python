# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
x=(1,2,3,4,5,6,7,8,9)
y=0
z=0
for a in x:
    if a%2==0:
        y=y+1
    else:
        z=z+1
print("even is",y)
print("odd is",z)
