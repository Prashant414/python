# # Write a do-while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user whether he or she wishes to perform the operation again. If so, the loop should repeat; otherwise it should terminate.
# x=1
# while x!=0:
#     c = int(input("number 1"))
#     d = int(input("number 2"))
#     a=c+d
#     print(a)
#
#     z=input("do you wish to continue (y/n)")
#     if z=="y":
#         x=1
#     elif z=="n":
#         x=0
#     else:
#         print("choose between options only")
option="y"
while option=="y":


    a=int(input("value"))
    b=int(input("second value"))
    print(a+b)
    option=input("y/n")
