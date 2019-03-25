# Dilation is opposite of erosion
import cv2
img = cv2.imread('babe.JPG')

#Convert to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Get thresholded image
# thresh = cv.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blocksize,C[,dst])
thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,10)

# dilate
#cv2.dilate(src,kernel...... 
# Notice if kernel size was 1x1 it will be adaptivethresh ie no change
dilated = cv2.dilate(thresh, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))) 


# save file
cv2.imwrite('Dilation.jpg',dilated)

# show image
cv2.imshow('Dilation', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

