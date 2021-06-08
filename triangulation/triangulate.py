import cv2 as cv
import sys
import numpy as np

img = cv.imread("sample.jpg")
if img is None:
    sys.exit("Could not read the image.")

pts = np.array([214, 36, 311, 65, 211, 135], np.int32)
pts = pts.reshape((-1, 1, 2))

mask = np.zeros(img.shape[:2], np.uint8)
cv.fillPoly(mask, [pts], (255, 255, 255))

mean = cv.mean(img, mask)
cv.fillPoly(img, [pts], mean)

cv.imshow("Display window", img)
cv.waitKey(0)
