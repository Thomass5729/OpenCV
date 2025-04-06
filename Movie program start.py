import cv2
import numpy as np
from PIL import Image
import os
os.chdir("C:\\Users\\Thomas\\Documents\\Coding\\OpenCV\\movie")
path = "C:\\Users\\Thomas\\Documents\\Coding\\OpenCV\\movie"

totH = 0
totW = 0


Image.MAX_IMAGE_PIXELS = None
for i in os.listdir("."):
    img = Image.open(os.path.join(path,i))
    width,height = img.size
    totW += width
    totH += height

meanW = totW//(len(os.listdir(".")))
meanH = totH//(len(os.listdir(".")))

for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith("jpeg") or i.endswith("png"):
        img = Image.open(os.path.join(path,i))
        resized = img.resize((meanW,meanH))
        resized.save(i,"JPEG",quality = 95)
        print("file has been resized")

print(meanW,meanH)
