import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('EqnImage.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)


titles = ['Original Image','BINARY','BINARY_INV']
images = [img,thresh1,thresh2]

for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

#plt.show()
cv2.imshow('image',images[1])
cv2.waitKey(0)
x=images[1]
for i in range(len(x)):
    for j in range(len(x[0])):
        if (x[i][j]>230):
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

e=8
start=0
end=1
counter=0
print(len(arr))
while- start+counter<len(arr) :
    print(start+counter)
    counter=0
    if arr[start+counter]>0.90*len(x[0]) :
        counter=counter+1

        if counter>e:
            end=start+counter
            mid=(end+start)/2
            print(mid)
            start = start + counter;

    else:
        counter=counter+1
        start=start+counter;
    #print('y')
    break
