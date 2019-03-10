# usar o Time (built in) e o Matplot lib (externo)
# Digitar uma palavra 5 vezes seguidas
# contar o tempo de digitação de cada
#gerar um gŕafico em linha (x , y) com a duração de digitação de cada palavra

import time as t
import matplotlib.pyplot as plt

def countTime():

    begin = t.time()
    word = input("Type any word: ")
    end = t.time()
    # obtendo diferença de tempo e definindo como 2 casas decimais
    totalTime = (end - begin)
    totalTime = round(totalTime, 2)
    return totalTime

def generateGraphicMatPlot (timesList):
    elementsX = [1,2,3,4,5]
    elementsLegendsX = ['word 1','word 2','word 3','word 4','word 4']

    # Associando os respectivos elementos de elementsX com as legendas de elementsLegendX 
    plt.xticks(elementsX, elementsLegendsX)

    # Generate the graphic
    plt.plot(elementsX, timesList)
    
    # Show graphics
    plt.show()
    
i = 1
countTimeList = []
countWordsList  = []

while i <= 5:
    countTimeList.append( countTime() )
    countWordsList = i
    i+=1

#print(countTimeList)
generateGraphicMatPlot(countTimeList)