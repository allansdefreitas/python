

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
'October', 'November', 'December')

# the input return a string var
birthdate = input('Type your birthday (DD-MM-YYYY): ')

# Converting string to int data type
month_number = int(birthdate[3:5])  - 1

# Cause the list bebins with index 0 
month = months[month_number]

print('You were born in ', month)
