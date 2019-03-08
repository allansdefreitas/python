x = 0
# list
persons = []


# while x < 4:

#     name = input('name, please: ')
#     persons.append(name)
#     print(persons)
#     x += 1

# Enquanto joão não fizer parte da lista persons

# while 'joao' not in persons:
#     name = input('name, please: ')

#     if(name == 'joao'):
#         #próxima iteração do loop
#         continue
#     persons.append(name)
#     print(persons)
#     x += 1
  
while x < 4:
    name = input('name, please: ')
    
    if(name == 'joao'):
        #próxima iteração do loop: não conta com João
        continue
    persons.append(name)
    print(persons)
    x += 1
