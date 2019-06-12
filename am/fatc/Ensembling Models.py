import pandas as pd
import numpy as np
import numpy as np
from sklearn.naive_bayes import GaussianNB

#TREINAR GAUSS1,GAUSS2 e GAUSS3 COM View1, View2 E View3
# combinar os Gauss pela regra da soma

def gaussCombinadoSoma(exemploIndex):
#exemploIndex é o índice da linha

#array[10]

#i= 0...9:
#    array[i] = priori(i) +  ( Gauss1, post(i)) + ( Gauss2, post(i)) + ( Gauss3, post(i))

#pega o máximo de array[]
#o índice será a classe escolhida

#   GaussClf1.predict_proba(X)[indiceLinhaExemplo, classe]

#Pegar priori de cada classe:
    #clf.class_prior_[0]...
#pegar posteriori:
    #clf.predict_proba(X)
        #clf.predict_proba(X)[0,0] exemplo 0 classe 0 

#aplicar regra, se não tiver método que o faça

    # para armazenar a priori + posterioris de cada classe
    arrayPosterioriClasses = np.zeros(10)

    #para cada classe: SÓ TEM 9 CLASSES, PROBLEMA DO CRISP
    for i in range(9): # tem que ser 10
        priori = GaussClf1.class_prior_[i]
        arrayPosterioriClasses[i] =  priori + ( GaussClf1.predict_proba(X_view1_fac)[exemploIndex, i] ) + ( GaussClf2.predict_proba(X_view2_fou)[exemploIndex, i] ) + ( GaussClf3.predict_proba(X_view3_kar)[exemploIndex, i] )
        #print(i)
    #índice do máximo é a classe escolhida (0 - 9)
    classeEscolhida = np.argmax(arrayPosterioriClasses)
    return classeEscolhida


"""Pegando os dados de treinamento de fac - CRISP ------------------------------------------------------------"""
X_fac_original = pd.read_csv('datasets/mfeat-fac-crisp.csv', delimiter =',', header=None)

#Pega todas as linhas de todos os exemplos até a coluna 216 (exclusive) . Na prática (o que se quer) pega até a coluna 215
#Esses são nossos dados sem a rotulação de classes (label)
X_view1_fac = X_fac_original.iloc[:, 0: 216].get_values() # retorna como uma matriz e não como dataframe 

#Pega a última coluna com todas suas linhas. Isso será nosso array de TRUE LABEL, com a marcação correta das classes
y_view1_fac = X_fac_original.iloc[:, 216].get_values()

#Naive Bayes Classifier
GaussClf1 = GaussianNB()

#dados de treino x com os true labels de y para TREINAR
GaussClf1.fit(X_view1_fac, y_view1_fac)

print("score do gauss1: ", GaussClf1.score(X_view1_fac, y_view1_fac))


"""Pegando os dados de treinamento de FOU - CRISP ------------------------------------------------------------"""
X_fou_original = pd.read_csv('datasets/mfeat-fou-crisp.csv', delimiter =',', header=None)

#Esses são nossos dados sem a rotulação de classes (label)
X_view2_fou = X_fou_original.iloc[:, 0: 76].get_values() # retorna como uma matriz e não como dataframe 

#Pega a última coluna com todas suas linhas. Isso será nosso array de TRUE LABEL, com a marcação correta das classes
y_view2_fou = X_fou_original.iloc[:, 76].get_values()

#Naive Bayes Classifier
GaussClf2 = GaussianNB()

#dados de treino x com os true labels de y para TREINAR
GaussClf2.fit(X_view2_fou, y_view2_fou)
print("score do gauss2: ", GaussClf2.score(X_view2_fou, y_view2_fou))

"""Pegando os dados de treinamento de KAR - CRISP ------------------------------------------------------------"""
X_kar_original = pd.read_csv('datasets/mfeat-kar-crisp.csv', delimiter =',', header=None)
#print(X_kar_original.shape)

#Pega as 64 primeiras (0-63)
X_view3_kar = X_kar_original.iloc[:, 0: 64].get_values() # retorna como uma matriz e não como dataframe 

#Pega a coluna de índice 64: O true label
y_view3_kar = X_kar_original.iloc[:, 64].get_values()

#Naive Bayes Classifier
GaussClf3 = GaussianNB()

#dados de treino x com os true labels de y para TREINAR
GaussClf3.fit(X_view3_kar, y_view3_kar)
print("score do gauss3: ", GaussClf3.score(X_view3_kar, y_view3_kar))

""" Vendo os resultados do classificador combinado ---------------------------------------- """

#print([X_view1_fac[0] ])

for i in range(2000):
    #print( "Gauss 1:", GaussClf1.predict( [X_view1_fac[i] ]) )
    #print( "Gauss 2:", GaussClf2.predict( [X_view2_fou[i] ]) )
    #print("Gauss 3:", GaussClf3.predict( [X_view3_kar[i] ]) )
    
    if(GaussClf1.predict( [X_view1_fac[i] ]) != gaussCombinadoSoma(i)):
        print("Gauss combinado:", gaussCombinadoSoma(i))
        print( "Gauss 1:", GaussClf1.predict( [X_view1_fac[i] ]) )
    








""" TRASH CODE
for j = 0...10 classes
k = 0
    if(j != k)            
        para cada classe j (verifica a maior priori + posteriori ) em relação a k:
        SE a priori + posteriori j > priori + posteriori k
        k++  passa pro próximo k (próxima classe) """