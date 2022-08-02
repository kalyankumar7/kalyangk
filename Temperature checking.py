''' To enter temperature in celsius
 1. Temperature less then -273.15 is invalid.
 2. Temperature exactly -273.15 is absolute 0.
 3. Temperature is b/w -273.15 to 0 is freezing.
 4. Temperature is 0 is freezing point
 5. Temperature is b/w 0 to 100 is normal range.
 6. Temperature is 100 is boiling point.
 7. Temperature is a above 100 is above the boiling point. '''

c=float(input("enter a temperature in celsius is: "))
if(c < -273.15):
     print("temperature is invalid")
elif(c == -273.15):
     print("temperature is absolute")
elif(c >= -273.15 and c < 0):
     print("temperature is frezzing")
elif(c == 0):
     print("temperature is frezzing point")
elif(c >= 0and c < 100):
     print("temperature is normal raqnge")
elif(c == 100):
     print("temperature is boiling point")
else:
     print("temperature is above the boiling point")
