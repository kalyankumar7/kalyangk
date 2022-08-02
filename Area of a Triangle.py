#Project 9 Area of a Triangle
'''The area of a triangle can be computed using the following formula. Where b
is the length of the base of the triangle. and h is its height:

        b*h
area= -------
         2
 write a program that allows the user to enter values for b and h. The program
 should then compute and display the area of a triangle with base length b and height h.'''

b=int(input("enter b value: "))
h=int(input("enter h value: "))
sum1=(b*h)/2
print("the area of the triangle is",sum1)
