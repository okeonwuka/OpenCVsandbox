
import cv2

img = cv2.imread('babe.JPG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('babe_gray.JPG', gray)