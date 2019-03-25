import cv2
img = cv2.imread('babe.JPG')

#Convert to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Get thresholded image
# Notice if kernel size was 1x1 it will be adaptivethresh ie no change
# thresh = cv.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blocksize,C[,dst])
thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,10)

# erosion
#cv2.erode(src,kernel......)
eroded = cv2.erode(thresh, cv2.getStructuringElement(cv2.MORPH_RECT,(3,1)))

# save file
cv2.imwrite('Erosion.jpg',eroded)

# show image
cv2.imshow('Erosion', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

