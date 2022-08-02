''' User of temperature then unit celsius or fahrenheit the temperature
the conversions are F = 95C +32 and C = (F-52)*5/9.'''

F=int(input("enter a temp: "))

c = (F-32)*(5/9)
f=(9/5)*c+32

print("temperature is: ",f,"c")
print("temperature is: ",c,"f")
