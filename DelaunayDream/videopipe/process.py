import cv2
import numpy as np


def rotate_hue(val, deg):
    return (val + deg) % 180


class Process:

    def __init__(self, triangulate=False, frame_rate=0, hue=0, saturation=1, brightness=1):
        self.__triangulate = triangulate
        self.__frame_rate = frame_rate
        self.__hue = hue
        self.__saturation = saturation
        self.__brightness = brightness

    # Triangulate
    @property
    def triangulate(self):
        return self.__triangulate

    @triangulate.setter
    def triangulate(self, triangulate):
        self.__triangulate = triangulate

    # Frame Rate
    @property
    def frame_rate(self):
        return self.__frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        self.__frame_rate = frame_rate

    # Hue
    @property
    def hue(self):
        return self.__hue

    @hue.setter
    def hue(self, hue):
        self.__hue = hue

    # Saturation
    @property
    def saturation(self):
        return self.__saturation

    @saturation.setter
    def saturation(self, saturation):
        self.__saturation = saturation / 100

    # Brightness
    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        self.__brightness = brightness / 100

    # Filter Functions
    def apply_filters(self, bgr_frame):
        hsv_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2HSV)
        hsv_frame = np.array(hsv_frame, dtype=np.float64)

        hsv_frame = self.hue_filter(hsv_frame)
        hsv_frame = self.saturation_filter(hsv_frame)
        hsv_frame = self.brightness_filter(hsv_frame)

        hsv_frame = np.array(hsv_frame, dtype=np.uint8)
        out_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
        return out_frame

    def hue_filter(self, hsv_frame):
        # scale pixel values up or down for channel 0(Hue)
        hsv_frame[:, :, 0] = rotate_hue(hsv_frame[:, :, 0], self.__hue)
        return hsv_frame

    def saturation_filter(self, hsv_frame):
        # scale pixel values up or down for channel 1(Saturation)
        hsv_frame[:, :, 1] = hsv_frame[:, :, 1] * self.__saturation
        hsv_frame[:, :, 1][hsv_frame[:, :, 1] > 255] = 255  # setting values > 255 to 255.
        return hsv_frame

    def brightness_filter(self, hsv_frame):
        # scale pixel values up or down for channel 2(Value)
        hsv_frame[:, :, 2] = hsv_frame[:, :, 2] * self.__brightness
        hsv_frame[:, :, 2][hsv_frame[:, :, 2] > 255] = 255  # setting values > 255 to 255.
        return hsv_frame
