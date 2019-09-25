import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/contim.png')


x=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)  # Converted to Gray
threshold,y=cv2.threshold( x, 254,255,cv2.THRESH_BINARY );             # we have to conver the imaga black and white in order to get contours.


contours,hiearchy = cv2.findContours(y,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resim,contours,-1,color=(0,0,255),thickness=1)

cv2.imshow('Contour with External Hiearchy',resim)
cv2.waitKey(0)




cv2.destroyAllWindows()