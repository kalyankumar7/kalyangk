''' A Triangle has three sides
    A Equilateral triangle is all side are equal.
    A Scalene triangle is three side are unequal.
    A isosceles triangle is two side is equal another on side is different.'''

x=int(input("enter x value: "))
y=int(input("enter y value: "))
z=int(input("enter z value: "))

if x==y and y==z:
    print("this is a equilateral triangle")
elif x==y or y==z or z==x:
    print("this is a isosceles triangle")
else:
    print("triangle is scalane")
