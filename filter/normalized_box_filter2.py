import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('babe.JPG')

blurred = cv2.blur(img,(5,5))

#save blurred image to file
cv2.imwrite('babe_Blurred2.JPG',blurred)

# show both images
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blurred),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()