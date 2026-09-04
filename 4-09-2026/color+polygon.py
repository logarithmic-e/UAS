import cv2 as cv
import numpy as np
import os
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
elevation_dict = {"ground" : 0 , "slope" : 1 , "peak" : 2}
img = cv.imread('IMG-20260831-WA0028.jpg')

hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)

mask = cv.bitwise_not(cv.bitwise_or(cv.inRange(hsv , black["lower"] , black["upper"]),cv.inRange(hsv , blue["lower"] , blue["upper"])))

# cv.imshow('test' , mask)
speeds = {0:20 , 1:15 , 2:10}
# cv.waitKey(0)
cord_of_shapes = []

mask_green = cv.inRange(hsv , green["lower"],green["upper"])
mask_red = cv.inRange(hsv , red["lower"],red["upper"])
mask_yellow = cv.inRange(hsv , yellow["lower"],yellow["upper"])
mask_orange = cv.inRange(hsv , orange["lower"],orange["upper"])
mask_purple = cv.inRange(hsv , purple["lower"],purple["upper"])
mask_white = cv.inRange(hsv , white["lower"],white["upper"])
level0_mask = cv.inRange(hsv, (30, 40, 180), (80, 255, 255))   # ground
level1_mask = cv.inRange(hsv, (30, 40, 100), (80, 255, 180))   # slope
level2_mask = cv.inRange(hsv, (30, 40, 0),   (80, 255, 100))   # peak
# cv.imshow('test' , mask_green)

# # cv.waitKey(0)
# cv.imshow('test' , mask)
# cv.waitKey(0)
# cv.imshow('test' , mask_purple)
# cv.waitKey(0)
#priority score = age score * color score

priority_score = 1


# --------------------------------
# SHAPE IDENTIFICATION
# --------------------------------


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


# -----------------------------------
# COLOR IDENTIFICATION
# -----------------------------------    


def color_identifier(hsv , name):
    if name == "green":
        return mask_green
    elif name == "red":
        return mask_red
    elif name == "yellow":
        return mask_yellow
    elif name=="white":
        return mask_white
    elif name=="purple":
        return mask_purple
    elif name=="orange":
        return mask_orange

# ---------------------------------
# ELEVATION DETECTION
# ---------------------------------

def elevation_detect(x,y):
    if level2_mask[y_mid, x_mid] > 0:
            elevation = "peak"
    elif level1_mask[y_mid, x_mid] > 0:
            elevation = "slope"
    elif level0_mask[y_mid, x_mid] > 0:
            elevation = "ground"
    else:
            elevation = "ground"


    elevation_level = elevation_dict.get(elevation)
    return elevation_level

# -------------------------------
# COLOR DETECTION
# -------------------------------

def detected_color(cnt):
    contour_mask = np.zeros(hsv.shape[:2], dtype=np.uint8)#i dont understand it that much but every website that taught color detection in open cv had this
    cv.drawContours(contour_mask, [cnt], -1, 255, -1)

    color_masks = {
        "green": mask_green,
        "red": mask_red,
        "yellow": mask_yellow,
        "orange": mask_orange,
        "purple": mask_purple,
        "white": mask_white,
    }
    matches = {
        name: cv.countNonZero(cv.bitwise_and(color_mask, contour_mask))
        for name, color_mask in color_masks.items() 
    }
    color, pixel_count = max(matches.items(), key=lambda item: item[1])
    return color if pixel_count > 0 else "Unknown"
counter = 0
example = cv.bitwise_xor(mask_green , mask)
#after sharing the issue on whatsapp , I was thinking that the polygon detection is only working on those polygons whom I have subtracted i.e. the oval water bodies and rectangular walls , meaning the detection model works , so I did an eXclusive OR and now it works
contours, _ = cv.findContours(example, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
annotated_img = img.copy()

# ---------------------------------
# MAIN LOOP
# ---------------------------------


print ("Casualty" + " " + "Score" +" "+ "Co-Ordinates" + " "+"Elevation")
for cnt in contours:
    if cv.contourArea(cnt) < 200:
            continue
            
            
    color = detected_color(cnt)
    priority_score = shapes.get(shape_identifier(cnt), 0) * color_scores.get(color, 0)
    
    
    x,y,w,h = cv.boundingRect(cnt)
    
    x1 = max(0,x)
    x2= min(img.shape[1] , x+w)
    x_mid = round((x1 + x2)/2)
    y1 = max(0,y)
    y2 = min(img.shape[0] , y+h)
    y_mid = round((y1 + y2)/2)


    elevation = elevation_detect(y_mid,x_mid)

    cord_of_shapes.append(priority_score + x_mid + y_mid)
    centre_of_shape = (x_mid , y_mid)
    cv.circle(annotated_img,  centre_of_shape ,radius=2,color= (102 , 255 , 255) , thickness=-1 )
    cv.rectangle(annotated_img , (x1,y1),(x2,y2) , (128,128,255) , 2)
    label = color.capitalize()+ "/ " + shape_identifier(cnt) +" "+ "Priority:" + str(priority_score) + " "+"elevation:" + str(elevation)
    text_size, _ = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.4, 2)
    text_x = max(0, x + (w - text_size[0]) // 2)
    text_y = y1 - 8 if y1 > text_size[1] + 8 else y1 + text_size[1] + 8
    cv.putText(annotated_img, label, (text_x, text_y),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv.LINE_AA)
    print(color+shape_identifier(cnt) + " " + str(priority_score) + " " + str(centre_of_shape) + " " + str(elevation))
    counter = counter + 1

# if cord_of_shapes:
#     print(cord_of_shapes[0])
# else:
#     print("No valid shapes detected")

cv.imshow('test' , annotated_img)
cv.waitKey(0)
