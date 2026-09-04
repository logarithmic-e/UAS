import cv2 as cv
import numpy as np
#i wanted something similar to C structs so I am using dicts

#colors
black = dict(lower = np.array([0,0,0]) , upper = np.array([180,255,50]))
green = dict(lower=np.array([35, 40, 40]), upper=np.array([85, 255, 255]))
orange = dict(lower=np.array([10, 150, 150]), upper=np.array([20, 255, 255]))
blue = dict(lower = np.array([100, 150, 50]) , upper = np.array([140, 255, 255]) )
red = dict(lower=np.array([0, 120, 70]), upper=np.array([9, 255, 255]))
yellow = dict(lower=np.array([21, 100, 100]), upper=np.array([34, 255, 255]))
white = dict(lower=np.array([0, 0, 200]), upper=np.array([180, 40, 255]))
purple = dict(lower=np.array([120, 60, 60]), upper=np.array([160, 255, 255]))

#shape scores
shapes = {"Circle" : 3, "Star" : 1 , "Square" : 2}
color_scores = {"red" : 3 , "yellow" : 2 , "white" : 1}
age = {"Circle" : "Children" , "Star" : "Adults" , "Square" : "Senior Citizens"}

img = cv.imread('IMG-20260831-WA0028.jpg')

hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)

mask = cv.bitwise_not(cv.bitwise_or(cv.inRange(hsv , black["lower"] , black["upper"]),cv.inRange(hsv , blue["lower"] , blue["upper"])))

# cv.imshow('test' , mask)

# cv.waitKey(0)

mask_green = cv.inRange(hsv , green["lower"],green["upper"])
mask_red = cv.inRange(hsv , red["lower"],red["upper"])
mask_yellow = cv.inRange(hsv , yellow["lower"],yellow["upper"])
mask_orange = cv.inRange(hsv , orange["lower"],orange["upper"])
mask_purple = cv.inRange(hsv , purple["lower"],purple["upper"])
mask_white = cv.inRange(hsv , white["lower"],white["upper"])
# cv.imshow('test' , mask_green)

# # cv.waitKey(0)
# cv.imshow('test' , mask)
# cv.waitKey(0)
# cv.imshow('test' , mask_purple)
# cv.waitKey(0)



def shape_identifier(cnt):
    perimeter = cv.arcLength(cnt , True)
    approx = cv.approxPolyDP(cnt , 0.01*perimeter , True)
    vertices = len(approx)
#for star:https://stackoverflow.com/questions/34203311/detect-star-shape-in-opencv-python
    area = cv.contourArea(cnt)
#hull as star is a difficult shape , others are proper convex but here it is convex and concave(my understanding) , this is also why in previous attempts , polygon detected only rectangles
    hull = cv.convexHull(cnt)
    hull_area = cv.contourArea(hull)
    if hull_area == 0:
     return "Unknown"
    solid = float(area)/hull_area

    if vertices == 3:
        return "Triangle"
    elif vertices == 4:
        return "Square"
    elif solid < 0.75:
        return "Star"
    elif vertices >= 5:
        return "Circle"
def color_identifier(hsv , name):
    if name == "red":
        return mask_red
    elif name == "yellow":
        return mask_yellow
    elif name=="white":
        return mask_white
    elif name=="purple":
        return mask_purple
    elif name=="orange":
        return mask_orange

example = cv.bitwise_xor(mask_green , mask)
contours, _ = cv.findContours(example, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
annotated_img = img.copy()
for cnt in contours:
    if cv.contourArea(cnt) < 200:
            continue
    label = shape_identifier(cnt)
    
    x,y,w,h = cv.boundingRect(cnt)
    
    x1 = max(0,x)
    x2= min(img.shape[1] , x+w)
    y1 = max(0,y)
    y2 = min(img.shape[0] , y+h)
    
    cv.rectangle(annotated_img , (x1,y1),(x2,y2) , (128,128,255) , 2)

    text_size, _ = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    text_x = max(0, x + (w - text_size[0]) // 2)
    text_y = y1 - 8 if y1 > text_size[1] + 8 else y1 + text_size[1] + 8
    cv.putText(annotated_img, label, (text_x, text_y),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv.LINE_AA)

cv.imshow('test' , annotated_img)
cv.waitKey(0)
