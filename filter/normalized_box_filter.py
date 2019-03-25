import cv2

from matplotlib import pyplot as plt


img = cv2.imread('babe.JPG')

# apply filter
# cv2.blur(src,kernel-size.....)
blurred = cv2.blur(img,(5,5))

# output blurred/filtered image
plt.imshow(blurred, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv2.imwrite('babe_Blurred.JPG', blurred)


#output original image
plt.imshow(img, cmap = 'hot', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# show both images
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blurred),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
