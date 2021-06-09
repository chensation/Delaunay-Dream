import cv2 as cv
import sys
import numpy as np


def triangulate_frame(frame, coordinates):
    # use lib here
    trig_pts = np.array(coordinates, np.int32)
    trig_pts = trig_pts.reshape((-1, 3, 1, 2))
    for triangle in trig_pts:
        mask = np.zeros(img.shape[:2], np.uint8)
        cv.fillPoly(mask, [triangle], (255, 255, 255))
        mean = cv.mean(frame, mask)
        cv.fillPoly(frame, [triangle], mean)


if __name__ == "__main__":
    img = cv.imread("sample.jpg")
    if img is None:
        sys.exit("Could not read the image.")

    # pts = np.array([214, 36, 311, 65, 211, 135, 414, 36, 511, 65, 411, 135], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    # pts = pts.reshape((-1, 3, 1, 2))

    # mask = np.zeros(img.shape[:2], np.uint8)
    # cv.fillPoly(mask, [pts], (255, 255, 255))

    # mean = cv.mean(img, mask)
    # cv.fillPoly(img, [pts], mean)
    # cv.drawContours(img, pts, -1, color=(0,255,0), thickness=cv.FILLED)

    triangulate_frame(img, [214, 36, 311, 65, 211, 135, 414, 36, 511, 65, 411, 135])

    cv.imshow("Display window", img)
    cv.waitKey(0)
