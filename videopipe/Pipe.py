import cv2 as cv
import os
import sys
import numpy as np

#
#First step, read the video
#
def get_frames():
    capture = cv.VideoCapture(sys.argv[1])
    rate = capture.get(cv.CAP_PROP_FPS)#get video frame rate

    capture = cv.VideoCapture(sys.argv[1])
    frame_list =[]
    while True:
        success, frame = capture.read()
        cv.imshow('Frame', frame)#display current frame-to be removed/modified
        frame_list.append(frame)
        if not success:
            break
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    
    
    capture.release()
    cv.destroyAllWindows()
    return frame_list


def apply_filter(frame):
    #
    #Apply pre-filter here
    #
    return frame

def frame_processing(frame_list):
    processed_frames = []
    return processed_frames


    
def apply_triangulation(frames):
    triangulated_frames=[]
    #
    #Do triangulation here
    #
    return triangulated_frames

def generate_result(frames,rate,size):
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    #size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)),
    #int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
    out = cv.VideoWriter('sampleout.avi',fourcc,rate,size,True)
    for frame in frames:
        out.write(frame)