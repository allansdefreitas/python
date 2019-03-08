import	cv2
#	Carregando	a	imagem	em	RGB
imagem	=	cv2.imread("fruits.jpg")

#	Convertendo	e	exibindo	a	imagem	em	tons	de	cinza
imagem	=	cv2.cvtColor(imagem,	cv2.COLOR_RGB2GRAY)

cv2.imshow("Imagem GRAY",	imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()