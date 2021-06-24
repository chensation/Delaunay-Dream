import cv2 as cv


class Video:

    def __init__(self, name=""):
        self.frame_list = []
        self.fourcc = None
        self.fps = 0
        self.video_size = ()
        self.result_frames = []
        self.filename = name

    def get_frames(self):
        """ read the video according to filename,
            return list containing all frames
        """
        self.frame_list.clear()
        self.result_frames.clear()
        cap = cv.VideoCapture(self.filename)
        self.fps = cap.get(cv.CAP_PROP_FPS)  # get video frame rate
        self.fourcc = cv.VideoWriter_fourcc(*'XVID')
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.video_size = (width, height)

        while True:
            success, frame = cap.read()
            if not success:
                break
            # cv.imshow('Frame', frame)#display current frame-to be removed/modified
            self.frame_list.append(frame)
            self.result_frames.append(0)

            # if cv.waitKey(20) & 0xFF == ord('d'):
            #     break
        cap.release()
        # cv.destroyAllWindows()

    def generate_gray(self, filename):
        out_gray = cv.VideoWriter(filename, self.fourcc, self.fps, self.video_size, False)
        for frame in self.result_frames:
            out_gray.write(frame)

    def generate_color(self, filename):
        out_color = cv.VideoWriter(filename, self.fourcc, self.fps, self.video_size, True)
        for frame in self.result_frames:
            out_color.write(frame)

    def process_video(self, func, process_original=True, *args, **kwargs):
        if process_original:
            frames = self.frame_list
        else:
            frames = self.result_frames
        for index, frame in enumerate(frames):
            self.result_frames[index] = func(frame, *args, **kwargs)
