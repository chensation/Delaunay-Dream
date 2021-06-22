import cv2

class Process:
    def __init__(self, triangulate, frame_rate, hue, saturation, brightness):
        self.__triangulate = triangulate
        self.__frame_rate = frame_rate
        self.__hue = hue
        self.__saturation = saturation
        self.__brightness = brightness

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
        self.__saturation = saturation

    #Brightness
    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        self.__brightness = brightness

    def changeBrightness(self, img):
        """ This function will take an image (img) and the brightness
            value. It will perform the brightness change using OpenCv
            and after split, will merge the img and return it.
        """
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - self.__brightness
        v[v>lim] = 255
        v[v<=lim] += self.__brightness
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
    
    def changeBlur(self, img):
        img = cv2.blur(img, (self.__frame_rate+1, self.__frame_rate+1))
        return img
