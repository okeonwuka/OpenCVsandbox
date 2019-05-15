"""
Notes
For the python build system for this file, I use python + virtualEnv
This points to the python interpreter for my OpenCV4 virtual environment ie "/home/oke/.virtualenvs/Opencv4"
To activate go to Menu->Tools->Command Pallete (command+Shift+P) then Choose ,"VirtualEnv: Activate". 
You can also deactivate with "VirtualEnv: Dectivate" fill out the path of your VirtualEnv under. 
To add a new virtual directory path, go to Menu->Tools->Command Pallete (command+Shift+P) then Choose "VirtualEnv: Add Directory"
"""


# This code blends 2 images together, according to their alpha (opacity) value
# The image with higher alpha value will be the more prominent image in the blend
# Both input images have to be the same size for this to work

# Import opencv
import cv2;


#load input image1
img1 = cv2.imread('blend1.JPG');

#load input image2
img2 = cv2.imread('blend2.JPG');

# Give alpha (OPACITY) value
alpha = 0.5;

# output image
result = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0);

# Save result
cv2.imwrite('blended1.JPG', result)