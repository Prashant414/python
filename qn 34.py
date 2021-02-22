# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
x=int(input("value of x"))
if x<=0:
    print("gues is wrong")
elif x in range (1,10):
    print("right")
