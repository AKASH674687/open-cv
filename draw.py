import cv2 as cv
import numpy as np


# Create a black image
img = np.zeros((520,520,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(519,519),(259,259,0),6)
#Drawing ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#circle
cv.circle(img,(447,63), 63, (0,0,255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'cereal',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
#image display
j = cv.imshow("image",img)
cv.waitKey(0)

if j == ord("s"):
    cv.imwrite("images/drawing.png",img)