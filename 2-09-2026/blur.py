import cv2 as cv
import numpy as np

from pathlib import Path

path = "/k1.jpg"

filename = Path(path).stem

image = cv.imread('k1.jpg')

blurred_image = cv.blur(image , (151,5))

cv.imshow('',blurred_image)
final_name = filename + 'blur.jpg'
cv.imwrite(final_name , blurred_image)
cv.waitKey(0)