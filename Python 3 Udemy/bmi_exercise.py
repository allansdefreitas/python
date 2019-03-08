def bmi_func(weight, height):
    return ( weight / (height * height) * 10000)

#show condition from bmi value (for men)
def classify_bmi_male_func(bmi):
    if bmi < 20.7:
        result = 'under weight'
    elif bmi >= 20.7 and bmi <= 26.4:
        result = 'normal weight'
    elif bmi >= 26.4 and bmi <= 27.8:
        result = 'a little overweight'
    elif bmi > 27.8 and bmi <= 31.1:
        result = 'overweight'
    elif bmi > 31.1:
        result = 'obese'

    return result

#show condition from bmi value (for women)
def classify_bmi_female_func(bmi):
    if bmi < 19.1:
        result = 'under weight'
    elif bmi >= 19.1 and bmi <= 25.8:
        result = 'normal weight'
    elif bmi >= 25.8 and bmi <= 27.3:
        result = 'a little overweight'
    elif bmi > 27.3 and bmi <= 32.3:
        result = 'overweight'
    elif bmi > 32.3:
        result = 'obese'
    
    return result

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
    bmi = bmi_func(weight, height)
      
    result = classify_bmi_male_func(bmi)
   
    # Format bmi: 2 numbers after point
    bmi = str(bmi)
    bmi = bmi[0:4]
    
elif gender == 'F':
    bmi = bmi_func(weight, height)
    result = classify_bmi_female_func(bmi)

    # Format bmi: 2 numbers after point
    bmi = str(bmi)
    bmi = bmi[0:4]

print("The Body Mass Index (BMI) is:", bmi ,'.', result)