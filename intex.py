import cv2
import os
import  numpy as np
from  seperator import seperatorfun
from ImageFun import rotateImage

path0 = 'E:/5th sem/PdLabProj/'
path1 = 'E:/5th sem/PdLabProj/CroppedImg/'
path2 = 'E:/5th sem/PdLabProj/RotImg/'

img = cv2.imread('EqnImage.png',0)
noImgs=seperatorfun('EqnImage.png',path1,path2)

for i in range(noImgs):
    cropping = cv2.imread(os.path.join( path1,str(i)+'.png'))
    rotateImage(cropping,i)
    rotshow = cv2.imread(os.path.join(path2, str(i) + '.png'))
    cv2.imshow('this is rotated',rotshow )
    cv2.waitKey(0)
path3='E:/5th sem/PdLabProj/SymbolImg/'



for i in range(noImgs):
    change = []
    readRot = cv2.imread(os.path.join(path2, str(i) + '.png'),0)
    masksize = len(readRot[0])// 15
    Image4Arr = readRot.copy()
    Image4Mask = readRot.copy()
    arr = SumINTOarr(Image4Arr)
    change = changelist(Image4Mask)
    image = maskfunction(Image4Mask, change, masksize)
    midlist = MIDpointARR(arr, image)
    noImgs = CROPimage(midlist, readRot, arr,path3)
    cv2.waitKey(0)
