import cv2
import numpy as np

def SumINTOarr(newImage):

    x=newImage
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
    return arr

def MIDpointARR(arr,th3):
    e=1
    start=0
    end=0
    counter=0
    midlist=[0]
    x = th3
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
    return midlist


def CROPimage(midlist,newImage,arr,path,decide,imageno):
    x=newImage
    for i in range(len(midlist)):
        cv2.line(newImage,(0,int(midlist[i])),(len(x[0]),int (midlist[i])),(0,0,255))
    cv2.imshow('linrd image',newImage)
    cv2.waitKey(0)
    counter=0;
    for i in range(len(midlist)-1):
        row1=int(midlist[i])
        row2=int(midlist[i+1])
        intensity=np.sum(arr[row1:row2+1])
        if ((row2-row1+1)*len(newImage[0])*0.97)>intensity:
            roi = newImage[int(midlist[i])+1:int(midlist[i+1]),0:len(x[0])]
            cv2.imshow('ROI',roi)
            if decide==0:
                cv2.imwrite(str(path) + str(counter) + '.png', roi)
            else:
                cv2.imwrite(str(path) + str(counter) +str(imageno)+ '.png', roi)

            counter=counter+1
            cv2.waitKey(0)

    return counter

