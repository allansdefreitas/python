#Transforming Code: R to Python (STARTING)

# ----------------------------------- INICIO DO CÓDIGO ----------------------------------->
# Carrega o dataset demfeat-kar
#HOW TO READ A DATASET IN PYTHON? (16-05 - 22:02) 
library(readr)
dados_kar <- read_table("C:/Users/Usuario/Downloads/projeto_francisco/mfeat-kar", col_names = FALSE)
#View(dados_kar)

# Transformar o dados_kar, em uma matriz (númerica)
# Por algum motivo o R-Studio não entende a matriz original (quando carregada) do tipo matriz de numerics
dados_kar <- as.matrix(dados_kar)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala e centraliza)
dados_kar_normalizados <- scale(dados_kar)

# Calcula a distância euclidiana para o numero de colunas (64)
matrizDistanciaLinhaKar <- as.matrix(dist(dados_kar_normalizados))   

#-------------------------------------------

# Carrega o dataset de mfeat-fou
dados_fou <- read_table("C:/Users/Usuario/Downloads/projeto_mestrado/mfeat-fou", col_names = FALSE)
#View(dados_fou)

# Transformar o dados_fou, em uma matriz (númerica)
# Por algum motivo o R-Studio não entendea matriz original (quando carregada) do tipo matriz de numerics
# class(dados_fou)
dados_fou <- as.matrix(dados_fou)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala e centraliza)
dados_fou_normalizados <- scale(dados_fou)

# Calcula a distância euclidiana para o numero de colunas (76)
matrizDistanciaLinhaFou <- as.matrix(dist(dados_fou_normalizados)) 

# --------------------------------------------

dados_fac <- read_table("C:/Users/Usuario/Downloads/projeto_mestrado/mfeat-fac", col_names = FALSE)
#View(dados_fac)

# Transformar o dados_fac, em uma matriz (númerica)
# Por algum motivo o R-Studio não entendea matriz original (quando carregada) do tipo matriz de numerics
# class(dados_fac)
dados_fac <- as.matrix(dados_fac)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala ecentraliza)
dados_fac_normalizados <- scale(dados_fac)

matrizDistanciaLinhaFac <- as.matrix(dist(dados_fac_normalizados))

# ------------------------------------ FIM DO CÓDIGO ------------------------------------>

