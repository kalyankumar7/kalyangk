#Fizz-Buzz
'''if the players number is divisible by 3 then the player says fizz instead of their number.
if the players number is divisible by 5 then the player says buzz instead of their number.'''
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print("eliminated")
