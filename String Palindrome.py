''' string palindrone to identical foeward and backward
    "anna","civic","level" and "hannah" is a palindrome words. '''

name = str(input(" enter a name: "))

rstr = name[::-1]

if name == rstr:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
