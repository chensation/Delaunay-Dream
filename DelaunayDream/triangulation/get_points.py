import numpy as np
from numpy.random import choice
import cv2 as cv
from math import sqrt, pow
from random import randrange

"""
Based on: https://github.com/pmaldonado/PyTri/blob/master/delaunay.py#L56
"""

# Deprecated
def generate_threshold_points(img, max_points, threshold):
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

def generate_sample_points(img, max_points, threshold):
    # Threshold (type: float) is the threshold above which points should be sampled for triangulation.
    # The weights of each pixel (as determined by approx_canny) are compared to this value.

    height, width = img.shape[:2]

    # Originally: n = min(round(height * width * args.rate), max_points)
    n = min(round(height * width * 0.03), max_points)

    weights = approx_canny(img, threshold) > 0
    sample_points = poisson_sample(max_points, weights)
    corners = np.array([[0, 0], [0, height - 1], [width - 1, 0], [width - 1, height - 1]])
    result = np.append(sample_points, corners, axis=0)
    return result.reshape((-1))

def rowIsIn(row, arr):
    return np.any(np.equal(arr, row).all(1))

def getCanDisk(src, center, rH, rW):
    hOffset = int(np.max(np.array([0, center[0] - (2 * rH)])))
    wOffset = int(np.max(np.array([0, center[1] - (2 * rW)])))
    trimmed = src[hOffset: int(np.min(np.array([src.shape[0], center[0] + (2 * rH)]))),
              wOffset: int(np.min(np.array([src.shape[1], center[1] + (2 * rW)])))]
    candidates = np.argwhere(trimmed == True) + np.array([hOffset, wOffset])
    canResults = candidates[
                 np.logical_and(
                     (((np.power(candidates[:, 0] - center[0], 2) / np.power(rH, 2)) + (
                             np.power(candidates[:, 1] - center[1], 2) / np.power(rW, 2))) >= 1),
                     (((np.power(candidates[:, 0] - center[0], 2) / np.power((2 * rH), 2)) + (
                             np.power(candidates[:, 1] - center[1], 2) / np.power((2 * rW), 2))) <= 1)
                 ), :
                 ]
    return canResults

def getOthDisk(src, center, rH, rW):
    hOffset = int(np.max(np.array([0, center[0] - (2 * rH)])))
    wOffset = int(np.max(np.array([0, center[1] - (2 * rW)])))
    trimmed = src[hOffset: int(np.min(np.array([src.shape[0], center[0] + (2 * rH)]))),
              wOffset: int(np.min(np.array([src.shape[1], center[1] + (2 * rW)])))]
    others = np.argwhere(trimmed == False) + np.array([hOffset, wOffset])
    othResults = others[
                 np.logical_and(
                     (((np.power(others[:, 0] - center[0], 2) / np.power(rH, 2)) + (
                             np.power(others[:, 1] - center[1], 2) / np.power(rW, 2))) >= 1),
                     (((np.power(others[:, 0] - center[0], 2) / np.power((2 * rH), 2)) + (
                             np.power(others[:, 1] - center[1], 2) / np.power((2 * rW), 2))) <= 1)
                 ), :
                 ]
    return othResults


def available(point, found, rH, rW):
    return(
        not(np.any((
            (np.power(found[:, 0] - point[0], 2) / pow(rH, 2)) +
            (np.power(found[:, 1] - point[1], 2) / pow(rW, 2))
        ) <= 1))
    )

def poisson_sample(n, weights):
    height, width = weights.shape[:2]

    idealRH = round((height / (sqrt(n) - 1)))
    idealRW = round((idealRH * (width / height)))
    candidates = np.argwhere(weights > 0)
    points = np.ndarray(shape=(1, 2))
    points[0, :] = candidates[randrange(0, candidates.shape[0]), :]

    # Now have initial point to start expanding from, list of candidates to choose from, and weights.

    numPoints = 1
    eligiblePoints = np.ndarray(shape = (1, 2))
    eligiblePoints[0, :] = points
    unavailable = np.zeros_like(weights, dtype = bool)
    unavailable[points[0, :].astype(int)] = True

    while numPoints < n and eligiblePoints.shape[0] > 0:
        sourcePointRow = randrange(0, eligiblePoints.shape[0])
        sourcePoint = eligiblePoints[sourcePointRow, :]
        primeTargets= getCanDisk(weights, sourcePoint, idealRH, idealRW)
        attempts = 0
        while primeTargets.shape[0] > 0:
            if attempts == 15:
                primeTargets = np.empty([0, 0])
                continue
            targetRow = randrange(0, primeTargets.shape[0])
            target = primeTargets[targetRow, :]
            isUnavailable = unavailable[target[0], target[1]]
            if not(isUnavailable) and available(target, points, idealRH, idealRW):
                points = np.vstack((points, target))
                unavailable[target[0], target[1]] = True
                eligiblePoints = np.vstack((eligiblePoints, target))
                numPoints = numPoints + 1
                break
            else:
                if not(isUnavailable):
                    unavailable[target[0], target[1]] = True
                primeTargets = np.delete(primeTargets, targetRow, 0)
                attempts = attempts + 1
        else:
            otherTargets = getOthDisk(weights, sourcePoint, idealRH, idealRW)
            attempts = 0
            while otherTargets.shape[0] > 0:
                if attempts == 15:
                    otherTargets = np.empty([0, 0])
                    continue
                targetRow = randrange(0, otherTargets.shape[0])
                target = otherTargets[targetRow, :]
                isUnavailable = unavailable[target[0], target[1]]
                if not(isUnavailable) and available(target, points, idealRH, idealRW):
                    points = np.vstack((points, target))
                    unavailable[target[0], target[1]] = True
                    eligiblePoints = np.vstack((eligiblePoints, target))
                    numPoints = numPoints + 1
                    break
                else:
                    if not(isUnavailable):
                        unavailable[target[0], target[1]] = True
                    otherTargets = np.delete(otherTargets, targetRow, 0)
                    attempts = attempts + 1
            else:
                eligiblePoints = np.delete(eligiblePoints, sourcePointRow, 0)

    return np.fliplr(points.astype(int))

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
