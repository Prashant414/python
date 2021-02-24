# Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number.
x=int(input("positive integer"))

for i in range (1,11):
    s=i*x

    print(s)