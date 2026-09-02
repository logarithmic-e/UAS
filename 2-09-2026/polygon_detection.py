import cv2 as cv
import numpy as np

img1 = cv.imread('a.jpg', cv.IMREAD_COLOR)

img2 = cv.imread('a.jpg', cv.IMREAD_GRAYSCALE)
blurred = cv.GaussianBlur(img1 , (5,5) , 0)
threshold = cv.Canny(  blurred ,0 , 100)

contours ,_ = cv.findContours(threshold , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 400:
        approx = cv.approxPolyDP(cnt , 0.01*cv.arcLength(cnt, True) , True)
        vertices = len(approx)
        if vertices == 3 or vertices == 4 or vertices <= 12:
            cv.drawContours(img1 , [approx] , 0 , (128,0,128) , 3)

cv.imshow('image' , img1)

cv.waitKey(0)