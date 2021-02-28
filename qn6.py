# Take input of age of 3 people by user and determine oldest and youngest among them.
x=int(input("age of x"))
y=int(input("age of y"))
z=int(input("age of z"))
if x>=y and x>=z:
    print("oldest is x")
    if y>=z:
        print("youngest is z")
    elif y==z:
        print("y and z is youngest")
    else:
        print("youngest is y")
elif y>=x and y>=z:
    print("oldest is y")
    if x>=z:
        print("youngest is z")
    elif x==z:
        print("x and z is youngest")
    else:
        print("youngest is x")
elif z>=x and z>=y:
    print("oldest is z")
    if x>=y:
        print("youngest is y")
    elif x==y:
        print("x and y is youngest")
    else:
        print("youngest is x")
else:
    print("same")
