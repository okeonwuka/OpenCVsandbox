


import cv2

#import image
img = cv2.imread('babe.JPG')

#convert image to grayscale for thresholding 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#thresholding syntax. Threshold is a specific pixel value that determines if other pixels are binarized to
# 0 or 1...depending if they are greater or less than the threshold value. maxval usu 255
# ret,dst = cv2.threshold(src/img,thresh,maxval,type[,dst]).
#where ret = optimal threshold value given by an OTSU's binarization. not important now
# dst = thresholded image
ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('thresholded',thresh)

# hold off/ show imshow window till keybord input (number 0)
cv2.waitKey(0)

cv2.destroyAllWindows()
