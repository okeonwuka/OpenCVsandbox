import cv2
import numpy as np
from matplotlib import pyplot as plt

#original image
img = cv2.imread('babe.JPG')

# this is a A 5x5 averaging filter kernel
kernel = np.ones((5,5),np.float32)/25

dst_image = cv2.filter2D(img,-1,kernel)

#save blurred image to file
cv2.imwrite('babe_2D-conv.JPG',dst_image)

# show both images
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst_image),plt.title('babe_2D-conv : Averaging')
plt.xticks([]), plt.yticks([])
plt.show()