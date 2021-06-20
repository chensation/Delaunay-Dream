import cv2
import numpy as np
from DelaunayDream import filters

def nothing(b):
    if False:
        print("nothng")

def main():
    cv2.namedWindow('image')
    cv2.createTrackbar('brit', 'image', 100, 150, nothing)
    cv2.createTrackbar('saturation', 'image', 100, 200, nothing)
    cv2.createTrackbar('Hue', 'image', 0, 179, nothing)
    cap = cv2.VideoCapture(0)

    while True:
        britVal = cv2.getTrackbarPos('brit', 'image')
        satVal = cv2.getTrackbarPos('saturation', 'image')
        hueVal = cv2.getTrackbarPos('Hue', 'image')
        britVal = britVal/100 # dividing by 100 to get in range 0-1.5
        satVal = satVal/100

        _, rawFrame = cap.read()

        res = filters.applyFilters(britVal, satVal, hueVal, rawFrame)

        cv2.imshow("original", rawFrame)
        cv2.imshow('image', res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()