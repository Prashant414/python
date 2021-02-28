# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
x=int(input("year"))
if x%4==0:

    if x%100==0:
        if x%400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")

else:
    print("no leap year")