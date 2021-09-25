# WRITE A PROGRAM THAT GENERATES THE SEEQUENCE 0,5,10,15,20,25..., 80

#```````````` WHILE LOOP```````````````
num = int(input("ENTER THE END NUMBER: "))
i = 0
while (i<=num):
    print(i)
    i += 5

# alternate

num1 = int(input("ENTER THE END NUMBER: "))
for x in range(0, num1, 5):
    print(x)
    x+=5
print(num1)
