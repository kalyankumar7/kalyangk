#project 8 Height Units
''' Many think about there height in feet and inches. even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user followed bt a number of inches. Once these values are real. your program
should compute and display the equivalent number of centimeters.

Hint: One foot is 12 inches.One inche is 2.54 centimeters'''

feet=int(input("enter height in feet: "))
inc=int(input("enter height in inches: "))
feet_cm=feet*12*2.54
inc_cm=inc*2.54
height_cm=feet_cm+inc_cm
print("your height in cm is",height_cm)
