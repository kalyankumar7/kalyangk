''' Least common multiple'''

a=int(input("enter first number is: "))
b=int(input("enter second number is: "))

if a>b:
    i = a
else:
    i = b
while(true):
    if(i%a==0 and i%b==0):
        print(i)
        break
    i = i + 1

 print("the least common multiple number is: ",i)   
