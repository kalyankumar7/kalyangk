''' the no of days from user & calculate the charges for library

       number of days         charges
      ----------------       ---------
      Till 5 days            rs 2/day
      6 to 10days            rs 3/day
      11 to 15days           rs 4/day
      after 15days           rs 5/day'''

days = int(input("enter days: "))
if(days<5):
    bill=days*2
    print("the charges for library is: ",bill)
elif(days>=6 and days<=10):
    bill=days*3
    print("the charges for library is: ",bill)
elif(days>=11 and days<=15):
    bill=days*4
    print("the charges for library is: ",bill)
else:
    bill=days*5
    print("the charges for library is: ",bill)
