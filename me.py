import cv2
import os
import  numpy as np
from  seperator import seperatorfun
from ImageFun import rotateImage
from ImageFun import BINuGAU,rotateImage
from ArrMidCrop import show

path0 = 'C:/Users/SAROJ/Desktop/PdLabProj'
path1 = 'C:/Users/SAROJ/Desktop/PdLabProj/CroppedImg/'
path2 = 'C:/Users/SAROJ/Desktop/PdLabProj/RotImg/'
path3='C:/Users/SAROJ/Desktop/PdLabProj/SymbolImg/'



#for i in range(noImgs):
    #symbol=cv2.imread(os.path.join(path2,str(i) + '.png'), 0)
    #noImgs = seperatorfun(symbol, path3,1,i)

#print('d,shuteshl;f,c')

for i in range(3):
    img = cv2.imread(os.path.join(path1, str(i) + '.png'),0)
    for f in range(len(img)):
        for g in range(len(img[0])):
            print(img[f][g], end=" ")
        print("\n")
    show('Grayscale',img)
    x = BINuGAU(img, 1)

    for f in range(len(x)):
        for g in range(len(x[0])):
            if x[f][g]==255:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print("\n")

    show('BinaryGaus',x)