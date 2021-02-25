# Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.
x=123
z=0
while x>0:
    y=x%10
    z=(z*10)+y
    x=x//10
print(z)

