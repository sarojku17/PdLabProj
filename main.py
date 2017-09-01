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
newImage = images[1].copy()
newImage1 = images[1].copy()
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
print(arr[0],arr[1])
midlist=[0];
while start + counter <len(arr):
    #print('start+counter ', start + counter, 'start', start, 'counter', counter, 'arr[start+counter]',arr[start + counter], '0.90*len(x[0]', 0.90 * len(x[0]))
    if arr[start+counter]>0.98*len(x[0]):
     #   print(arr[start + counter] > 0 * len(x[0]))
      #  print(start+counter)
       # print(arr[start + counter])
        #print(0.90 * len(x[0]))
        counter=counter+1
        #print('hyi')
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
        #print('hyi1')

cv2.imshow('image',newImage)
cv2.waitKey(0)

kernel = np.zeros((20,20),np.uint8)
newImage = cv2.dilate(newImage,kernel,iterations = 1)
for i in range(len(midlist)):
    cv2.line(newImage,(0,int(midlist[i])),(len(x[0]),int (midlist[i])),(0,0,255))
cv2.imshow('image',newImage)
cv2.waitKey(0)

for i in range(len(midlist)-1):
    roi = img[int(midlist[i]):int(midlist[i+1]),0:len(x[0])]
    cv2.imshow('ROI',roi)
    cv2.waitKey(0)
