#project 5 :Bottle Deposite
'''In many jurisdictions a small deposite is added to drink containers to encourage people
to recycle them. In one particular jurisdication. drink containers holding one liter
or less have a $0.10 deposite. and drink containeras bolding more then oneliter have a $0.25 deposit.
   write a program that reads the number of containers of each size from the user. your program should
 continue by computing and displaying the refund that will be received for returning those continues.
 Format the output so that it includes a dollar sigh and two digits to the right of the decimal point'''
bottles_above_lit=int(input("enter the no of bottles(above lit): "))
bottles_below_lit=int(input("enter the no of bottles(below lit): "))
refund=(bottles_above_lit*0.25)+(bottles_below_lit*0.1)
print("the total refund amount=",refund,"$")
