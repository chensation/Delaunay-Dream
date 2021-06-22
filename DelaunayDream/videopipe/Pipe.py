import cv2 as cv
import os
import sys
import numpy as np

def get_frames(filename):
    """ read the video according to filename,
        return list containing all frames
    """
    cap = cv.VideoCapture(filename)
    fps = cap.get(cv.CAP_PROP_FPS)#get video frame rate
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)  
    frame_list =[]
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        #cv.imshow('Frame', frame)#display current frame-to be removed/modified
        frame_list.append(frame)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    print("All frames loaded")
    
    cap.release()
    cv.destroyAllWindows()
    return frame_list, fourcc, fps, size


def apply_filter(frame):
    """ TODO:Apply pre-filter here
    """
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)# for testing
    return gray

def frame_processing(frame_list):
    processed_frames = []
    return processed_frames


    
def apply_triangulation(frames):
    triangulated_frames=[]
    return triangulated_frames

def generate_gray(frames,fourcc,fps,size):
    out_gray = cv.VideoWriter('sampleout1.avi',fourcc,fps,size,False)
    for frame in frames:
        out_gray.write(frame)
    print("Write finished")

def generate_color(frames,fourcc,fps,size):
    out_color = cv.VideoWriter('sampleout1.avi',fourcc,fps,size,True)
    for frame in frames:
        out_color.write(frame)
    print("Write finished")