user = "Cassio"

def showGreeting(name):
    print("Good Night, "+name+"!")


showGreeting(user)


def bmi(weight, height):
    return ( weight / (height * height) * 10000)
    

print (bmi(65, 177))