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

# Apply thresholding
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

#Apply Morph operation
# there are several composite morph operations: MORPH_CLOSE, MORPH_OPEN etc
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)))


#Output
#show output
titles = ['Original Image','Thresholded Image','Morphologically Filtered Image']
images = [img, thresh,morph]
for i in range(3):
    plt.subplot(3,1,i+1),plt.imshow(images[i],'gray') # 3 = no of rows, 1 = no of columns
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()