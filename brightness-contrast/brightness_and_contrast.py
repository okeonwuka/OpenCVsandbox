import cv2
import numpy as np

#Read in image file
img = cv2.imread('babe.JPG')

#Input constants for image matrix brightness and constrast modification
# alpha rep contrast constant
alpha = 2
# beta rep brightness constant
beta = 50

# apply addWeighted function to image to generate modified image
result = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)

#store the result
cv2.imwrite('babe_bc.JPG', result)