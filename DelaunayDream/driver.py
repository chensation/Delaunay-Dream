
# from DelaunayDream.testee.test import plzexport
from DelaunayDream.triangulation.triangulate import triangulate_frame
import cv2 as cv


def main():
    print("hello")
    # plzexport()

    img = cv.imread("DelaunayDream/triangulation/sample.jpg")
    # if img is None:
    #     sys.exit("Could not read the image.")

    temp_pts = [214, 36, 311, 65, 211, 135, 414, 36, 511, 65, 411, 135] * 1000
    trig_img = triangulate_frame(img, temp_pts)

    cv.imshow("Display window", trig_img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
