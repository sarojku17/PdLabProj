import cv2
import numpy as np
from ImageFun import BINuGAU,rotateImage
from ArrMidCrop import SumINTOarr,MIDpointARR,CROPimage,show
from mask import *

def seperatorfun(img,path,decide,imgno):
    #readRot = cv2.imread(os.path.join(path, str(i) + '.png'), 0)

    masksize = len(img[0]) /20
    if(decide==0):
        BinImg = BINuGAU(img,0)
    else:
        BinImg = BINuGAU(img,1)
    Image4Arr = BinImg.copy()
    Image4Mask = BinImg.copy()


    arr = SumINTOarr(Image4Arr)
    if(decide==0):
        change = changelist(Image4Mask)
        image = maskfunction(Image4Mask, change, masksize)
    else:
        change = changelist2(Image4Mask)
        image= maskfunction2(Image4Mask, change, 2)


    midlist = MIDpointARR(arr, image)
    return CROPimage(midlist, img, arr,path,decide,imgno)