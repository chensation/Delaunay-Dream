import cv2 as cv
import sys
import numpy as np
# import numpy.ma as ma


def triangulate_frame(frame, coordinates):

    trig_frame = frame.copy()

    # use trig lib here to get triangle pts

    trig_pts = np.array(coordinates, np.int32)
    trig_pts = trig_pts.reshape((-1, 3, 1, 2))
    for triangle in trig_pts:  # let's parallelize this for loop
        mask = np.zeros(trig_frame.shape[:2], np.uint8)
        cv.fillPoly(mask, [triangle], (255, 255, 255))

        # the bottleneck point: 1.6 second for 2000 triangles, 50%-60% of runtime without the cpp lib
        mean_color = cv.mean(trig_frame, mask)

        # tried to optimize it with numpy mean, lmao way worse
        # trig_pixels = cv.bitwise_and(frame, frame, mask=mask)
        # trig_pixels = ma.masked_equal(trig_pixels, [0, 0, 0])
        # average = trig_pixels.reshape((-1, 3)).mean(axis = 0)
        cv.polylines(trig_frame, [triangle], isClosed=True, color=(255, 255, 255), thickness=2)
        cv.fillPoly(trig_frame, [triangle], mean_color)

    return trig_frame


if __name__ == "__main__":
    img = cv.imread("sample.jpg")
    if img is None:
        sys.exit("Could not read the image.")

    # use drawContours to draw all the triangles at once, can't have different colors though :(
    # pts = np.array([214, 36, 311, 65, 211, 135, 414, 36, 511, 65, 411, 135], np.int32)
    # pts = pts.reshape((-1, 3, 1, 2))
    # cv.drawContours(img, pts, -1, color=(0,255,0), thickness=cv.FILLED)

    temp_pts = [214, 36, 311, 65, 211, 135, 414, 36, 511, 65, 411, 135] * 1000
    trig_img = triangulate_frame(img, temp_pts)

    cv.imshow("Display window", trig_img)
    cv.waitKey(0)
