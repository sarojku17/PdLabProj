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

