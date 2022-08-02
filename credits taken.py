'''user take how many credits they have taken.
 1. Freshman tsken 23 or less
 2. Sophamore taken b\w 24 and 53
 3. Juniors is taken b\w 54 to 83
 4. Seniors is taken b\w 84 and over'''

credit=int(input("enter how many credits are taken: "))
        
if(credit<=23):
    print("the student is a fresher")
elif(credit>=24 and credit<=53):
    print("the student is a sophamore")
elif(credit>=54 and credit<=83):
    print("the student is a junior")
else:
    print("they are seniors")
