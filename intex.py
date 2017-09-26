import cv2
import os
#import  numpy as np
from  seperator import seperatorfun
#from ImageFun import rotateImage
from ImageFun import BINuGAU,rotateImage

path0 = 'C:/Users/SAROJ/Desktop/PdLabProj'
path1 = 'C:/Users/SAROJ/Desktop/PdLabProj/CroppedImg/'
path2 = 'C:/Users/SAROJ/Desktop/PdLabProj/RotImg/'

img = cv2.imread('EqnImage.png',0)
noImgs=seperatorfun(img,path1,0,0)
#print (noImgs)

for i in range(noImgs):
    cropping = cv2.imread(os.path.join( path1,str(i)+'.png'))
    rotateImage(cropping,i)
    #rotshow = cv2.imread(os.path.join(path2, str(i) + '.png'))
    #cv2.imshow('this is rotated',rotshow )
    #cv2.waitKey(0)

path3='C:/Users/SAROJ/Desktop/PdLabProj/SymbolImg/'



for i in range(noImgs):
    symbol=cv2.imread(os.path.join(path2,str(i) + '.png'), 0)
    noImgs = seperatorfun(symbol, path3,1,i)

