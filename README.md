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

Issues tackled : Priority Score , Polygon Detection , Printing 1 Table of output
Issues left: Actual path drawing(most imp) , Elevation calculation(basic idea implemented but need refinement as it is outputting 0 instead of a value)
Time and Distance table/score calculation , proper image input and output CLI (currently I have to modify the code to add images and in future I have an idea to make a folder that saves all images made)

Need to sift through: https://docs.python.org/3/library/os.html#module-os , https://docs.python.org/3/library/pathlib.html#module-pathlib
I watched a tutorial video where they used these two libraries to get filenames and store them , I did a basic checking of this earlier 


<img width="1386" height="966" alt="image" src="https://github.com/user-attachments/assets/e72d479c-75b7-4b0f-b98b-b58fd380d076" />
Current image progress


5-09-2026

I will be adding a word file I made today that is basically this readme only but properly formatted with zero grammatical errors for refrence 

According to me this can be considered as an enlarged maze or a maze with invisible walls, so I tried to understand how pathing works in mazes.
The solutions involved an algorithm known as A* and its derivatives based on need, I tried to implement this but I couldn’t understand how to divide the image into separate nodes

For elevation, my masks are also not accurate due to some values of green overlapping 
The pathing currently goes from highest priority to least priority but it cuts into the pixels deemed non-traversable in the mask

I also didn’t understand how to rank the files based on the path score.
References:
https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image
https://www.youtube.com/watch?v=kS-CGkiPetQ


<img width="1278" height="751" alt="image" src="https://github.com/user-attachments/assets/d2d68428-4511-455a-8969-6c2e3e2ae900" />
