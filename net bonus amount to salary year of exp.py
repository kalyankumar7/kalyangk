''' A company gives bouns to employee

 time period of service      bouns
 -----------------------    --------
 more then 10 years           10%
 >=6 and <=10 years            8%
 less then 6 years             5%

 calculate net bonus amount'''

salary=float(input("enter your salary amount: "))
exp= float(input("enter your experiences: "))

if(exp>10):
    bouns=salary*0.1
    print("the net bouns amount is: ",bouns)
elif(exp>=6 and exp<=10):
    bouns=salary*0.08
    print("the net bonus amount is: ",bonus)
else:
    bonus=salary*0.05
    print("the net bonus amount is: ",bouns)
