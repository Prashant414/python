# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) anx=float(input("number of clases held"))
x=float(input("number of clases held"))
a=float(input("number of classes attend"))
m=input("any medical issue type y or n")
z=a/x*100

if z<=75:
    if m=='y':
        print("allowed")
    else:
        print("not allowed")

else:
    print("allowed")
