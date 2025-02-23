import cv2
import numpy

chalet = cv2.imread("snowy_hut.jpg")
planet = cv2.imread("red planet.jpg")

#weightedsum = cv2.addWeighted(chalet,0.5,planet,0.3,-50)
subtracted_img = cv2.subtract(chalet,planet)
cv2.imshow("Image merge",subtracted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
