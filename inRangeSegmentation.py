import	cv2
import	numpy	as	np

imgRGB	=	cv2.imread("poker.png")
# Para HSV
imgHSV	=	cv2.cvtColor(imgRGB,	cv2.COLOR_BGR2HSV)

# limite inferior (mais claro) e superior (mais escuro) aceitos
# do vermelho: [[120 255 255]]]

tomClaro	=	np.array([160,	100,	100])
tomEscuro	=	np.array([200,	255,	255])

imgSegmentada	=	cv2.inRange(imgHSV,	tomClaro,	tomEscuro)


cv2.imshow("Original",	imgRGB)	
cv2.imshow("Segmentada",	imgSegmentada)
#cv2.imshow("Processada", imgProcessada)


cv2.waitKey(0)
cv2.destroyAllWindows()