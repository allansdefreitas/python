#Transforming Code:  to Python (STARTING)

# Start of main code -------------------------------------------------------------------------##########################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics.pairwise import euclidean_distances

# MFEAT-KAR -----------------------------------------------------------------------------#############
dados_kar = pd.read_csv('C:/datasets/mfeat-kar', delimiter='\s+', header=None)

numLinhas_kar = dados_kar.shape[0]
numColunas_kar = dados_kar.shape[1]
 
#Normalizando com média 0 e desvio padrão 1
dados_kar_normalizados = preprocessing.scale(dados_kar)
dados_kar_normalizados

# Calcula a distância euclidiana para o numero de colunas (64)
matrizDistanciaEucKar = euclidean_distances(dados_kar_normalizados, dados_kar_normalizados)

# MFEAT-FOU -----------------------------------------------------------------------------#############

dados_fou = pd.read_csv('C:/datasets/mfeat-fou', delimiter='\s+', header=None)

numLinhas_fou = dados_fou.shape[0]
numColunas_fou = dados_fou.shape[1]

#Normalizando com média 0 e desvio padrão 1
dados_fou_normalizados = preprocessing.scale(dados_fou)
dados_fou_normalizados

# Calcula a distância euclidiana para o numero de colunas
matrizDistanciaEucFou = euclidean_distances(dados_fou_normalizados, dados_fou_normalizados)

# MFEAT-FAC -----------------------------------------------------------------------------#############

dados_fac = pd.read_csv('C:/datasets/mfeat-fac', delimiter='\s+', header=None)

numLinhas_fac = dados_fou.shape[0]
numColunas_fac = dados_fou.shape[1]

#Normalizando com média 0 e desvio padrão 1
dados_fac_normalizados = preprocessing.scale(dados_fac)
dados_fac_normalizados

# Calcula a distância euclidiana para o numero de colunas (76)
matrizDistanciaEucFac = euclidean_distances(dados_fac_normalizados, dados_fac_normalizados)


#/ End of main code --------------------------------------------------------------------------------------######

# -------------------------- INICIALIZADOR DA MATRIZ DE MEDOIDS ------------------------->

# Inicializa uma matriz de medoids de tamanho [KxP], com o valor da ultima linha de cada classe
def inicializaMatrizMedoids(quantidadeGrupos, quantidadeMatrizesDissimilaridades):
    matrizMedoids = np.zeros((quantidadeGrupos, quantidadeMatrizesDissimilaridades)) # U

    for i in range(quantidadeGrupos) :
        for j in range(quantidadeMatrizesDissimilaridades):
            matrizMedoids[i, j] = i*200
  
    return matrizMedoids
# ---------------------------------- FIM INICIALIZADOR ---------------------------------->

# --------------------------- INICIALIZADOR DA MATRIZ DE PESOS -------------------------->

# Inicializa uma matriz de pesos de tamanho [KxP], com o valor unitário 
def inicializaMatrizPesos(quantidadeGrupos, quantidadeMatrizDissimilaridade):
  matrizPesos = np.full((quantidadeGrupos, quantidadeMatrizDissimilaridade), 1)
  
  return matrizPeso

# ------------------------------- FIM INICIALIZADOR PESOS ------------------------------->

# --------------------------------------------------------------------------------------->

def retornaMatrizDistancia(posicao):
  listaMatrizes = np.array([matrizDistanciaEucKar, matrizDistanciaEucFac, matrizDistanciaEucFou])
  
  return(listaMatrizes[posicao])

# --------------------------------------------------------------------------------------->

# ----------------------------------------------------------------------------------------------------------------------------->

def distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, vetorPesosRelevancia, vetorMedoids, posicaoVetorDados):
    
    distanciaFinal = np.zeros(quantidadeMatrizDissimilaridade)
    
    # Somatório j=1..p
    for j in range(quantidadeMatrizDissimilaridade):
        distanciaFinal[j] = vetorPesosRelevancia[j] * retornaMatrizDistancia(j)[posicaoVetorDados, vetorMedoids[j]]

    return np.sum(distanciaFinal)

def funcaoCriterio(quantidadeMatrizDissimilaridade, quantidadeClusters, matrizGrauAssociacao, matrizPesosRelevantes, dados, matrizMedoids, m):
    # Somátorio k=1..K
    medidaAdequacao = np.zeros(quantidadeClusters)
    numeroLinhas = len(dados)

    # Poderia ser utilizado np.power(matrizGrauassociacao, m)
    # porém 30x mais lento...
    matrizGrauAssociacao = matrizGrauAssociacao**m

    for k in range(quantidadeClusters):
    
        # Somatório i=1..n
        somatorioLinhas = np.zeros(numeroLinhas)

        for i in range(numeroLinhas):
            somatorioLinhas[i] = matrizGrauAssociacao[i, k] * distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesosRelevantes[k, :], matrizMedoids[k, :], i)
        
        # O index 600 do somatorioLinhas possui o falor NaN (que quebra o somatório), por isso, utilizando o na.rm = TRUE
        medidaAdequacao[k] = np.sum(somatorioLinhas)
    
  
    return np.sum(medidaAdequacao)
# FIM FUNÇÃO DE CRITÉRIO -> J(G, A, U) ------------------------------------------------------------------------------------------------------->

# FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g ------------------------------------------------------------------------------------------------>

def calculaMatrizMedoids(matrizGrauAssociacao, dados, m, quantidadeClusters, quantidadeMatrizDissimilaridade):
    # Somatório i=1...n
    matrizMedoids = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
    numeroLinhas = len(dados)

    matrizGrauAssociacao = matrizGrauAssociacao**m

    for k in range(quantidadeClusters):
        vetorMedoids = np.zeros(quantidadeMatrizDissimilaridade)

        for j in range(quantidadeMatrizDissimilaridade):
            matrizMultiplicacoes = matrizGrauAssociacao[:, k] * retornaMatrizDistancia(j)
            # Realiza a soma de todas as linhas de uma coluna
            arraySomatorios = matrizMultiplicacoes.sum(axis=0)
            # Retorna o index do conjunto de dados cujo somatorio do produto do matrizGrauAssociacao pela distancia sejao mínimo
            vetorMedoids[j] = np.amin(arraySomatorios)

        matrizMedoids[k, :] = vetorMedoids

    return matrizMedoids
# FIM FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g -------------------------------------------------------------------------------------------->

# FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ----------------------------------------------------------------------------------------->

def calculaMatrizRelevancia(quantidadeClusters, quantidadeMatrizDissimilaridade, dados, matrizGrauAssociacao, m, matrizMedoids):
    matrizRelevancia = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
    matrizGrauAssociacao = matrizGrauAssociacao**m
  
    for k in range(quantidadeClusters):
    
        vetorRelevancias = np.zeros(quantidadeMatrizDissimilaridade)
    
        for j in range(quantidadeMatrizDissimilaridade):
      
            somatorioSuperior = np.zeros(quantidadeMatrizDissimilaridade)
            somatorioInferior = 0
      
            vetorMultiplicacoesInferior = matrizGrauAssociacao[:, k] * retornaMatrizDistancia(j)[:, matrizMedoids[k, j]] 
            somatorioInferior = np.sum(vetorMultiplicacoesInferior)
      
            # Produtório 1...p
            for h in range(quantidadeMatrizDissimilaridade):

                vetorMultiplicacoesSuperior = matrizGrauAssociacao[:, k] * retornaMatrizDistancia(h)[:, matrizMedoids[k, h]]
                somatorioSuperior[h] = np.sum(vetorMultiplicacoesSuperior)
            
            vetorRelevancias[j] = ( np.prod(somatorioSuperior) ^ (1/quantidadeMatrizDissimilaridade) ) / (np.sum(somatorioInferior))
    
        matrizRelevancia[k, :] = vetorRelevancias
    
    return matrizRelevancia

# FIM FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ------------------------------------------------------------------------------------->



# FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u ------------------------------------------------------------------------------------------------->

def calculaMatrizGrauAssociacao(dados, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesos, matrizMedoids, m):
    numeroLinhas = len(dados)
    matrizGrauAssociacao = np.zeros((numeroLinhas, quantidadeClusters))
  
    for i in range(numeroLinhas):
    
        vetorGrauAssociacao = np.zeros(quantidadeClusters)
    
        for k in range(quantidadeClusters):
      
            valorGrauAssociacao = np.zeros(quantidadeClusters)
            distanciaSuperior = distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesos[k, :], matrizMedoids[k, :], i)
      
            for h in range(quantidadeClusters):
                distanciaInferior = distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesos[h, :], matrizMedoids[h, :], i)

                valorGrauAssociacao[h] = (distanciaSuperior/distanciaInferior) ^ 1/(m-1)
            
            vetorGrauAssociacao[k] = ( 1/(np.sum(valorGrauAssociacao)) )
        
        matrizGrauAssociacao[i, :] = vetorGrauAssociacao
  
    return matrizGrauAssociacao

# FIM FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u --------------------------------------------------------------------------------------------->

# -------------------------------------- ALGORITMO -------------------------------------->
quantidadeClusters = 10 # K
quantidadeMatrizDissimilaridade = 3
m = 1.6 # m
iterationLimit = 150 # T
diferencaMedoids = 10 ^ (-10) 

matrizMedoidsFinal = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
matrizPesosFinal = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
matrizGrauAssociacaoFinal = np.zeros((len(retornaMatrizDistancia(1)), quantidadeClusters))
adequacaoAtual = 1
adequacaoAnterior = 0

# Initialization
for t in range(iterationLimit):
  
    if t == 1:
        matrizMedoidsFinal = inicializaMatrizMedoids(quantidadeClusters, quantidadeMatrizDissimilaridade)
        matrizPesosFinal = inicializaMatrizPesos(quantidadeClusters, quantidadeMatrizDissimilaridade)
        # Estou passando dados_kar_normalizados, mas só utilizará para capturar o número de linhas (2000) que é padrão para todos
        matrizGrauAssociacaoFinal = calculaMatrizGrauAssociacao(dados_kar_normalizados, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
    else:
    
        matrizMedoidsFinal = calculaMatrizMedoids(matrizGrauAssociacaoFinal, dados_kar_normalizados, m, quantidadeClusters, quantidadeMatrizDissimilaridade)
        # print('Matriz Medoids -------------------------->')
        # print(matrizMedoidsFinal)

        matrizPesosFinal = calculaMatrizRelevancia(quantidadeClusters, quantidadeMatrizDissimilaridade, dados_kar_normalizados, matrizGrauAssociacaoFinal, m, matrizMedoidsFinal)
        matrizPesoAntiga = matrizPesosFinal
        # print('Matriz Pesos -------------------------->')
        # print(matrizPesosFinal)

        # prod(matrizPesosFinal[10, ])

        matrizGrauAssociacaoFinal = calculaMatrizGrauAssociacao(dados_kar_normalizados, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
        # print('Matriz Associação -------------------------->')
        # print(matrizGrauAssociacaoFinal)

        # sum(matrizGrauAssociacaoFinal[2, ]) 
    
  
    adequacaoAtual = funcaoCriterio(quantidadeMatrizDissimilaridade, quantidadeClusters, matrizGrauAssociacaoFinal, matrizPesosFinal, dados_kar_normalizados, matrizMedoidsFinal)

    # print('Adequação Atual -------------------------->')
    # print(adequacaoAtual)

    # print('Adequacao Anterior -------------------------->')
    # print(adequacaoAnterior)

    if abs(adequacaoAtual - adequacaoAnterior) < diferencaMedoids:
        break
    else:
        adequacaoAnterior = adequacaoAtual
        adequacaoAtual = 1

# ------------------------------------ FIM ALGORITMO ------------------------------------>