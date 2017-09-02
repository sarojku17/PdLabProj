import cv2
import numpy as np
from ImageFun import BINuGAU,rotateImage
from ArrMidCrop import SumINTOarr,MIDpointARR,CROPimage
from  mask import changelist,maskfunction

def seperatorfun(img,path):
    readRot = cv2.imread(os.path.join(path, str(i) + '.png'), 0)
    masksize = len(img[0]) / 15
    BinImg = BINuGAU(img)
    Image4Arr = BinImg.copy()
    Image4Mask = BinImg.copy()
    cv2.imshow('BinaryImage', BinImg)
    cv2.waitKey(0)
    arr = SumINTOarr(Image4Arr)
    change = changelist(Image4Mask)
    image = maskfunction(Image4Mask, change, masksize)
    midlist = MIDpointARR(arr, image)
    noImgs = CROPimage(midlist, img, arr,path)