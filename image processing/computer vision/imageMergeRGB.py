import cv2

 #-*- coding: utf-8 -*-
 
 # Carregando imagem	RGB	e segmentando canais
imagem = cv2.imread("fruits.jpg")
azul, verde, vermelho = cv2.split(imagem)

# Combinando os três canais	em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()