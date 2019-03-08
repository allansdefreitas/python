cassio = {'nome': 'Cassio', 'cursos': ['Música', 'Computação'], 'idade': 25}

#print(cassio)

for x in cassio:
    print (x, ' :' ,cassio[x])

print(cassio.get('nome', '404 - NOT FOUND'))
print(cassio.get('sobrenome', '404 - NOT FOUND'))

cassio['nome'] = 'Cassio Santos'

print(cassio)

cassio['cursos'].append('Eletricidade')

print(cassio)
