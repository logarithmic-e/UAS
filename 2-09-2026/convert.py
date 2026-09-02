import cv2 as cv
import numpy as np
#convert rgb values

img = cv.imread('k1.jpg')

# imt_x = cv.cvtColor(img , cv.COLOR_RGB2BGR)
# img_y = cv.cvtColor(img , cv.COLOR_RGB2GRAY)
# img_z = cv.cvtColor(img , cv.COLOR_RGB2HSV )
# cv.imshow('img' , imt_x)
# cv.imshow('img_z' , img_z)
# cv.imshow('img' , img_y)

# ret ,  img_t = cv.threshold(img , 80 , 255 , cv.THRESH_BINARY)
# cv.imshow('img' , img_t)
cv.waitKey(0)