import math as m
import time as t

sales = [200, 300, 500]

# somatório dos valores da lista
print(m.fsum(sales))

#imprimir hora local
print(t.localtime())

#obter a hora
hora = t.localtime().tm_hour

#obter os minutos
minuto = t.localtime().tm_min

#conversão para string
hora = str(hora)
minuto = str(minuto)

print("transacao concluida as "+ hora +'h'+ minuto+'min')

## tempo para digitar o nome: time.clock() não esta disponível mais
## em vez dela, usar .perf_counter() ou time.time(), por exemplo
def count_time():
    begin = t.perf_counter()
    input('Type your name: ')
    end = t.perf_counter()
    time_secs = end - begin

    #Fixando a quantidade de casas decimais (digitos pós ponto)
    return round(time_secs, 2)

    
print( str(count_time()) + ' segundos para digitar seu nome')


