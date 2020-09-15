#From : Introdução à Visão Computacional, Felipe Bareli (Adaptado)
#ERROR

import numpy as np
import cv2

cascadeFace	= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#get image
imagemOriginal = cv2.imread("imgs/brazilian_women_soccer_team.jpg")

# converts to gray
imagem = cv2.cvtColor(imagemOriginal,	cv2.COLOR_BGR2GRAY)

faces =	cascadeFace.detectMultiScale(imagem,	1.3,	5,	(30,30))

# Desenha	um	retângulo	nas	faces	detectadas
for	(x,y,w,h) in faces:
    ctangle(imagemOriginal,	(x,y),	(x+w,	y+h),	(000,255,0),	2
)
        
#Exibe	o	total	de	faces	detectadas
    
print len(faces)

cv2.imshow("Resultado",	imagemOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows()
