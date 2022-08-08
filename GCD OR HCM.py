'''Greastest common divisor'''

n = int(input("enter a number1 is: "))
m = int(input("enter a number2 is: "))
x = min(n,m)
 hcf =0

 for i in range(1,x+1):
     if n%i ==0 and m%i ==0:
         hfc = i
 print("the Greatest common dividion is: ",hcf)
