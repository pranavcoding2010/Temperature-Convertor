temp=float (input ('Enter the temperature in celsius'))
fahrenheit=(temp*1.8)+32
print('%0.1f degree celsius is = %0.1f degree fahrenheit'%(temp,fahrenheit))
if (fahrenheit>=104):
    print('its too hot')
elif (fahrenheit<=50):
    print('ist too cold')
else : 
    print('temperature is good')