import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [100, 200, 167, 400, 640]

## Gerar grafico
plt.plot(x, y)

# Exibir grafico
plt.show()

# Com legenda ------

legenda = ['Janeiro', 'Fevereiro', 'Marco', 'Abri', 'Maio']
## para cada elemento da lista x...
#  substituir pelo elemento correpondente/respectivo na lista de legendas
plt.xticks(x, legenda)

plt.plot(x,y)
plt.show()