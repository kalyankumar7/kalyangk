'''
 print value of the number in which are divisible by 4 but not divisible by 8

 '''

n=int(input(" enter any number: "))
for i in range(1,n+1):
    if(i%4==0 and i%8!=0):
     print(i)
