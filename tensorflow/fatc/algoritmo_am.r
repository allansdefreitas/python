# FUNÇÃO DE CRITÉRIO -> J(G, A, U) ----------------------------------------------------------------------------------------------------------->

distanciaObjetoMedoid <- function(quantidadeMatrizDissimilaridade, vetorPesosRelevancia, vetorMedoids, posicaoVetorDados){
  
  # Somatório j=1..p
  distanciaFinal = numeric(0)
  
  for (j in 1:quantidadeMatrizDissimilaridade) {
    distanciaFinal[j] = vetorPesosRelevancia[j] * retornaMatrizDistancia(j)[posicaoVetorDados, vetorMedoids[j]]
  }
  
  return(sum(distanciaFinal))
}

funcaoCriterio <- function(quantidadeMatrizDissimilaridade, quantidadeClusters, matrizGrauAssociacao, matrizPesosRelevantes, dados, matrizMedoids, m = 1.6){
  
  # Somátorio k=1..K
  medidaAdequacao = numeric(0)
  numeroLinhas = nrow(dados)
  
  matrizGrauAssociacao <- matrizGrauAssociacao ^ m
  
  for (k in 1:quantidadeClusters) {
    
    # Somatório i=1..n
    somatorioLinhas = numeric(0)
    
    for(i in 1:numeroLinhas){
      somatorioLinhas[i] = matrizGrauAssociacao[i, k] * distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesosRelevantes[k, ], matrizMedoids[k, ], i)
    }
    
    # O index 600 do somatorioLinhas possui o falor NaN (que quebra o somatório), por isso, utilizando o na.rm = TRUE
    medidaAdequacao[k] = sum(somatorioLinhas, na.rm = TRUE)
  }
  
  return(sum(medidaAdequacao))
}
# FIM FUNÇÃO DE CRITÉRIO -> J(G, A, U) ------------------------------------------------------------------------------------------------------->



# FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g ------------------------------------------------------------------------------------------------>

calculaMatrizMedoids <- function(matrizGrauAssociacao, dados, m, quantidadeClusters, quantidadeMatrizDissimilaridade){
  
  # Somatório i=1...n
  numeroLinhas = nrow(dados)
  matrizMedoids = matrix(0, quantidadeClusters, quantidadeMatrizDissimilaridade)
  
  matrizGrauAssociacao <- matrizGrauAssociacao ^ m
  
  for (k in 1:quantidadeClusters) {
    vetorMedoids <- numeric(0)
    
    for (j in 1:quantidadeMatrizDissimilaridade) {
      
      matrizMultiplicacoes <- matrizGrauAssociacao[, k] * retornaMatrizDistancia(j)
      
      arraySomatorios <- colSums(matrizMultiplicacoes, na.rm = TRUE)
      
      # Retorna o index do conjunto de dados cujo somatorio do produto do matrizGrauAssociacao pela distancia sejao mínimo
      vetorMedoids[j] <- which.min(arraySomatorios)
    }
    
    matrizMedoids[k, ] <- vetorMedoids
  }
  
  return (matrizMedoids)
}
# FIM FUNÇÃO DE CALCULO DO VETOR DE MEDOIDS -> g -------------------------------------------------------------------------------------------->



# FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ----------------------------------------------------------------------------------------->

calculaMatrizRelevancia <- function(quantidadeClusters, quantidadeMatrizDissimilaridade, dados, matrizGrauAssociacao, m, matrizMedoids){
  
  numeroLinhas = nrow(dados)
  matrizRelevancia = matrix(0, quantidadeClusters, quantidadeMatrizDissimilaridade)
  matrizGrauAssociacao <- matrizGrauAssociacao ^ m
  
  for (k in 1:quantidadeClusters) {
    
    vetorRelevancias = numeric(0)
    
    for (j in 1:quantidadeMatrizDissimilaridade) {
      
      somatorioSuperior = numeric(0)
      somatorioInferior = numeric(0)
      
      vetorMultiplicacoesInferior <- matrizGrauAssociacao[, k] * retornaMatrizDistancia(j)[, matrizMedoids[k, j]] 
      somatorioInferior <- sum(vetorMultiplicacoesInferior, na.rm = TRUE)
      
      # Produtório 1...p
      for (h in 1:quantidadeMatrizDissimilaridade) {
        
        vetorMultiplicacoesSuperior <- matrizGrauAssociacao[, k] * retornaMatrizDistancia(h)[, matrizMedoids[k, h]]
        somatorioSuperior[h] <- sum(vetorMultiplicacoesSuperior, na.rm = TRUE)
      }
      
      vetorRelevancias[j] = ( prod(somatorioSuperior) ^ (1/quantidadeMatrizDissimilaridade) ) / (sum(somatorioInferior, na.rm = TRUE))
    }
    
    matrizRelevancia[k, ] = vetorRelevancias
  }
  
  return (matrizRelevancia)
}
# FIM FUNÇÃO DO CALCULO DO PESO DE RELEVÂNCIA -> lambda ------------------------------------------------------------------------------------->



# FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u ------------------------------------------------------------------------------------------------->

calculaMatrizGrauAssociacao <- function(dados, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesos, matrizMedoids, m){
  
  numeroLinhas = nrow(dados)
  matrizGrauAssociacao = matrix(0, numeroLinhas, quantidadeClusters)
  
  for (i in 1:numeroLinhas) {
    
    vetorGrauAssociacao = numeric(0)
    
    for (k in 1:quantidadeClusters) {
      
      valorGrauAssociacao = numeric(0)
      distanciaSuperior <- distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesos[k, ], matrizMedoids[k, ], i)
      
      for (h in 1:quantidadeClusters) {
        distanciaInferior <- distanciaObjetoMedoid(quantidadeMatrizDissimilaridade, matrizPesos[h, ], matrizMedoids[h, ], i)
        
        valorGrauAssociacao[h] = (distanciaSuperior/distanciaInferior) ^ 1/(m-1)
      }
      
      vetorGrauAssociacao[k] = ( 1/(sum(valorGrauAssociacao)) )
    }
    
    matrizGrauAssociacao[i, ] = vetorGrauAssociacao
  }
  
  return (matrizGrauAssociacao)
}
# FIM FUNÇÃO CALCULO DO GRAU DE ASSOCIAÇÃO -> u --------------------------------------------------------------------------------------------->



# ----------------------------------- INICIO DO CÓDIGO ----------------------------------->
# Carrega o dataset demfeat-kar
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

# -------------------------- INICIALIZADOR DA MATRIZ DE MEDOIDS ------------------------->

# Inicializa uma matriz de medoids de tamanho [KxP], com o valor da ultima linha de cada classe
inicializaMatrizMedoids <- function(quantidadeGrupos, quantidadeMatrizesDissimilaridades){
  matrizMedoids = matrix(0, quantidadeGrupos, quantidadeMatrizesDissimilaridades) # U
  
  for (i in 1:quantidadeGrupos) {
    for(j in 1:quantidadeMatrizesDissimilaridades){
        matrizMedoids[i, j] = i*200
    }
  }
  
  return (matrizMedoids)
}
# ---------------------------------- FIM INICIALIZADOR ---------------------------------->



# --------------------------- INICIALIZADOR DA MATRIZ DE PESOS -------------------------->

# Inicializa uma matriz de pesos de tamanho [KxP], com o valor unitário 
inicializaMatrizPesos <- function(quantidadeGrupos, quantidadeMatrizDissimilaridade){
  matrizPesos = matrix(1, quantidadeGrupos, quantidadeMatrizDissimilaridade)
  
  return (matrizPesos)
}
# ------------------------------- FIM INICIALIZADOR PESOS ------------------------------->



# ------------- FUNÇÃO QUE RETORNA A MATRIZ DE DISSIMILARIDADE NA POSIÇÃO P ------------->
retornaMatrizDistancia <- function(posicao){
  
  listaMatrizes <- list(matrizDistanciaLinhaKar, matrizDistanciaLinhaFac, matrizDistanciaLinhaFou)
  
  return(listaMatrizes[[posicao]])
}
# --------------------------------------------------------------------------------------->



# ---------------------------------------- TESTE ---------------------------------------->

matrizPesoTeste = inicializaMatrizPesos(10, 3)
matrizMedoidTeste = inicializaMatrizMedoids(10, 3)
matrizGrauAssociacaoTeste <- calculaMatrizGrauAssociacao(dados_kar, 10, 3, matrizPesoTeste, matrizMedoidTeste, 1.6)
head(matrizGrauAssociacaoTeste)
adequacaoTeste = funcaoCriterio(3, 10, matrizGrauAssociacaoTeste, matrizPesoTeste, dados_kar_normalizados, matrizMedoidTeste, 1.6)

# -------------------------------------- FIM TESTE -------------------------------------->



# -------------------------------------- ALGORITMO -------------------------------------->

# Inputs
quantidadeClusters <- 10
quantidadeMatrizDissimilaridade <- 3
m <- 1.6
iterationLimit <- 150
diferencaMedoids <- 10 ^ (-10)

# Outputs
matrizMedoidsFinal <- numeric(0)
matrizPesosFinal <- numeric(0)
matrizGrauAssociacaoFinal <- numeric(0)
adequacaoAtual <- 1
adequacaoAnterior <- 0

# Initialization
for (t in 1:iterationLimit) {
  
  if (t == 1) {
    matrizMedoidsFinal <- inicializaMatrizMedoids(quantidadeClusters, quantidadeMatrizDissimilaridade)
    matrizPesosFinal <- inicializaMatrizPesos(quantidadeClusters, quantidadeMatrizDissimilaridade)
    matrizGrauAssociacaoFinal <- calculaMatrizGrauAssociacao(dados_kar, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
  }else {
    
    matrizMedoidsFinal <- calculaMatrizMedoids(matrizGrauAssociacaoFinal, dados_kar_normalizados, m, quantidadeClusters, quantidadeMatrizDissimilaridade)
    print('Matriz Medoids -------------------------->')
    print(matrizMedoidsFinal)
    
    matrizPesosFinal <- calculaMatrizRelevancia(quantidadeClusters, quantidadeMatrizDissimilaridade, dados_kar_normalizados, matrizGrauAssociacaoFinal, m, matrizMedoidsFinal)
    print('Matriz Pesos -------------------------->')
    print(matrizPesosFinal)
    matrizPesoAntiga <- matrizPesosFinal
    
    prod(matrizPesosFinal[10, ])
    
    matrizGrauAssociacaoFinal <- calculaMatrizGrauAssociacao(dados_kar_normalizados, quantidadeClusters, quantidadeMatrizDissimilaridade, matrizPesosFinal, matrizMedoidsFinal, m)
    print('Matriz Associação -------------------------->')
    print(matrizGrauAssociacaoFinal)
    
    sum(matrizGrauAssociacaoFinal[2, ]) 
  }
  
  adequacaoAtual <- funcaoCriterio(quantidadeMatrizDissimilaridade, quantidadeClusters, matrizGrauAssociacaoFinal, matrizPesosFinal, dados_kar, matrizMedoidsFinal)
  
  print('Adequação Atual -------------------------->')
  print(adequacaoAtual)
  
  print('Adequacao Anterior -------------------------->')
  print(adequacaoAnterior)
  
  if (abs(adequacaoAtual - adequacaoAnterior) < diferencaMedoids) {
    break
  } else {
    adequacaoAnterior <- adequacaoAtual
    adequacaoAtual <- 1
  }
}

print('funcionou!')

# ------------------------------------ FIM ALGORITMO ------------------------------------>
