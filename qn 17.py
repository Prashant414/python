# Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
x = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for y in x:
    if y>150 :
        break
    elif y%5==0:
        print(y)
