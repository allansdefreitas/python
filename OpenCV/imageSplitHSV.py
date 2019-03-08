import	cv2

imagem = cv2.imread("fruits.jpg")

# RGB to HSV
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# split a HSV image in three channels: Hue, Saturation and Value
matiz,	saturacao, valor = cv2.split(imagem)

cv2.imshow("Canal	H",	matiz)
cv2.imshow("Canal	S",	saturacao)
cv2.imshow("Canal	V",	valor)

cv2.waitKey(0)
cv2.destroyAllWindows()