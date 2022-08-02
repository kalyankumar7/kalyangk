#Project 16 Vowel or Consonant
'''In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a,e,i,o or u then your program should display a message
indicating that the entered letteris a vowel. If the user enters Y then your program
should display a message indicating that sometimes y is a vowel. and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.'''

alp= str(input("enter a Alphabet: "))

if(alp=='a')or(alp=='e')or(alp=='i')or(alp=='o')or(alp=='u'):
    print("this is a vowel Alphabet.")
else:
    print("Error.")
