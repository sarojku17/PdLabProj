import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('EqnImage.png',0)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow('imgb',th3)
cv2.waitKey(0)


newImage = th3.copy()
x=th3
for i in range(len(x)):
    for j in range(len(x[0])):
        if (x[i][j]==255):
            x[i][j]=1
        else:
            x[i][j]=0

for i in range(len(x)):
    for j in range(len(x[0])):
       print(x[i][j], end=" ")
    print("\n")

arr=np.zeros(len(x))
for i in range(len(x)):
    arr=np.sum(x,axis=1)
    print(i,'-->',arr[i])

e=1
start=0
end=0
counter=0
midlist=[0]
while start + counter <len(arr):

    if arr[start+counter]>0.999*len(x[0]):

        counter=counter+1

        if counter>e:
            end=start+counter
            mid=(end+start)/2
            midlist.append(mid)
            start = start + counter;
            counter=0
    else:
        counter=counter+1
        start=start+counter
        counter=0

midlist.append(len(x))

for i in range(len(midlist)):
    cv2.line(newImage,(0,int(midlist[i])),(len(x[0]),int (midlist[i])),(0,0,255))
cv2.imshow('image',newImage)
cv2.waitKey(0)

print
for i in range(len(midlist)-1):
    row1=int(midlist[i])
    row2=int(midlist[i+1])
    intensity=np.sum(arr[row1:row2+1])
    if ((row2-row1+1)*len(newImage[0])*0.97)>intensity:
        roi = newImage[int(midlist[i]):int(midlist[i+1]),0:len(x[0])]
        cv2.imshow('ROI',roi)
        cv2.waitKey(0)
