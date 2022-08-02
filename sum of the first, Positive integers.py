#Project 7 sum of the first, Positive integers
'''Write a program that reads a positive integer,n. from the user and then
displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula.

      (n)(n+1)
sum= ----------
         2          formula'''
n=int(input("enter n value: "))
sum1=n*(n+1)/2
print("the sum of n numbers is",sum1)
