
# from DelaunayDream.testee.test import plzexport
from DelaunayDream.triangulation.triangulate import triangulate_frame
from DelaunayDream.triangulation.get_points import generate_sample_points
import cv2 as cv
import numpy as np
import sys


def main():
    img = cv.imread("triangulation/m.jpg")
    if img is None:
        sys.exit("Could not read the image.")

    # f = open("DelaunayDream/triangulation/coords.txt", "r")
    # temp_pts = f.read().split(" ")
    # temp_pts.pop()
    # temp_pts = [int(i) for i in temp_pts]
    # f.close()
    # temp_pts = np.array(temp_pts, dtype=int)

    sample_pts = generate_sample_points(img, 2000, 10)

    test_pts = sample_pts.reshape((-1, 2))
    test_img = img.copy()
    for pt in test_pts:
        cv.circle(test_img, tuple(pt), 1, (0, 0, 255))

    cv.imshow("Display window", test_img)
    cv.waitKey(0)

    trig_img = triangulate_frame(img, sample_pts, scale_factor=0.1)

    cv.imshow("Display window", trig_img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
