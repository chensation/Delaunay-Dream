import cv2 as cv
import math
from multiprocessing import shared_memory
import multiprocessing as mp
import numpy as np
from moviepy.editor import *
import uuid
import os


class Video:

    def __init__(self, name=""):
        self._fourcc = None
        self._fps = 0
        
        self._video_size = ()
        self._frames = ()
        self._audio = ()
        self._filename = name

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, str):
        self._filename = str

    @property
    def framerate(self):
        return self._fps

    @framerate.setter
    def framerate(self, fps):
        self._fps = fps

    @property
    def frames(self):
        return self._frames

    def get_fps_from_file(self):

        result = cv.imread(self._filename)

        if result is not None:
            raise ValueError("Invalid file type")

        cap = cv.VideoCapture(self._filename)
        success, _ = cap.read()

        if not success:
            raise ValueError("Unable to open file")


        fps =  math.ceil(cap.get(cv.CAP_PROP_FPS))
        cap.release()

        return fps

    def load_frames(self):
        """ read the video according to filename,
        """

        temp_array = []
        try:
            cap = cv.VideoCapture(self._filename)
            self._audio = AudioFileClip(self._filename)
            self._frames = ()
            original_fps = math.ceil(cap.get(cv.CAP_PROP_FPS)) # get video frame rate, use ceil as 23.976 fps is a popular format
            self._fourcc = cv.VideoWriter_fourcc(*'XVID')
            width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
            height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
            self._video_size = (width, height)

            if not self._fps:
                self._fps = original_fps

            # only read frames needed for the target fps
            step_size = int(original_fps/self._fps)
            curr_index = 0
            while True:
                success, frame = cap.read()
                if not success:
                    break

                if curr_index % step_size == 0:
                    temp_array.append(frame)

                curr_index += 1

            self._frames = np.asarray(temp_array)
        except Exception:
            raise ValueError(f"Unabled to read from {self._filename}")
        finally:
            cap.release()

    def export_video(self, filename, have_color=True):

        tempfile = str(uuid.uuid4())+'.avi'

        writer = cv.VideoWriter(tempfile, self._fourcc, self._fps, self._video_size, have_color)
        for frame in self._frames:
            writer.write(frame)
        writer.release()

        clip = VideoFileClip(filename= tempfile)
        clip = clip.set_audio(self._audio)
       
        clip.write_videofile(filename, codec = 'libx264')
        del clip
        if os.path.exists(tempfile):
            os.remove(tempfile)

    def process_video(self, func):

        Q1 = self._frames.shape[0]//4
        Q2 = Q1 * 2
        Q3 = Q1 * 3

        shm = shared_memory.SharedMemory(create=True, size=self._frames.nbytes)
        shared_array = np.ndarray(self._frames.shape, dtype=self._frames.dtype, buffer=shm.buf)
        shared_array[:] = self._frames[:]
        self._frames = ()

        Q1out = mp.Process(target=process_shared_mem, args=(func, shm.name, 0, Q1, shared_array.shape, shared_array.dtype))
        Q2out = mp.Process(target=process_shared_mem, args=(func, shm.name, Q1, Q2, shared_array.shape, shared_array.dtype))
        Q3out = mp.Process(target=process_shared_mem, args=(func, shm.name, Q2, Q3, shared_array.shape, shared_array.dtype))
        Q4out = mp.Process(target=process_shared_mem, args=(func, shm.name, Q3, shared_array.shape[0], shared_array.shape, shared_array.dtype))

        Q1out.start()
        Q2out.start()
        Q3out.start()
        Q4out.start()

        Q1out.join()
        Q2out.join()
        Q3out.join()
        Q4out.join()

        self._frames = shared_array.copy()
        del shared_array

        shm.close()
        shm.unlink()


def process_shared_mem(func, shared_mem_name, begin, end, shape, data_type):
    shm = shared_memory.SharedMemory(name=shared_mem_name)
    shared_array = np.ndarray(shape, dtype=data_type, buffer=shm.buf)

    for index in range(begin, end):
        shared_array[index] = func(shared_array[index])

    shm.close()
