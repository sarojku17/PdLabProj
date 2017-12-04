import cv2
import os
import numpy as np

def BINuGAU(img):

    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
           cv2.THRESH_BINARY,11,2)
    cv2.fastNlMeansDenoising(th3, None, 10,7, 21)
    cv2.fastNlMeansDenoising(th3, None, 10, 7, 21)
    cv2.fastNlMeansDenoising(th3, None, 10, 7, 21)
    cv2.imshow('hutesh kumar Binery Image', th3)
    cv2.fastNlMeansDenoising(th3, None, 10, 7, 21)
    cv2.waitKey(0)
    cv2.imshow('hutesh kumar Binery Image', th3)
    cv2.waitKey(0)
    return th3

def rotateImage(image,i):
    angle=90
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    path = 'E:/5th sem/PdLabProj/RotImg/'
    cv2.imwrite(str(path) + str(i) + '.png', cv2.warpAffine(image, M, (nW, nH)))
    image1=cv2.imread(os.path.join(path,str(i)+'.png'),0)
    image2=image1[3:len(image1)-3,2:len(image1[0])-2]
    cv2.imwrite(str(path)+str(i)+'.png',image2)
    #cv2.imshow('rotated image',image2)

def rotateImage2(image,i):
    angle=270
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    path = 'E:/5th sem/PdLabProj/RotNewImg/'
    cv2.imwrite(str(path) + str(i) + '.png', cv2.warpAffine(image, M, (nW, nH)))
    image1=cv2.imread(os.path.join(path,str(i)+'.png'),0)
    image2=image1[3:len(image1)-3,2:len(image1[0])-2]
    cv2.imwrite(str(path)+str(i)+'.png',image2)
    #cv2.imshow('rotated image',image2)
