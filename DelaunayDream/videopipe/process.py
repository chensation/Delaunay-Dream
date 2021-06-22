import cv2
import numpy as np

class Process:
    def __init__(self, triangulate, frame_rate, hue, saturation, brightness):
        self.__triangulate = triangulate
        self.__frame_rate = frame_rate
        self.__hue = hue
        self.__saturation = saturation
        self.__brightness = brightness
    
    def __init__(self):
        self.__triangulate = False
        self.__frame_rate = 0
        self.__hue = 0
        self.__saturation = 1
        self.__brightness = 1

    #Triangulate
    @property
    def triangulate(self):
        return self.__triangulate

    @triangulate.setter
    def triangulate(self, triangulate):
        self.__triangulate = triangulate

    #Frame Rate
    @property
    def frame_rate(self):
        return self.__frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        self.__frame_rate = frame_rate

    #Hue
    @property
    def hue(self):
        return self.__hue

    @hue.setter
    def hue(self, hue):
        self.__hue = hue

    #Saturation
    @property
    def saturation(self):
        return self.__saturation

    @saturation.setter
    def saturation(self, saturation):
        self.__saturation = saturation/100

    #Brightness
    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        self.__brightness = brightness/100

    #Filter Functions
    def applyFilters(self, bgrFrame):
        hsvFrame = cv2.cvtColor(bgrFrame, cv2.COLOR_BGR2HSV)
        hsvFrame = np.array(hsvFrame, dtype=np.float64)

        hsvFrame = self.hueFilter(hsvFrame)
        hsvFrame = self.saturationFilter(hsvFrame)
        hsvFrame = self.brightnessFilter(hsvFrame)

        hsvFrame = np.array(hsvFrame, dtype=np.uint8)
        outFrame = cv2.cvtColor(hsvFrame, cv2.COLOR_HSV2BGR)
        return outFrame

    def changeBlur(self, img):
        img = cv2.blur(img, (self.__frame_rate+1, self.__frame_rate+1))
        return img

    def hueFilter(self, hsvFrame):
        # scale pixel values up or down for channel 0(Hue)
        hsvFrame[:, :, 0] = self.rotateHue(hsvFrame[:, :, 0], self.__hue)
        return hsvFrame

    def saturationFilter(self, hsvFrame):
        # scale pixel values up or down for channel 1(Saturation)
        hsvFrame[:, :, 1] = hsvFrame[:, :, 1] * self.__saturation
        hsvFrame[:, :, 1][hsvFrame[:, :, 1] > 255] = 255  # setting values > 255 to 255.
        return hsvFrame

    def brightnessFilter(self, hsvFrame):
        # scale pixel values up or down for channel 2(Value)
        hsvFrame[:, :, 2] = hsvFrame[:, :, 2] * self.__brightness
        hsvFrame[:, :, 2][hsvFrame[:, :, 2] > 255] = 255  # setting values > 255 to 255.
        return hsvFrame

    def rotateHue(self, val, deg):
        return (val + deg)%180