import cv2
import os
import numpy as np
from ImageFun import BINuGAU
from ArrMidCrop import SumINTOarr,MIDpointARR,CROPimage
from  mask import changelist,maskfunction

def seperatorfun(img,path,decide,imageno):

    masksize = len(img[0]) /20
    BinImg = BINuGAU(img)
    Image4Arr = BinImg.copy()
    Image4Mask = BinImg.copy()
    cv2.waitKey(0)
    arr = SumINTOarr(Image4Arr)
    change = changelist(Image4Mask)
    image = maskfunction(Image4Mask, change, masksize)
    midlist = MIDpointARR(arr, image)
    return CROPimage(midlist, img, arr,path,decide,imageno)

def seperatorfun2(img,path,decide,imageno,glo):

    masksize = len(img[0]) /20
    BinImg = BINuGAU(img)
    Image4Arr = BinImg.copy()
    Image4Mask = BinImg.copy()
    cv2.waitKey(0)
    arr = SumINTOarr(Image4Arr)
    change = changelist(Image4Mask)
    #image = maskfunction(Image4Mask, change, masksize)
    midlist = MIDpointARR(arr, Image4Mask)
    return CROPimage(midlist, img, arr,path,decide,imageno)
