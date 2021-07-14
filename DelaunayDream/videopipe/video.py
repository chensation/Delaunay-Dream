import cv2 as cv
import math
import multiprocessing
from multiprocessing import shared_memory
import multiprocessing as mp
import numpy as np

class Video:

    def __init__(self, name=""):
        self.frame_list = ()
        self.fourcc = None
        self.fps = 0
        
        self.output_fps = 0
        self.video_size = ()
        self.result_frames = ()
        self.filename = name

    def get_frames(self):
        """ read the video according to filename,
            return list containing all frames
        """
        # del self.frame_list
        # del  self.result_frames
        placeHolder = []
        cap = cv.VideoCapture(self.filename)
        self.fps = math.ceil(cap.get(cv.CAP_PROP_FPS)) # get video frame rate, use ceil as 23.976 fps is a popular format
        self.fourcc = cv.VideoWriter_fourcc(*'XVID')
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.video_size = (width, height)

        while True:
            success, frame = cap.read()
            if not success:
                break
            # cv.imshow('Frame', frame)#display current frame-to be removed/modified
            placeHolder.append(frame)
            # self.frame_list.append(frame)
            # self.result_frames.append(frame, axis=0)

            # if cv.waitKey(20) & 0xFF == ord('d'):
            #     break
        cap.release()

        self.frame_list = np.array(placeHolder)
        self.result_frames = np.array(placeHolder)
        del placeHolder
        # cv.destroyAllWindows()

    def export_video(self, filename, have_color=True):
        writer = cv.VideoWriter(filename, self.fourcc, self.output_fps, self.video_size, have_color)
        for frame in self.result_frames:
            writer.write(frame)

    # TODO: move this into load_video once the gui is ready
    def apply_output_framerate(self, alt_fps):
        placeHolder = []
        self.output_fps = alt_fps
        step_size = int(self.fps/self.output_fps)

        if step_size == 1:
            self.result_frames = self.frame_list.copy()
            return

        for index, frame in enumerate(self.frame_list):
            if index % step_size == 0:
                placeHolder.append(frame)

        self.result_frames = np.array(placeHolder)


    # def process_video(self, func):
        # newFrames = [None]*len(self.result_frames)
        # newFrames[:] = self.result_frames[:]
        # print("Starting this curse")
        # with mp.Pool(processes= mp.cpu_count()) as pool:
        #     self.result_frames = list(pool.imap(func, newFrames, 20))
        # self.result_frames = list(map(func, self.result_frames))

    def process_video(self, func):
        # inputFrames = self.result_frames
        Q1 = len(self.result_frames)//4
        Q2 = Q1 * 2
        Q3 = Q1 *3

        # inputArray = np.array(inputFrames)
        shm = shared_memory.SharedMemory(create=True, size=self.result_frames.nbytes)
        sharedArray = np.ndarray(self.result_frames.shape, dtype=self.result_frames.dtype, buffer=shm.buf)
        sharedArray = self.result_frames.copy()

        Q1out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(func, shm.name, inputFrames[:Q1], 1, Q1, sharedArray.shape, sharedArray.dtype))
        Q2out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(func, shm.name, inputFrames[Q1:Q2], 2, Q1, sharedArray.shape, sharedArray.dtype))
        Q3out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(func, shm.name, inputFrames[Q2:Q3], 3, Q1, sharedArray.shape, sharedArray.dtype))
        Q4out = multiprocessing.Process(target = self.process_frames_sharedMem, args=(func, shm.name, inputFrames[Q3:], 4, Q1, sharedArray.shape, sharedArray.dtype))

        Q1out.start()
        Q2out.start()
        Q3out.start()
        Q4out.start()

        Q1out.join()
        Q2out.join()
        Q3out.join()
        Q4out.join()

        self.result_frames = sharedArray.copy()

        del sharedArray
        shm.close()
        shm.unlink()
    
    def process_frames_sharedMem(self, func, sharedMemName, inputArray, q, Q1, shape, dataType):
        print("Starting process", q )
        shm = shared_memory.SharedMemory(name=sharedMemName)
        sharedArray = np.ndarray(shape, dtype=dataType, buffer=shm.buf)

        inputList = list(inputArray)
        # processedList = list(map(func, inputList))
        processedList = self.process_frames(inputList, func)

        processedArray = np.array(processedList)
        if q==1:
            sharedArray[:q*Q1] = processedArray[:]
        elif q==4:
            sharedArray[(q-1)*Q1:] = processedArray[:]
        else:
            sharedArray[(q-1)*Q1:q*Q1] = processedArray[:]

        shm.close()
        print("Q", q, "processed")

    def process_frames(self, inputFrames, func):
        outputFrames = [None]*len(inputFrames)
        # Q1 = len(outputFrames)//4
        # print("Processing frames")
        for index, frame in enumerate(inputFrames):
            # if index % Q1 == 0: print(" . ", end='', flush=True)
            outputFrames[index] = func(frame)
        # print("Num Frames processed: ", len(outputFrames))
        return outputFrames
    

    """ try: output video with specified fps
    """
    def generate_with_fps(self, filename,alt_fps):
        out_color = cv.VideoWriter(filename, self.fourcc, alt_fps, self.video_size, True)
        step_size = self.fps/alt_fps
        frame_buf = None
        out_frames = []
        step = 1
        for frame in self.result_frames:
            if step == 1:
                frame_buf = frame
                #out_color.write(frame)
                out_frames.append(frame)
            elif step == step_size:
                step = 0
                #out_color.write(frame_buf)
            # else:
            #   out_color.write(frame_buf)
            step += 1
        for frame in out_frames:
            out_color.write(frame)
