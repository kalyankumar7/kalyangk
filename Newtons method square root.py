'''
Newton's method to computer display the square root of a number.
the algorithm of newton's method following
1. Read x from the user.
2. Initialize guess to x/2.
3. "While"guess to not good enough do.
4. update to be the average of guess and x/guess.
    guess contains in approximation of the squere root of x.
    the absolute value of the difference b/w guess*guess and x was less then or equal to 10e-12
    '''

x = int(input("enter any number: "))
guss = x/2

while ((guess**2)-(x)) >= 10e-12:
    guess = (guess + x/guess)/2
print("the squere root of ",x,"is",guess)    
