# WRITE A PROGRAM THAT PRINTS THE FIRST 100 MEMBERS OF THE SEQUENCE
#2, -3, 4, -5, 6
"""
for i in range(1, 100):
    x = 2
    print(x)
    y = -3
    print(y)
    x+=2
    print(x)
    y-=2
    print(y)
    
while (i<100): 
    x = 2
    print(x)
    y = -3
    print(y)
    x+=2
    print(x)
    y-=2
    print(y)
    i+=1
"""
num1 = int(input("FIRST NUMBER: "))
num2 = int(input("SECOND NUMBE: "))
print(num1)
print(num2)
count = 0
while(count<95):
    num1+=2
    num2-=2
    print(num1)
    print(num2)
    count+=1