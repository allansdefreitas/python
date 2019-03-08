# Calcular media de estudante, faltas e dar resultado
# 70% frequencia e media >= 6
#resutados: reprovado por media e falta, por falta, por media, aprovado
# imprimir nome, media, porcentual e resultado

total_classes = 20
approved = False

print('Student data ---------------------\n')
name = input('Name: ')
grade_test1 = float( input('Test 1 (grade): ') )
grade_test2 = float( input('Test 1 (grade): ') )
absences = int ( input('Absences: '))

# total de aulas que compareceu
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
