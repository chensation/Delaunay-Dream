import cv2 as cv
import os
import sys
import numpy as np

#
#First step, read the video
#
capture = cv.VideoCapture(sys.argv[1])
rate = capture.get(cv.CAP_PROP_FPS)#get video frame rate
fourcc = cv.VideoWriter_fourcc(*'XVID')
size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
out = cv.VideoWriter('sampleout.avi',fourcc,rate,size,True)
index =1
while True:
    success, frame = capture.read()
    cv.imshow('Frame', frame)#display current frame-to be removed/modified
    #
    #Apply pre-filter here
    #


    #
    #Generate points here
    #


    #
    #Do triangulation here
    #


    #
    #Apply post-filter here
    #

    #
    #Output result here
    #

    out.write(frame)
    index += 1
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    if not success:
        break

capture.release()
cv.destroyAllWindows()