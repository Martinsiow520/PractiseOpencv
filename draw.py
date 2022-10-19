import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')


# paint the image a certain colour

#blank[50:100, 300:450] = 0, 255,0
# draw a rectangle
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//3), 
#(0,255,0), thickness =-1)

#draw circle
#cv.circle(blank, (250,250), 100, (250,250,250), thickness =-1)

#draw line
#cv.line( blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), 
#(0,255,0), thickness =1)
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX,
 1.0, (0,255,0),1)
cv.imshow('Blank', blank)
cv.waitKey(0)