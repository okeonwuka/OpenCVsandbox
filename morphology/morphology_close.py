import cv2
img = cv2.imread('babe.JPG')

#Convert to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Get thresholded image
# Notice if kernel size was 1x1 it will be adaptivethresh ie no change
# thresh = cv.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blocksize,C[,dst])
thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,10)

# morphology 'close' composite operation
#cv2.morphologyEx(src,cv2.MORPH_CLOSE......) Remember to try different kernel sizes for diff results
morph_closed = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))

# save file
cv2.imwrite('morph_closeed.jpg',morph_closed)

# Show original thresholded image
cv2.imshow('thresholded image', thresh)

# show morph opened image
cv2.imshow('morph_closed', morph_closed)
cv2.waitKey(0)
cv2.destroyAllWindows()

