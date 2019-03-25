# Code draws rect, square etc on Image
# The drawing is stored in memory, and not actually on the image file
# To store drwaing in image file, use 'cv2.imwrite'
# the x,y origin for pixels in OpenCv is at the top left of the image.
# This means that x increases from left to right and y increases from top to bottom

import cv2

#load input image
img1 = cv2.imread('DrawOnImage.JPG')
img2 = cv2.imread('DrawOnImage.JPG')
img3 = cv2.imread('DrawOnImage.JPG')
img4 = cv2.imread('DrawOnImage.JPG')

# Draw a diagonal blue line with thickness of 5 px
result1 = cv2.line(img1,(0,0),(5011,5011),(255,0,0),5)

# Draw a blue line with thickness of 5 px
# cv2.line(img, pt1(x,y), pt2(x,y), color[, thickness[, lineType[, shift]]])
result2 = cv2.line(img2,(20,2000),(5011,2000),(255,0,0),5)

# Draw green rectangle at the top-right corner of image thickness 10
# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.
# cv2.rectangle(img, pt1(x,y), pt2(x,y), color[, thickness[, lineType[, shift]]])
result3 = cv2.rectangle(img3,(384,0),(510,128),(0,255,0),10)

# Draw solid circle (thickness = -1)
# cv2.circle(img, center(x,y), radius, color[, thickness[, lineType[, shift]]])
result4 = cv2.circle(img4,(4470,1000), 630, (0,0,255), -1)






#Write to new file
cv2.imwrite('DrawDiagLineOnImage.JPG', result1)
cv2.imwrite('DrawLineOnImage.JPG', result2)
cv2.imwrite('DrawRectOnImage.JPG', result3)
cv2.imwrite('DrawCirOnImage.JPG', result4)