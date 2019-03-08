# Calcular media de estudante, faltas e dar resultado
# 70% frequencia e media >= 6
#resutados: reprovado por media e falta, por falta, por media, aprovado
# imprimir nome, media, porcentual e resultado


# Validação:
    # Nunca interromper por erro
    # nota entre 0  e 10 (inclusive)
    # número de faltas entre 0 e 20 (inclusive)

total_classes = 20
approved = False
valid = False

print('Student data ---------------------\n')
name = input('Name: ')

# input grade 1 (validation) -----------------------
while valid == False:
    grade_test1 = input('Test 1 (grade): ') 
    try:
        
        # validation 1: Try convert to float
        grade_test1 = float(grade_test1)

        # validation 2: is it a number?
        if (grade_test1 >= 0 and grade_test1 <= 10):
            valid = True
        else:
            print("Grade have to be between 0 and 10")
    except:
        print("Grade have to be a number separeted by '.' ")

# Lets validate second grade!
valid = False

# input grade 2 (validation) -----------------
while valid == False:
    grade_test2 = input('Test 2 (grade): ') 
    try:
        
        # validation 1: Try convert to float
        grade_test2 = float(grade_test2)

        # validation 2: is it a number?
        if (grade_test2 >= 0 and grade_test2 <= 10):
            valid = True
        else:
            print("Grade have to be between 0 and 10")
    except:
        print("Grade have to be a number separeted by '.'")
        
# Lets validate absences!
valid = False

# Input Absences -----------------
while valid == False:
    absences = input('Absences: ')
    try:
        # Try convert: is it a number value?
        absences = int(absences)
        # Verify the interval
        if( absences >= 0 and absences <= 20):
           valid = True
        else:
            print("Absences have to be between 0 and 20")
    except:
        print("Absences have to be a integer number")

# percentual de aulas que compareceu
frequency_classes = ( (total_classes - absences)/total_classes ) *100

#média
grades_avg = (grade_test1 + grade_test2) / 2

result = ''

# atingiu a frequência de 70%?
if frequency_classes >= 70:
   
    if grades_avg >= 6.0:
        result = 'Approved'
    else:
        result = 'Disapproved for grade'

elif grades_avg < 6.0:
    result ='Disapproved for grade and absence'
else: 
   result = 'Disapproved for absence'


print('Results ----------------------------')
print('Name:', name)
print('Grade average:', grades_avg)
print('Frequency:', frequency_classes, '%')
print('Result:', result)
