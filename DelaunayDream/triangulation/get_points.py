import numpy as np
from numpy.random import choice
import cv2 as cv
from math import sqrt, pow

"""
Based on: https://github.com/pmaldonado/PyTri/blob/master/delaunay.py#L56
"""


def generate_sample_points(img, max_points, threshold):
    # Threshold (type: float) is the threshold above which points should be sampled for triangulation.
    # The weights of each pixel (as determined by approx_canny) are compared to this value.

    height, width = img.shape[:2]

    # Originally: n = min(round(height * width * args.rate), max_points)
    n = min(round(height * width * 0.03), max_points)

    weights = approx_canny(img, threshold)
    sample_points = threshold_sample(n, weights)

    corners = np.array([[0, 0], [0, height - 1], [width - 1, 0], [width - 1, height - 1]])
    result = np.append(sample_points, corners, axis=0)
    return result.reshape((-1))

def generate_PDS_points(img, max_points, threshold)
    # Threshold (type: float) is the threshold above which points should be sampled for triangulation.
    # The weights of each pixel (as determined by approx_canny) are compared to this value.

    height, width = img.shape[:2]

    # Originally: n = min(round(height * width * args.rate), max_points)
    n = min(round(height * width * 0.03), max_points)

    weights = approx_canny(img, threshold)

def poisson_sample(n, weights):
    height, width = weights.shape[:2]

    idealRH = (height / (sqrt(n) - 1)) / 1.5
    idealRW = (idealRH * (width / height)) / 1.5
    candidates = np.argwhere(weights > 0)
    initPoint = choice(candidates, 1)
    points = np.append(initPoint, 0)
    candidates = np.delete(np.where((candidates == initPoint).all(axis=1)))
    while points.shape[0] < n and candidates.shape[0] > 0:
        if np.amin(points, 0)[2] >= 15:
            break
        sourcePoint = choice(points, 1)
        while sourcePoint[2] >= 15:
            sourcePoint = choice(points, 1)
        while sourcePoint[2] < 15:
            localCandidates = candidates[np.where(pow(candidates[:, 0] - sourcePoint[0], 2) / )]

def threshold_sample(n, weights):
    candidates = np.fliplr(np.argwhere(weights > 0))

    if candidates.shape[0] <= n:
        return candidates
    else:
        return candidates[np.around(np.linspace(0, candidates.shape[0] - 1, n)).astype(int)]


def approx_canny(img, threshold=0.33):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    v = np.median(gray)
    lower = int(max(0, (1.0 - threshold) * v))
    upper = int(min(255, (1.0 + threshold) * v))
    canny = cv.Canny(gray, lower, upper)
    return canny
