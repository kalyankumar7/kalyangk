''' Prime factor '''

n = int(input( "enter any number: "))
fact = 2

while(fact <=n):
    if(n%fact ==0):
        print(fact,end="*")
        n =n/fact
    else:
        fact = fact + 1
