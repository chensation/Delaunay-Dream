import cv2 as cv
import os
import sys
import numpy as np

capture = cv.VideoCapture('Samples/sample1.mp4')
fps = capture.get(cv.CAP_PROP_FPS)#get video frame rate
fourcc = cv.VideoWriter_fourcc(*'XVID')
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
out_gray = cv.VideoWriter('sampleout.avi',fourcc,fps,size,False)
out_color = cv.VideoWriter('sampleout.avi',fourcc,fps,size,True)
#
#First step, read the video
#
def get_frames():
    frame_list =[]
    while True:
        success, frame = capture.read()
        if not success:
            break
        cv.imshow('Frame', frame)#display current frame-to be removed/modified
        frame_list.append(frame)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    
    
    capture.release()
    cv.destroyAllWindows()
    return frame_list


def apply_filter(frame):
    
    #
    #Apply pre-filter here
    #
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)# for testing
    return gray

def frame_processing(frame_list):
    processed_frames = []
    return processed_frames


    
def apply_triangulation(frames):
    triangulated_frames=[]
    #
    #Do triangulation here
    #
    return triangulated_frames

def generate_gray(frames):
    for frame in frames:
        out_gray.write(frame)

def generate_color(frames):
    for frame in frames:
        out_color.write(frame)