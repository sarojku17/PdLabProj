import cv2

#storing pixel location whose value changes
def changelist(img):
    img_height = len(img)
    img_width = len(img[0])
    change = []
    for i in range(img_height):
        for j in range(img_width - 1):
            if img[i][j] != img[i][j + 1]:
                change.append((i,j))
    return change

def changelist2(img):
    img_height = len(img)
    img_width = len(img[0])
    change = []
    for i in range(img_height):
        for j in range(img_width -5):
            if img[i][j] != img[i][j + 1]:
                if(img[i][j + 1])!=(img[i][j + 2]):
                    change.append((i,j))
                elif(img[i][j + 2]) != (img[i][j + 3]):
                    change.append((i, j))
                elif (img[i][j + 3]) != (img[i][j + 4]):
                    change.append((i, j))
                elif (img[i][j + 4]) != (img[i][j + 5]):
                    change.append((i, j))
    return change

# expanding charecters in horizontal Direction
def maskfunction(img, change, zerovectorsize):
    extend = int(zerovectorsize / 2)
    img_width = len(img[0])
    for i in range(len(change)):
        x, y = change[i]
        if (y - extend) > -1:
            img[x, y - extend:y] = 0
        else:
            img[x, 0:y] = 0
        if y + extend < img_width:
            img[x, y:y + extend] = 0
        else:
            img[x, y:img_width - 1] = 0
    cv2.imshow('image', img)
    cv2.waitKey(0)

    return img

def maskfunction2(img, change, zerovectorsize):
    extend = int(zerovectorsize / 2)
    img_rowsize = len(img)
    for i in range(len(change)):
        x, y = change[i]
        if (x- extend) > -1:
            img[x-extend:x,y] =255
        else:
            img[0:x,y] = 255
        if x + extend < img_rowsize:
            img[x:x+extend, y] = 255
        else:
            img[x:, y] = 255
    cv2.imshow('image', img)
    cv2.waitKey(0)

    return img
