num=int(input('your number: '))

rem=num%2

if (num>0 and rem==0):
    print('positive even number')
if (num>0 and rem!=0):
    print('positive odd number')
if (num<0 and rem==0):
    print('negative even number')
if (num<0 and rem!=0):
    print('negative odd number')
if (num==0):
    print('its zero')