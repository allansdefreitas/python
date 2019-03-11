import random

def megasena():
    lista = []
    while len(lista) < 6:
        num = random.randint(1,60)

        # Não podem ser números repetidos
        if num in lista:
            continue   
        else:
            lista.append(num)
    
    print(sorted(lista))


#megasena()

alunos = ['Cassio', 'Etinho', 'Mayara', 'Sabrina']
print(random.choice(alunos))
#sortear x alunos
print(random.sample(alunos, 2))

megasena()