import numpy as np
import cv2



def findArea(contours):
    Area = []
    for i in contours:

        areax=cv2.contourArea(i)
        Area.append(areax)

    return Area


resim=cv2.imread('/home/salih/Desktop/conttt.png')

Gray=cv2.cvtColor(resim,cv2.cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(Gray,50,150)

contours,hiearchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resim,contours,-1,color=(0,0,255),thickness=1)

cv2.imshow('a',resim)
cv2.waitKey(0)

sıralı=sorted(contours,key=cv2.contourArea,reverse=True)

print(findArea(sıralı))