
# from DelaunayDream.testee.test import plzexport
from DelaunayDream.triangulation.triangulate import triangulate_frame
import cv2 as cv
import sys


def main():

    img = cv.imread("triangulation/sample.jpg")
    if img is None:
        sys.exit("Could not read the image.")

    f = open("triangulation/coords.txt", "r")

    temp_pts = f.read().split(" ")
    temp_pts.pop()
    temp_pts = [int(i) for i in temp_pts]

    f.close()

    trig_img = triangulate_frame(img, temp_pts)

    cv.imshow("Display window", trig_img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
