

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
