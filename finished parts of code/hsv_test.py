import numpy as np
import cv2 as cv
img = cv.imread('IMG-20260831-WA0028.jpg')

img_test =cv.cvtColor (img , cv.COLOR_BGR2HSV)

lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])
mask_black = cv.inRange(img_test, lower_black, upper_black)
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255]) 
mask_blue = cv.inRange(img_test, lower_blue, upper_blue) 
#mask_blue = cv.inRange(img_test, lower_blue, upper_blue)

mask = cv.bitwise_not(cv.bitwise_or(mask_black, mask_blue))
cv.imshow('img' , mask)

cv.waitKey(0)