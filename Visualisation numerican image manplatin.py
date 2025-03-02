import cv2
import numpy as np
import matplotlib.pyplot as plt

r = np.array([102,102,102])
r2 = np.array([24,24,24])

box1 = np.full((300,300,3),r,dtype=np.uint8)
box2 = np.full((300,300,3),r2,dtype=np.uint8)

#box1=cv2.cvtColor(box1,cv2.COLOR_BGR2RGB)
#box2=cv2.cvtColor(box2,cv2.COLOR_BGR2RGB)

result = box1 + box2

subresult = cv2.subtract(box1,box2)
addresult = cv2.add(box1,box2)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(addresult,"This is the result from cv2.add",(0,280),font,0.6,(0,0,0))
cv2.putText(subresult,"This is the result from cv2.subtract",(0,280),font,0.6,(0,0,0))

mainimg = np.concatenate((box1,box2,addresult,subresult),axis=1)

cv2.imshow("Framework",mainimg)
cv2.waitKey(0)

'''
cv2.imshow("color1",box1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("color2",box2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("colormix",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

result2 = cv2.add(box1,box2)
cv2.imshow("colormix2",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(box1)
plt.title("color1")

plt.figure(figsize=(10,5))
plt.subplot(1,3,2)
plt.imshow(box2)
plt.title("color2")

plt.figure(figsize=(10,5))
plt.subplot(1,3,3)
plt.imshow(result)
plt.title("result")

plt.show()'''