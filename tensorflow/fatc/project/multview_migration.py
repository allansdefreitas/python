#Transforming Code: R to Python (STARTING)

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
matrizDistanciaLinhaKar = euclidean_distances(dados_kar_normalizados, dados_kar_normalizados)

# MFEAT-FOU -----------------------------------------------------------------------------#############

dados_fou = pd.read_csv('C:/datasets/mfeat-fou', delimiter='\s+', header=None)

numLinhas_fou = dados_fou.shape[0]
numColunas_fou = dados_fou.shape[1]

#Normalizando com média 0 e desvio padrão 1
dados_fou_normalizados = preprocessing.scale(dados_fou)
dados_fou_normalizados

# Calcula a distância euclidiana para o numero de colunas
matrizDistanciaLinhaFou = euclidean_distances(dados_fou_normalizados, dados_fou_normalizados)

# MFEAT-FAC -----------------------------------------------------------------------------#############

dados_fac = pd.read_csv('C:/datasets/mfeat-fac', delimiter='\s+', header=None)

numLinhas_fac = dados_fou.shape[0]
numColunas_fac = dados_fou.shape[1]

#Normalizando com média 0 e desvio padrão 1
dados_fac_normalizados = preprocessing.scale(dados_fac)
dados_fac_normalizados

# Calcula a distância euclidiana para o numero de colunas (76)
matrizDistanciaLinhaFac = euclidean_distances(dados_fac_normalizados, dados_fac_normalizados)
matrizDistanciaLinhaFac

#/ End of main code --------------------------------------------------------------------------------------######

# FUNÇÃO DE CRITÉRIO -> J(G, A, U) ----------------------------------------------------------------------------------------------------------->




# FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g ------------------------------------------------------------------------------------------------>


# FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ----------------------------------------------------------------------------------------->



# FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u ------------------------------------------------------------------------------------------------->















# -------------------------- INICIALIZADOR DA MATRIZ DE MEDOIDS ------------------------->


# --------------------------- INICIALIZADOR DA MATRIZ DE PESOS -------------------------->


# ------------- FUNÇÃO QUE RETORNA A MATRIZ DE DISSIMILARIDADE NA POSIÇÃO P ------------->


# ---------------------------------------- TESTE ---------------------------------------->

# -------------------------------------- ALGORITMO -------------------------------------->
