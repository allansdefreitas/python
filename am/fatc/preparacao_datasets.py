#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn import preprocessing
import csv

listaMatrizes = np.array([])

def distancia(a,b):
    """ retorna a distância euclideana entre dois vetores
    :param a: np.ndarray
    :param b: np.ndarray
    :return: float
    """

    tmp = a - b
    soma_quadrados = np.dot(tmp, tmp) # preferiu-se o desempenho em detrimento do rigor algébrico,
                                      # razão pela qual não foi passada a transposta de tmp
                                      # em nenhum dos parâmetros da função np.dot.
    result = np.sqrt(soma_quadrados)
    return result

def main():

    datasets = ['http://archive.ics.uci.edu/ml/machine-learning-databases/mfeat/mfeat-fac', 'http://archive.ics.uci.edu/ml/machine-learning-databases/mfeat/mfeat-fou', 'http://archive.ics.uci.edu/ml/machine-learning-databases/mfeat/mfeat-kar']
    
    for dataset_number in range(3):
        view = pd.read_csv (datasets[dataset_number],sep='\s+',header=None, dtype=np.float64)

        # Normaliza o array associado à primeira visão excluindo dos elementos a média da respectiva variável e
        # dividindo pelo desvio padrão amostral (ddof = 0)
        array_scaled = preprocessing.scale(view)
        # Após a execução da linha acima, a média de cada variável passa a ser zero e
        # o desvio padrão passa a ser 1 (um).

        # view_scaled = pd.DataFrame(data=array_scaled)

        # view.describe()
        # view_scaled.describe()

        # print distancia(array1_scaled[0,:], array1_scaled[0,:])
        # inicializa a matriz de dissimilaridade
        matriz_dissimilaridade = np.zeros((len(array_scaled),len(array_scaled)),dtype=np.float64)
        # matriz_dissimilaridade.shape

        for linha_externa in range(len(array_scaled)):
            for linha_interna in range(len(array_scaled)):
                # print "linha_interna {}".format(linha_interna)
                
                #Mexe no valor dos elementos e na diagonal principal, não faz nada
                #permanecem com zero
                if linha_externa != linha_interna:
                    #OU SEJA, se estiver ABAIXO DA DIAGONAL PRINCIPAL
                    if linha_externa > linha_interna:
                        matriz_dissimilaridade [linha_externa, linha_interna] = matriz_dissimilaridade [linha_interna, linha_externa]
                    #Se estiver ACIMA Da diagonal principal ou NELA.
                    else:
                        matriz_dissimilaridade [linha_externa, linha_interna] = distancia (array_scaled[linha_externa,:], array_scaled[linha_interna,:])
        
        #PAREI AQUI, CASA, 28/-5, 0H22
        
        view_matriz = pd.DataFrame(data=matriz_dissimilaridade)
        view_matriz.to_csv('Matriz' + str(dataset_number+1) + '.csv',index=False, header=False)
        listaMatrizes = np.append(listaMatrizes, view_matriz)

if __name__ == '__main__':
    main()



# -------------------------- INICIALIZADOR DA MATRIZ DE MEDOIDS ------------------------->

# Inicializa uma matriz de medoids de tamanho [KxP], com o valor da ultima linha de cada classe
def inicializaMatrizMedoids(quantidadeClusters, quantidadeMatrizDissimilaridade):
    matrizMedoids = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade), dtype=np.int64) # U

    for i in range(quantidadeClusters) :
        for j in range(quantidadeMatrizDissimilaridade):
            matrizMedoids[i, j] = i*200

    return matrizMedoids


# ---------------------------------- FIM INICIALIZADOR ---------------------------------->



# --------------------------- INICIALIZADOR DA MATRIZ DE PESOS -------------------------->

# Inicializa uma matriz de pesos de tamanho [KxP], com o valor unitário 
def inicializaMatrizPesos(quantidadeClusters, quantidadeMatrizDissimilaridade):
    matrizPesos = np.full((quantidadeClusters, quantidadeMatrizDissimilaridade), 1)

    return matrizPesos

# ------------------------------- FIM INICIALIZADOR PESOS ------------------------------->



# --------------------------------------------------------------------------------------->
def retornaMatrizDistancia(posicao):
    return listaMatrizes[posicao]
# --------------------------------------------------------------------------------------->


# ----------------------------------------------------------------------------------------------------------------------------->

def distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, vetorPesosRelevancia, vetorMedoids, posicaoVetorDados):
    
    distanciaFinal = np.zeros(quantidadeMatrizDissimilaridade)
    
    # Somatório j=1..p
    for j in range(quantidadeMatrizDissimilaridade):
        distanciaFinal[j] = vetorPesosRelevancia[j] * retornaMatrizDistancia(j).at[posicaoVetorDados, vetorMedoids[j]]

    return np.nansum(distanciaFinal)

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
        
        # O index 600 do somatorioLinhas possui o valor NaN (que quebra o somatório), por isso, utilizando o nansum
        medidaAdequacao[k] = np.nansum(somatorioLinhas)
  
    return np.nansum(medidaAdequacao)

# FIM FUNÇÃO DE CRITÉRIO -> J(G, A, U) ------------------------------------------------------------------------------------------------------->



# FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g ------------------------------------------------------------------------------------------------>

def calculaMatrizMedoids(matrizGrauAssociacao, dados, m, quantidadeClusters, quantidadeMatrizDissimilaridade):
    # Somatório i=1...n
    matrizMedoids = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade), dtype=np.int64)
    matrizGrauAssociacao = matrizGrauAssociacao**m

    for k in range(quantidadeClusters):
        vetorMedoids = np.zeros(quantidadeMatrizDissimilaridade)

        for j in range(quantidadeMatrizDissimilaridade):
            matrizMultiplicacoes = matrizGrauAssociacao[:, k][:, None] * retornaMatrizDistancia(j)
            # Realiza a soma de todas as linhas de uma coluna
            arraySomatorios = matrizMultiplicacoes.sum(axis=0, skipna=True)
            # Retorna o index do conjunto de dados cujo somatorio do produto do matrizGrauAssociacao pela distancia sejao mínimo
            vetorMedoids[j] = np.amin(arraySomatorios)

        matrizMedoids[k, :] = vetorMedoids

    return matrizMedoids

# FIM FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g -------------------------------------------------------------------------------------------->


# FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ----------------------------------------------------------------------------------------->

def calculaMatrizRelevancia(quantidadeClusters, quantidadeMatrizDissimilaridade, matrizGrauAssociacao, m, matrizMedoids):
    matrizRelevancia = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
    matrizGrauAssociacao = matrizGrauAssociacao**m
  
    for k in range(quantidadeClusters):
    
        vetorRelevancias = np.zeros(quantidadeMatrizDissimilaridade)
    
        for j in range(quantidadeMatrizDissimilaridade):
      
            somatorioSuperior = np.zeros(quantidadeMatrizDissimilaridade)
            somatorioInferior = 0
      
            # não se está utilizando o retornaMatrizDistancia(j).at[] pois só recebe inteiros, então não daria para fazer .at[:, ma...[k,j]] por causa dos ':'
            # poderia utilizar também o iloc[:][ma...[k, j]]
            vetorMultiplicacoesInferior = matrizGrauAssociacao[:, k] * retornaMatrizDistancia(j).loc[:, matrizMedoids[k, j]] 
            somatorioInferior = np.nansum(vetorMultiplicacoesInferior)
      
            # Produtório 1...p
            for h in range(quantidadeMatrizDissimilaridade):

                vetorMultiplicacoesSuperior = matrizGrauAssociacao[:, k] * retornaMatrizDistancia(h).loc[:, matrizMedoids[k, h]]
                somatorioSuperior[h] = np.nansum(vetorMultiplicacoesSuperior)
            
            vetorRelevancias[j] = ( np.prod(somatorioSuperior) ** (1/quantidadeMatrizDissimilaridade) ) / (np.nansum(somatorioInferior))
    
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
                distanciaInferior = np.float64(distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesos[h, :], matrizMedoids[h, :], i))
            
                if np.isclose(distanciaInferior, 0, rtol=1e-08, atol=1e-08, equal_nan=False) or abs(distanciaInferior) == 0:
                    valorGrauAssociacao[h] = 0
                else:
                    valorGrauAssociacao[h] = (distanciaSuperior/distanciaInferior) ** 1/(m-1)
            
            somatorio = np.nansum(valorGrauAssociacao)
            # Se o valor do somatório for 0 atribuiremos um valor de assoação mínimo (0.000001)
            if somatorio == 0:
                somatorio = 1000000
            
            vetorGrauAssociacao[k] = ( 1/(somatorio) )
        
        matrizGrauAssociacao[i, :] = vetorGrauAssociacao
  
    return matrizGrauAssociacao

# FIM FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u --------------------------------------------------------------------------------------------->

# -------------------------------------- ALGORITMO -------------------------------------->

def algoritmo():
    quantidadeClusters = 10
    quantidadeMatrizDissimilaridade = 3
    m = 1.6
    iterationLimit = 150
    diferencaMedoids = 10 ^ (-10)

    matrizMedoidsFinal = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade), dtype=np.int64)
    matrizPesosFinal = np.zeros((quantidadeClusters, quantidadeMatrizDissimilaridade))
    matrizGrauAssociacaoFinal = np.zeros((len(retornaMatrizDistancia(1)), quantidadeClusters))
    adequacaoAtual = 1
    adequacaoAnterior = 0

    # Initialization
    for t in range(iterationLimit):

        if t == 0:
            matrizMedoidsFinal = inicializaMatrizMedoids(quantidadeClusters, quantidadeMatrizDissimilaridade)
            matrizPesosFinal = inicializaMatrizPesos(quantidadeClusters, quantidadeMatrizDissimilaridade)
            matrizGrauAssociacaoFinal = calculaMatrizGrauAssociacao(retornaMatrizDistancia(1), quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
        else:

            matrizMedoidsFinal = calculaMatrizMedoids(matrizGrauAssociacaoFinal, retornaMatrizDistancia(1), m, quantidadeClusters, quantidadeMatrizDissimilaridade)
            # print('Matriz Medoids -------------------------->')
            # print(matrizMedoidsFinal)

            matrizPesosFinal = calculaMatrizRelevancia(quantidadeClusters, quantidadeMatrizDissimilaridade, matrizGrauAssociacaoFinal, m, matrizMedoidsFinal)
            matrizPesoAntiga = matrizPesosFinal
            # print('Matriz Pesos -------------------------->')
            # print(matrizPesosFinal)

            # prod(matrizPesosFinal[10, ])

            matrizGrauAssociacaoFinal = calculaMatrizGrauAssociacao(retornaMatrizDistancia(1), quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
            # print('Matriz Associação -------------------------->')
            # print(matrizGrauAssociacaoFinal)

            # sum(matrizGrauAssociacaoFinal[2, ]) 

        adequacaoAtual = funcaoCriterio(quantidadeMatrizDissimilaridade, quantidadeClusters, matrizGrauAssociacaoFinal, matrizPesosFinal, retornaMatrizDistancia(1), matrizMedoidsFinal, m)

        # print('Adequação Atual -------------------------->')
        # print(adequacaoAtual)

        # print('Adequacao Anterior -------------------------->')
        # print(adequacaoAnterior)

        if abs(adequacaoAtual - adequacaoAnterior) < diferencaMedoids:
            break
        else:
            adequacaoAnterior = adequacaoAtual
            adequacaoAtual = 1

    pd.DataFrame(matrizMedoidsFinal).to_csv('Matriz medoids.csv',index=False, header=False)
    pd.DataFrame(matrizPesosFinal).to_csv('Matriz pesos.csv',index=False, header=False)
    pd.DataFrame(matrizGrauAssociacaoFinal).to_csv('Matriz associacao.csv',index=False, header=False)


# ------------------------------------ FIM ALGORITMO ------------------------------------>
