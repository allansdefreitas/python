import imc as i

bmi = 0.0
result = ''
validate = False

# Validate Gender
while validate == False:

    gender = input('Gender (M | F): ')
    
    try:
        gender = gender.upper()
        if gender == 'M' or gender == 'F':
            validate = True
        else:
            print('Gender have to be M or F')
    except:
        print('Gender have to be M or F')

# Validate Weight: Number
validate = False

while validate == False:
    weight = input('Weight (Kg): ')
    try:
        weight = float(weight)
        validate = True
    except:
        print("Weight have to be a float number")

# Validate Height: Number
validate = False
while validate == False:
    height = input('Height(Cm): ')
    try:
        height = float(height)
        validate = True
    except:
        print("Height have to be a float number")
        
if gender == 'M':
    bmi = i.bmi_func(weight, height)
      
    result = i.classify_bmi_male_func(bmi)
   
    # Format bmi: 2 numbers after point
    bmi = str(bmi)
    bmi = bmi[0:4]
    
elif gender == 'F':
    bmi = i.bmi_func(weight, height)
    result = i.classify_bmi_female_func(bmi)

    # Format bmi: 2 numbers after point
    bmi = str(bmi)
    bmi = bmi[0:4]

print("The Body Mass Index (BMI) is:", bmi ,'.', result)