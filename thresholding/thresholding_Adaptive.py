import cv2
# import numpy as np
# from matplotlib import pyplot as plt
img = cv2.imread('babe.JPG',0)

# Note: Adaptive and OTSU-method can inherently converts color image to grayscale....so no need for explicit conversion 


# The concept of adaptive thresholding is to have local thresholds on different parts
# of the image, and not a global threshold across entire image (like in OTSU-binarization)
# Syntax:
# thresh = cv.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blocksize,C[,dst])
# where 
# adaptiveMethod = Gaussain or Average;
# thresholdType =  eg cv2.THRESH_TRUNC or cv2.THRESH_BINARY_INV etc
# blocksize = size of kernel/block where local thresholds will apply, 
# maxValue = 255 (usu)
# C-value: value subtracted from each pixel in resulting image.....sort of a tweaking variable to tune resulting image

thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,7,10)

# show output
# cv2.imshow('ThresholdedAdaptiveImage1',thresh)
# # hold off/ show imshow window till keybord input (number 0)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# save output
cv2.imwrite('ThresholdedAdaptiveImage.JPG', thresh)