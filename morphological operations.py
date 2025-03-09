#morphological operations

import cv2
import numpy as np

img = cv2.imread("noisy_desert.jpg",1)
resized = cv2.resize(img,(899,600))
cv2.imshow("desert",resized) #418x414
cv2.waitKey(0)


'''
cv2.imshow("Resized Pikachu",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((5,5),np.uint8)
eroded = cv2.erode(img,kernel)
cv2.imshow("Eroded Pikachu",eroded)
'''
gauss_blur = cv2.GaussianBlur(resized,(15,15),0)
cv2.imshow("Gauss Blur desert",gauss_blur)
cv2.waitKey(0)


median_blur = cv2.medianBlur(resized,11)
cv2.imshow("Median Blur desert",median_blur)
cv2.waitKey(0)

bilat_filter = cv2.bilateralFilter(resized,40,120,120)
cv2.imshow("Bilat Filter desert",bilat_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()