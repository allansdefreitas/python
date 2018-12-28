import	cv2

img	=	cv2.imread("imagem.png")

cv2.imshow("Imagem: Show",	img)
cv2.waitKey(0)
cv2.destroyAllWindows()
