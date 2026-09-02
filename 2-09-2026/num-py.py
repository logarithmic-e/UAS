import numpy as np
import cv2 as cv
image = cv.imread('k1.jpg')
blurred_image = cv.blur(image , (150,5))
cv.imshow("test window", blurred_image)
cv.imwrite('blurred_output.jpg', blurred_image)

cv.waitKey(0)