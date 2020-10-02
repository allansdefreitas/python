age = int(input('Type your age: '))
gender = input('Type your gender (M or F): ').lower()
city = input ('Type your hometown: ')

if city == 'Recife' or city == 'Olinda':

    if gender == 'm':
        if age >= 18:
            print ('Adult man')
        else:
            print('Man child: boy')
    elif gender == 'f':
        if age >= 18:
            print('Adult woman')
        else:
            print ('Woman child: girl')
    else:
        print('please, type a valid gender (M or F)')

else:
    print('You is not from authorized cities')