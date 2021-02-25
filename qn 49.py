# Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered.
x="y"
a,b,c=0,0,0
while x=="y":
    z=int(input("number"))
    x = input("again?? y/n")

    if z>0:
        a=a+1
    elif z<0:
        b=b+1
    elif z==0:
        c=c+1




print("positive",a,"negative",b,"zero",c)




