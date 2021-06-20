import cv2
import numpy as np


def applyFilters(britVal, satVal, hueVal, bgrFrame):
        hsvFrame = cv2.cvtColor(bgrFrame, cv2.COLOR_BGR2HSV)
        hsvFrame = np.array(hsvFrame, dtype=np.float64)

        hsvFrame = hueFilter(hueVal, hsvFrame)
        hsvFrame = saturationFilter(satVal, hsvFrame)
        hsvFrame = brightnessFilter(britVal, hsvFrame)

        hsvFrame = np.array(hsvFrame, dtype=np.uint8)
        outFrame = cv2.cvtColor(hsvFrame, cv2.COLOR_HSV2BGR)
        return outFrame

def hueFilter(hueVal, hsvFrame):
        # scale pixel values up or down for channel 0(Hue)
        hsvFrame[:, :, 0] = rotateHue(hsvFrame[:, :, 0], hueVal)
        return hsvFrame

def saturationFilter(satVal, hsvFrame):
        # scale pixel values up or down for channel 1(Saturation)
        hsvFrame[:, :, 1] = hsvFrame[:, :, 1] * satVal
        hsvFrame[:, :, 1][hsvFrame[:, :, 1] > 255] = 255  # setting values > 255 to 255.
        return hsvFrame

def brightnessFilter(britVal, hsvFrame):
        # scale pixel values up or down for channel 2(Value)
        hsvFrame[:, :, 2] = hsvFrame[:, :, 2] * britVal
        hsvFrame[:, :, 2][hsvFrame[:, :, 2] > 255] = 255  # setting values > 255 to 255.
        return hsvFrame

def rotateHue(val, deg):
    return (val + deg)%180