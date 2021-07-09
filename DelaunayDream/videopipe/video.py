import cv2 as cv


class Video:

    def __init__(self, name=""):
        self.frame_list = []
        self.fourcc = None
        self.fps = 0
        self.output_fps = 0
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

            # if cv.waitKey(20) & 0xFF == ord('d'):
            #     break
        cap.release()
        # cv.destroyAllWindows()

    def export_video(self, filename, have_color=True):
        writer = cv.VideoWriter(filename, self.fourcc, self.output_fps, self.video_size, have_color)
        for frame in self.result_frames:
            writer.write(frame)

    # TODO: move this into load_video once the gui is ready
    def apply_output_framerate(self, alt_fps):
        if alt_fps == self.fps:
            self.result_frames = self.frame_list
            return
        self.result_frames.clear()
        self.output_fps = alt_fps
        step_size = int(self.fps/self.output_fps)
        step = 1

        for frame in self.frame_list:
            if step == 1:
                self.result_frames.append(frame)
            elif step == step_size:
                step = 0
            step += 1

    def process_video(self, func):
        self.result_frames = list(map(func, self.result_frames))

    # """ try: output video with specified fps
    # """
    # def generate_with_fps(self, filename,alt_fps):
    #     out_color = cv.VideoWriter(filename, self.fourcc, alt_fps, self.video_size, True)
    #     step_size = self.fps/alt_fps
    #     frame_buf = None
    #     out_frames = []
    #     step = 1
    #     for frame in self.result_frames:
    #         if step == 1:
    #             frame_buf = frame
    #             #out_color.write(frame)
    #             out_frames.append(frame)
    #         elif step == step_size:
    #             step = 0
    #             #out_color.write(frame_buf)
    #         # else:
    #         #   out_color.write(frame_buf)
    #         step += 1
    #     for frame in out_frames:
    #         out_color.write(frame)
