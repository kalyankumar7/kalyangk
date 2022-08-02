# Project 15 Grade using elif constructs
'''The grade of a student based on marks
   s.no       marks          Grade
    1      90 above         Excellent
    2      70 above         very good
    3      60 above         Good
    4      40 above         Average
    5      40 below         failed    '''

marks =int(input("Enter a marks: "))

if(marks>90):
     print("Excellent Grade")
elif(marks>70):
     print("very good Grade")
elif(marks>60):
     print("good Grade")
elif(marks>40):
     print("Average Grade")
else:
     print("Failed")
