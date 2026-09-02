import cv2 as cv

img = cv.imread('k1.jpg')
final = cv.Canny(img , 150 , 200)

cv.imshow('final',final)
cv.waitKey(0)