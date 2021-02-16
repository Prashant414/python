# # x = int(input("value of x"))
# # y = int(input("value of y"))
# # c = int(input('''enter your choice
# # 1 addition
# # 2 subtraction
# # 3 division
# # 4 multiplication'''))
# # if c==1:
# #     d=x+y
# #     print(d)
# # elif c==2:
# #     d=x-y
# #     print(d)
# # elif c==3:
# #     d=x/y
# #     print(d)
# # elif c==4:
# #     d=x*y
# #     print(d)
# # else :
# #     print("choose the correct otion")
def sum(a,b):
    return c+b
def subtraction(a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b):
    return a/b
x=1
while(x!=0):
    a = int(input("value of a" ))
    b = int(input("value of b"))
    c=int(input('''enter your choice
    1 sum
    2 subtraction
    3 multiplication
    4 division'''))
    if c==1:
        print ("addition is",sum(a,b))
    elif c==2:
        print ("subtraction is ",subtraction(a,b))
    elif c==3:
        print ("multiplication is",multiplication (a,b))
    elif c==4:
        print("division is ",division(a,b))
    elif c==5:
        print("choose the correct option")
    z=input("do you wish to continue (y/n)")

    if z=="y":
        x=1
    elif z=="n":
        x=0







