import cv2

img = cv2.imread('coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

dilated = cv2.dilate(thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)))

cv2.imshow('thresholded', thresh)
cv2.imshow('dilated', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

