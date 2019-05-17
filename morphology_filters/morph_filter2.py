"""
Notes
For the python build system for this file, I use python + virtualEnv
This points to the python interpreter for my OpenCV4 virtual environment ie "/home/oke/.virtualenvs/Opencv4"
To activate go to Menu->Tools->Command Pallete (ctr+Shift+P) then Choose ,"VirtualEnv: Activate". 
You can also deactivate with "VirtualEnv: Dectivate" fill out the path of your VirtualEnv under. 
To add a new virtual directory path, go to Menu->Tools->Command Pallete (command+Shift+P) then Choose "VirtualEnv: Add Directory"
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg')

# convert image to gray as thresholding preprocessing step
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholded image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

# first Morph operation
morph1 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))

# second morph operation: Speckles actually removed
morph2 = cv2.morphologyEx(morph1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))

# cv2.imshow('thresholded', thresh)
# cv2.imshow('morph', morph)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#show output
titles = ['Original Image','Thresholded Image','Morphologically Filtered Image 1',
'Morphologically Filtered Image 2']
images = [img, thresh,morph1,morph2]
for i in range(4):
    plt.subplot(4,1,i+1),plt.imshow(images[i],'gray') # 3 = no of rows, 1 = no of columns
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()