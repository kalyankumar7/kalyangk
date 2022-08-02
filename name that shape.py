'''the name of a shape from its number of side the support shapes with anywhere
from 3 up to (and includes)10 sides.'''

num=int(input("enter a number:"))
if(num==3):
    print("this is a triangle")
elif(num==4):
    print("this is a square")
elif(num==5):
    print("this is a pentagonal")
elif(num==6):
    print("this is a hexgonal")
else:
    print("error")
