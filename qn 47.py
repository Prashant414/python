# Write a program that prompts the user to input a positive integer.
# It should then output a message indicating whether the number is a prime number.
x=int(input("positive integer"))
if x > 1:



    for i in range (2,x):
        if x%i==0 :

            print("not prime number")
            break


    else:
        print("prime number")
else:
    print("not a prime number")




