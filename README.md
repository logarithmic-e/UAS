# UAS
Work done for UAS round 2 selection

1/09/2026 

Read the material provided , setup python opencv and other requirements , practiced some basic python programs to get up and running

8:55 PM : Opened MIT Open Course Ware after finishing the 6 chapters provided , also studying the Open CV documentation

2/09/2-26

Learned openCV functions : how to blur images, grayscale , threshold 
Started main project

Referred to : https://www.youtube.com/watch?v=kS-CGkiPetQ
              https://www.youtube.com/watch?v=eDIj5LuIL4A
              https://youtu.be/aFNDh5k3SjU?si=lfSG3lRGb3ETLE5q
             
Currently working on learning the polygon detection , mask making , color detection via Open CV

Also , made the steps I will take to tackle the problem statement:
# load image
# convert colorspace from rgb to hsv
# threshold
# mask
# hsv values of all injured
# identify cords of center of these polygons
# hierarchy these cords according to score
# chart path using mask and score

2-09-2026 : I have finally generated masks onto to the hsv of injured
example : <img width="1277" height="750" alt="image" src="https://github.com/user-attachments/assets/2232843f-2f95-4388-b913-c2ff797520cc" />

3-09-2026: Working on polygon detection and simultaneous colour detection

Resources currently using   : https://stackoverflow.com/questions/34203311/detect-star-shape-in-opencv-python
                              https://learnopencv.com/contour-detection-using-opencv-python-c/
                              https://stackoverflow.com/questions/40203932/drawing-a-rectangle-around-all-contours-in-opencv-python
                              https://stackoverflow.com/questions/20912948/color-detection-using-opencv-python?rq=4
                              https://stackoverflow.com/questions/59442860/how-can-i-make-certain-pixels-transparent-in-opencv
4/09/2026

Referring to:
https://medium.com/@sardorabdirayimov/colors-detection-using-masks-contours-in-opencv-72d127f0797e
