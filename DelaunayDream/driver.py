
# from DelaunayDream.testee.test import plzexport
from DelaunayDream.triangulation.triangulate import triangulate_frame
import cv2 as cv
import sys


def main():
    img = cv.imread("DelaunayDream/triangulation/sample.jpg")
    if img is None:
        sys.exit("Could not read the image.")

    f = open("DelaunayDream/triangulation/coords.txt", "r")

    temp_pts = f.read().split(" ")
    temp_pts.pop()
    temp_pts = [int(i) for i in temp_pts]

    f.close()

    trig_img = triangulate_frame(img, temp_pts, scale_factor=0.1, draw_line=True)

    cv.imshow("Display window", trig_img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
