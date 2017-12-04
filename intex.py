import cv2
import os
from  seperator import*
from ImageFun import*

path0 = 'E:/5th sem/PdLabProj/'
path1 = 'E:/5th sem/PdLabProj/CroppedImg/'
path2 = 'E:/5th sem/PdLabProj/RotImg/'
x=50
img = cv2.imread('xyz1233.png',0)
noImgs=seperatorfun(img,path1,0,0)

for i in range(noImgs):
    cropping = cv2.imread(os.path.join( path1,str(i)+'.png'))
    rotateImage(cropping,i)
path3='E:/5th sem/PdLabProj/SymbolImg/'


globalCount=0
for i in range(noImgs):
    symbolR = cv2.imread(os.path.join(path2, str(i) + '.png'), 0);
    noImgs = seperatorfun2(symbolR, path3,1,i,globalCount)

for i in range(x):
    cropping = cv2.imread(os.path.join( path3,str(i)+'.png'))
    rotateImage2(cropping,i)