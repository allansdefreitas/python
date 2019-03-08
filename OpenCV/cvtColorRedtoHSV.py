import	cv2
import	numpy	as	np
vermelhoRGB	=	np.uint8([[[255,0,0]]])
vermelhoHSV	=	cv2.cvtColor(vermelhoRGB,	cv2.COLOR_BGR2HSV)
print	vermelhoHSV