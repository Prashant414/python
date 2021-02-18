# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
x=float(input("number of clases held"))
y=float(input("number of classes attend"))
z=y/x*100
if z<75:
    print("not allowed to sit")
else:
    print("allowed")
