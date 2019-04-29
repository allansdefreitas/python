# ----------------------------------- INICIO DO CÓDIGO ----------------------------------->
# Carrega o dataset demfeat-kar
library(readr)
dados_kar <- read_table("C:/Users/Allan Santos/Documents/Repos/python/tensorflow/fatc/mfeat-kar", col_names = FALSE)
View(dados_kar)
plot(dados_kar[, 1])
# Exibe apenas as 3 primeiras linhas do dataset
#dados_kar[c(1, 2, 3), ]

# Pegar o número delinhas e colunas
numeroLinhasKar = nrow(dados_kar)
numeroColunasKar = ncol(dados_kar)

# Transformar o dados_kar, em uma matriz (númerica)
# Por algum motivo o R-Studio não entendea matriz original (quando carregada) do tipo matriz de numerics
dados_kar <- as.matrix(dados_kar)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala e centraliza)
dados_kar_normalizados <- scale(dados_kar)

#dados normalizados/padronizados/Z (0,1)
View(dados_kar_normalizados)

# Plotar os dados da 1ª coluna
plot(dados_kar[, 1])
plot(dados_kar_normalizados[, 1]) # entre -2 e 2

##HERE###


# Calcula a distância euclidiana para o numero de colunas (64)
# Apenas o triangulo superior...
# matriz_distancias_euclidianas_triangulo_superior_kar = matrix(0, numeroColunasKar, numeroColunasKar)
# for(i in 1:numeroColunasKar){
#   for (j in i:numeroColunasKar) {
#     matriz_distancias_euclidianas_triangulo_superior_kar[i,j] <- euc.dist(dados_kar_normalizados[,i], dados_kar_normalizados[,j])
#   }
# }

matrizDistanciaLinhaKar <- as.matrix(dist(dados_kar_normalizados))

#-------------------------------------------

# Carrega o dataset de mfeat-fou
library(readr)
dados_fou <- read_table("C:/Users/Usuario/Downloads/projeto_mestrado/mfeat-fou", col_names = FALSE)
View(dados_fou)
# Exibe apenas as 3 primeiras linhas do dataset
# dados_fou[c(1, 2, 3), ]

# Pegar o número delinhas e colunas
numeroLinhasFou = nrow(dados_fou)
numeroColunasFou = ncol(dados_fou)

# Transformar o dados_fou, em uma matriz (númerica)
# Por algum motivo o R-Studio não entendea matriz original (quando carregada) do tipo matriz de numerics
# class(dados_fou)
dados_fou <- as.matrix(dados_fou)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala e centraliza)
dados_fou_normalizados <- scale(dados_fou)
# Plotar os dados da 1ª coluna
plot(dados_fou_normalizados[, 1])
plot(dados_fou[, 1])

# Calcula a distância euclidiana para o numero de colunas (76)
# Apenas o triangulo superior...
# matriz_distancias_euclidianas_triangulo_superior_fou = matrix(0, numeroColunasFou, numeroColunasFou)
# for(i in 1:numeroColunasFou){
#   for (j in i:numeroColunasFou) {
#     matriz_distancias_euclidianas_triangulo_superior_fou[i,j] <- euc.dist(dados_fou_normalizados[,i], dados_fou_normalizados[,j])
#   }
# }

matrizDistanciaLinhaFou <- as.matrix(dist(dados_fou_normalizados)) 
matrizDistanciaLinhaFou[3,]
# --------------------------------------------

library(readr)
dados_fac <- read_table("C:/Users/Usuario/Downloads/projeto_mestrado/mfeat-fac", col_names = FALSE)
View(dados_fac)
# Exibe apenas as 3 primeiras linhas do dataset
# dados_fac[c(1, 2, 3), ]

# Pegar o número delinhas e colunas
numeroLinhasFac = nrow(dados_fac)
numeroColunasFac = ncol(dados_fac)

# Transformar o dados_fac, em uma matriz (númerica)
# Por algum motivo o R-Studio não entendea matriz original (quando carregada) do tipo matriz de numerics
# class(dados_fac)
dados_fac <- as.matrix(dados_fac)

# Normaliza os dados (média = 0,variância = 1) (diminui a escala ecentraliza)
dados_fac_normalizados <- scale(dados_fac)
# Plotar os dados da 1ª coluna
plot(dados_fac_normalizados[, 1])
plot(dados_fac[, 1])

# Calcula a distância euclidiana para o numero de colunas (216)
# Apenas o triangulo superior...
# matriz_distancias_euclidianas_triangulo_superior_fac = matrix(0, numeroColunasFac, numeroColunasFac)
# for(i in 1:numeroColunasFac){
#   for (j in i:numeroColunasFac) {
#     matriz_distancias_euclidianas_triangulo_superior_fac[i,j] <- euc.dist(dados_fac_normalizados[,i], dados_fac_normalizados[,j])
#   }
# }

for(i in 1:numeroLinhasFac){
  for (j in i:numeroLinhasFac) {
    matriz_distancias_euclidianas_triangulo_superior_fac[i,j] <- euc.dist(dados_fac_normalizados[,i], dados_fac_normalizados[,j])
  }
}

matrizDistanciaLinhaFac <- as.matrix(dist(dados_fac_normalizados))
matrizDistanciaLinhaFac[c(1:9), c(1:9)]

# ------------------------------------ FIM DO CÓDIGO ------------------------------------>