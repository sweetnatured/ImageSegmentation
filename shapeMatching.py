import numpy as np
import cv2

resim2=cv2.imread('/home/salih/Desktop/second.png')

gray=cv2.cvtColor(resim2,cv2.COLOR_BGR2GRAY)

threshold,image=cv2.threshold(gray,127,255,0)

contours,hierachy=cv2.findContours(image.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
n=len(contours)-1                                                                       #We taking sorted list
sortlist=sorted(contours,key=cv2.contourArea,reverse=False)[:n]                          #we dont take the biggest contour

for cnt in sortlist:

    approx=cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)    #find the number of approximate contour number


    if len(approx)==3:                                           # if it is 3 that means a triangle

        shape_name="Triangle"
        cv2.drawContours(resim2,[cnt],0,(0,0,0),-1)
        M=cv2.moments(cnt)
        cx=  int(M['m10'] / M['m00'])                            #find the momentum for writing the its label.
        cy = int(M['m01'] / M['m00'])
        cv2.putText(resim2,"triangle",(cx-50,cy),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),1)


    elif len(approx)==4:                                          # if it is 4 that means a rectangular

        x,y,w,h=cv2.boundingRect(cnt)
        cv2.drawContours(resim2, [cnt], 0, (0,0, 0), -1)
        M = cv2.moments(cnt)                                        #find the momentum for writing the its label.
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        if(w-h==0):                                                  #İf w-h==0 that means that object is square
            cv2.putText(resim2, "square", (cx - 50, cy), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255,0), 1)

        else:

            M = cv2.moments(cnt)                                     #find the momentum for writing the its label.
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(resim2, "rectangular", (cx - 50, cy), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255,0), 1)


    elif len(approx)>10:                                           # if it is bigger than 10 that means a circle

        cv2.drawContours(resim2,cnt,0,(0,0,0),-1)
        M=cv2.moments(cnt)                                               #find the momentum for writing the its label.
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(resim2,"Circle",(cx-50,cy),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),1)



cv2.imshow("image",resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()



#You create a image that contains circle,rectangular,triangle
#Program can determine objects label.