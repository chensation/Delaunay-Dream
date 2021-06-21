import time
import numpy as np
from numpy.random import randint, choice
import cv2 as cv

def generate_sample_points(img, max_points, threshold):
    # Threshold (type: float) is the threshold above which points should be sampled for triangulation.
    # The weights of each pixel (as determined by approx_canny) are compared to this value.

    width = img.shape[0]
    height = img.shape[1]
    # Originally: n = min(round(height * width * args.rate), max_points)
    n = min(round(height * width * 0.03), max_points)

    t0 = time.perf_counter()
    weights = approx_canny(img) #TODO: integrate with the existing approx_canny function that we have created
    t1 = time.perf_counter()

    t0 = time.perf_counter()
    sample_points = threshold_sample(n, weights, threshold)
    t1 = time.perf_counter()

    corners = np.array([[0, 0], [0, height-1], [width-1, 0], [width-1, height-1]])
    return np.append(sample_points, corners, axis=0)

def threshold_sample(n, weights, threshold):
    candidates = np.array([idx for idx, weight in np.ndenumerate(weights) if weight >= threshold])
    if candidates.shape[0] < n:
        raise ValueError(f"Not enough candidate points for threshold {threshold}. "
                         f"Only {candidates.shape[0]} available.")

    return candidates[choice(candidates.shape[0], size=n, replace=False)]

def approx_canny(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    v = np.median(img)
    v_alt = np.median(gray)
    lower = int(max(0,(1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))
    #canny = cv.Canny(img, lower, upper)
    canny = cv.Canny(gray, lower, upper)
    return canny