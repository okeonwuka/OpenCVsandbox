import cv2

img = cv2.imread('coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))

cv2.imshow('thresholded', thresh)
cv2.imshow('morph', morph)
cv2.waitKey(0)
cv2.destroyAllWindows()

