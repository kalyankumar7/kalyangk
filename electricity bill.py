units=int(input("enter the bill:"))
if units<=100:
    print("zero")
elif units>=100 and units<=200:
    bill=5*(units-100)
    print("tha total bill is",bill)
else:
    bill=10*(units-200)+5*(100)
    print("tha total bill is",bill)
