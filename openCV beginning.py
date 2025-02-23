import cv2

'''var1 = cv2.imread("pikachu.png",cv2.IMREAD_GRAYSCALE)
#var1 = cv2.imread("pikachu.png",0) #is the same as above (1 is color)

cv2.imshow("Pikachu",var1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


'''var2 = cv2.imread("pikachu.png",1)
b,g,r = cv2.split(var2)

def shorten(text,var):
    cv2.imshow(text,var)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    shorten("Original",var2)
    shorten("Blue Saturation Image",b)
    '''

'''var3 = cv2.imread("buildings&tree.png")
#var4 = cv2.cvtColor(var3,cv2.COLOR_BGR2GRAY)
#print(var4.shape)
var5 = cv2.cvtColor(var3,cv2.COLOR_BGR2RGB)
print(var5)'''

var6 = cv2.imread("umbrellas.png")
var6 = cv2.cvtColor(var6,cv2.COLOR_BGR2RGB)
r,g,b = cv2.split(var6)

def shorten(text,var):
    cv2.imshow(text,var)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

shorten("red",r)
shorten("blue",b)
shorten("green",g)