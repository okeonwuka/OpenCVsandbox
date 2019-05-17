"""
Notes
For the python build system for this file, I use python + virtualEnv
This points to the python interpreter for my OpenCV4 virtual environment ie "/home/oke/.virtualenvs/Opencv4"
To activate go to Menu->Tools->Command Pallete (ctr+Shift+P) then Choose ,"VirtualEnv: Activate". 
You can also deactivate with "VirtualEnv: Dectivate" fill out the path of your VirtualEnv under. 
To add a new virtual directory path, go to Menu->Tools->Command Pallete (command+Shift+P) then Choose "VirtualEnv: Add Directory"
"""

import cv2


img = cv2.imread('coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)))


#Output
cv2.imshow('thresholded', thresh)
cv2.imshow('morph', morph)
cv2.waitKey(0)
cv2.destroyAllWindows()

