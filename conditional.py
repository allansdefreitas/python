idade = int (input('type your age, please: '))

if idade >= 16 or idade >= 65:
    print('YOU CAN VOTE, NOT REQUIRED')
    print('this is your right')
    
elif idade < 16:
    print ('You cant vote YET')
else: 
    print('YOU CANT VOTE')