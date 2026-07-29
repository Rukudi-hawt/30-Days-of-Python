Age = int(input("Your age is: ", ))
if Age >= 18:
     print('You are old enough to drive, buddy!')
else:
     print('You are not old enough to drive, kid. You need', 18 - Age,' more years to drive.')

Asabaneh_Age = 25
Your_Age = int(input('Your age is: ', ))
if Asabaneh_Age > Your_Age:
     print('You are', Asabaneh_Age - Your_Age, 'years younger than Asabaneh.')
elif Your_Age == Asabaneh_Age:
     print('Ypu and Asabaneh are the same age.')
elif Asabaneh_Age < Your_Age:
     print('You are', Your_Age - Asabaneh_Age, 'years older than Asabaneh.')
