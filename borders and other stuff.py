#borders

import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

'''img = cv2.imread("pikachu.png")

row,column = img.shape[0:2]
for i in range(row):
    for j in range(column):
        img[i,j] = sum(img[i,j])/3
cv2.imshow("grey",img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
'''
for i in range(72):
    img2 = cv2.imread("buildings&tree.png")
    row,column = img2.shape[0:2]
    centre = (row/2,column/2)
    rotate = cv2.getRotationMatrix2D(centre,5*i,scale=0.8)
    rotatyevarialvblee2 = cv2.warpAffine(img2,rotate,(row,column))
    cv2.imshow("spinnnn",rotatyevarialvblee2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

'''img3or4or5 = cv2.imread("pikachu.png")
variableforcamii = cv2.Canny(img3or4or5,750,750)
cv2.imshow("edgesss",variableforcamii)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

img4or5or6 = cv2.imread("red planet.jpg")
rectangle = cv2.rectangle(img4or5or6,(200,200),(1400,1000),(0,0,255),6)
line = cv2.line(img4or5or6,(200,200),(1400,1000),(0,0,255),6)
circle = cv2.circle(img4or5or6,(790,310),270,(0,255,0),6)
cv2.imshow("LINEEEE AND RECRANGEL",img4or5or6)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''#border = cv2.copyMakeBorder(img,250,250,250,250,cv2.BORDER,value=1)
#cv2.imshow("Border example 1",border)
cv2.waitKey(0)


border2 = cv2.copyMakeBorder(img,500,500,500,500,cv2.BORDER_WRAP,value=1)
cv2.imshow("Border example 2",border2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
