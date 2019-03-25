import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# in thresholding, images have to be converted to grayscale
img = cv2.imread('babe.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('babe_gray.JPG', gray)

#thresholding syntax. Threshold is a specific pixel value that determines if other pixels are binarized to
# 0 or 1...depending if they are greater or less than the threshold value. maxval usu 255
# retval,dst = cv2.threshold(src/img,thresh,maxval,type[,dst]).
#where ret = optimal threshold value given by an OTSU's binarization. not important now
# dst = thresholded image
img2 = cv2.imread('babe_gray.JPG')
ret,thresh1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)

cv2.imwrite('ThresholdedImage1.JPG', thresh1)