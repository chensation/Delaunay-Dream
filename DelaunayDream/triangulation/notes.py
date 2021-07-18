import cv2
import os
from timeit import timeit
import multiprocessing
from multiprocessing import shared_memory
import numpy as np
import moviepy
from moviepy.editor import *

from triangulation import Triangulation

class Note:
    def __init__(self):
        self.trigy = Triangulation()

        self.og_frames = []
        self.fourcc = None
        self.fps = 0
        self.video_size = ()
        self.result_frames = []

    def loadImg(self, fpath):
        return cv2.imread(fpath, cv2.IMREAD_COLOR)

    def pwd(self):
        return os.getcwd()

    def timeVidTrig(self, fpath, n = 1):
        vidFrames = self.get_frames(fpath)
        pTime = timeit(lambda: self.process_frames(vidFrames), number=n)
        print("Video processesed ", n,  " times, avg processTime: ", pTime/n)
    
    def timeFastVidTrig(self, fpath, n = 1):
        vidFrames = self.get_frames(fpath)
        pTime = timeit(lambda: self.process_frames_fast(vidFrames), number=n)
        print("Video processesed ", n,  " times, avg processTime: ", pTime/n)    

    def process_frames_fast(self, inputFrames):
        outputFrames = [None]*len(inputFrames)
        Q1 = len(outputFrames)//4
        Q2 = Q1 * 2
        Q3 = Q1 *3

        inputArray = np.array(inputFrames)
        shm = shared_memory.SharedMemory(create=True, size=inputArray.nbytes)
        sharedArray = np.ndarray(inputArray.shape, dtype=inputArray.dtype, buffer=shm.buf)
        sharedArray[:] = inputArray[:]

        print("Processing frames")
        Q1out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(shm.name, inputFrames[:Q1], 1, Q1, sharedArray.shape, sharedArray.dtype))
        Q2out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(shm.name, inputFrames[Q1:Q2], 2, Q1, sharedArray.shape, sharedArray.dtype))
        Q3out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(shm.name, inputFrames[Q2:Q3], 3, Q1, sharedArray.shape, sharedArray.dtype))
        Q4out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(shm.name, inputFrames[Q3:], 4, Q1, sharedArray.shape, sharedArray.dtype))

        Q1out.start()
        Q2out.start()
        Q3out.start()
        Q4out.start()

        Q1out.join()
        Q2out.join()
        Q3out.join()
        Q4out.join()

        outputFrames = list(sharedArray.copy())

        del sharedArray
        shm.close()
        shm.unlink()

        return outputFrames
    
    def process_frames_sharedMem(self, sharedMemName, inputArray, q, Q1, shape, dataType):
        print("Starting process", q )
        shm = shared_memory.SharedMemory(name=sharedMemName)
        sharedArray = np.ndarray(shape, dtype=dataType, buffer=shm.buf)

        inputList = list(inputArray)
        processedList = self.process_frames(inputList)
        processedArray = np.array(processedList)
        if q==1:
            sharedArray[:q*Q1] = processedArray[:]
        elif q==4:
            sharedArray[(q-1)*Q1:] = processedArray[:]
        else:
            sharedArray[(q-1)*Q1:q*Q1] = processedArray[:]

        shm.close()
        print("Q", q, "processed")
 



    def process_frames(self, inputFrames):
        outputFrames = [None]*len(inputFrames)
        # Q1 = len(outputFrames)//4
        # print("Processing frames")
        outputFrames = list(map(self.triangulate, inputFrames))
        # for index, frame in enumerate(inputFrames):
        #     if index % Q1 == 0: print(" . ", end='', flush=True)
        #     outputFrames[index] = self.triangulate(frame)
        # print("Num Frames processed: ", len(outputFrames))
        return outputFrames

    def triangulate(self, frame):
        return self.trigy.apply_triangulation(frame)

    
    def get_frames(self, fname):
        outputFrames = []

        cap = cv2.VideoCapture(fname)
        self.fps = cap.get(cv2.CAP_PROP_FPS)  # get video frame rate
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.video_size = (width, height)
        while True:
            success, frame = cap.read()
            if not success:
                break
            outputFrames.append(frame) #possibly use hstack here instead and keep everythin as np array
        cap.release()
        print("Frames loaded from video: \n\tNum Frames: ", len(outputFrames), "\n\tFrame shape: ", outputFrames[0].shape)
        
        return np.array(outputFrames)


    def combine_with_audio(self, frames, filename):
        def returnFrame(i):
            return frames[i]
        audio = AudioFileClip(filename).subclip(0,5)
        clip = ImageSequenceClip(list(frames), fps = 25).subclip(0,5)
        clip = clip.set_audio(audio)
        clip.write_videofile("movie.mp4")


if __name__ == '__main__':
    nn = Note()
    nn.timeFastVidTrig("../../../shortPexels.mp4")