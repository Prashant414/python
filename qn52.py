

a,b,c=0,0,0


s = input('enter the no .')
z = s.split(sep=",")
print(z)
y = z[0]
for y in z:



    if int(y)> 0:
        a = a + 1
    elif int (y)< 0:
        b = b + 1
    elif int(y) == 0:
        c = c + 1
print ("positive",a,"negative",b,"zero",c)

