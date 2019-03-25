import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('babe.JPG',0)

# Note: Adaptive and OTSU-method inherently converts color image to grayscale....so no need for explicit conversion 

#OTSU binarization thresholding syntax. Threshold is a specific pixel value that determines if other pixels are binarized to
# 0 or 1...depending if they are greater or less than the threshold value. maxval usu 255
# since this is OTSU-method, threshold is calculated for us, and is stored in 'ret'. So we just assign thresh = 0
# ret,dst = cv2.threshold(src/img,thresh,maxval,type[,dst]+cv2.THRESH_OTSU).
#where ret = optimal threshold value given by an OTSU's binarization. not important now
# dst = thresholded image
ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ret,thresh3 = cv2.threshold(img,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
ret,thresh4 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
ret,thresh5 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)

# print ret
print(ret)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()