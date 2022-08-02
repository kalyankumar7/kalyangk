'''write a program to print numbers which are divisible by 4 but not divisible
by 8 consider the b/w 1 to 100'''

num=int(input("enter any number: "))
for i in range(1,101):
 if(i%4==0) and (i%8!=0):
    print(i)
