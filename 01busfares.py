age = int(input('Please enter your age:'))
bc = 0.75
bc1 = 0.50
bc2 = 0.75

if age <= 5:
    print('You go free!')

elif (age >= 5 and age <= 16):
    print('Your fare is:' + ' ' +  str(bc) + ' ' + 'euro.')

elif (age >= 17 and age <= 20):
    print('Your fare is:' + ' ' +  str(bc + bc1) + ' ' +  'euro.')

elif (age >= 21 and age <= 64):
    print('Your fare is:' + ' ' +  str(bc + bc2) + ' ' + 'euro.')

else:
    print('You go free!')
