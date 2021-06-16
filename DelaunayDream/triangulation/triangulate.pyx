# distutils: language = c++
# cython: language_level=3
# cython: profile = True

import cv2 as cv
import numpy as np
cimport numpy as np
cimport cython
from libcpp.vector cimport vector


cdef extern from "lib/delaunator.hpp" namespace "delaunator":
    cdef cppclass Delaunator:
        Delaunator(vector[double]& in_coords) except +
        vector[double]& coords
        vector[size_t] triangles

# profiling
@cython.profile(True)
def mean(trig_frame, mask):
    return cv.mean(trig_frame, mask)


# little to no impact on performance
cdef delaunator_triangulate(coords):
    cdef vector[double] coords_vec = coords
    cdef Delaunator* d = new Delaunator(coords_vec)

    cdef size_t[::1] arr_triangles = <size_t [:d.triangles.size()]>d.triangles.data()

    np_coords = np.asarray(coords)
    np_triangles = np.asarray(arr_triangles)

    np_coords = np_coords.reshape((-1, 2))

    return np_coords[np_triangles]


def triangulate_frame(frame, coordinates, scale_factor):

    trig_frame = frame.copy()

    height, width = frame.shape[:2]
    small_frame = cv.resize(frame,(int(width*scale_factor), int(height*scale_factor)), interpolation = cv.INTER_AREA)
    # use trig lib here to get triangle pts
    trig_pts = delaunator_triangulate(coordinates)
    trig_pts = trig_pts.reshape((-1, 3, 1, 2))

    for triangle in trig_pts:  # let's parallelize this for loop

        small_triangle = np.multiply(triangle, scale_factor).astype(int)
        mask = np.zeros(small_frame.shape[:2], np.uint8)
        cv.fillPoly(mask, [small_triangle], (255, 255, 255))

        # the bottleneck point:
        # 3 second for 4000 triangles, 80-90% of runtime pre downscale
        # 0.03 second after downscale by 0.1
        # mean_color = cv.mean(trig_frame, mask)
        mean_color = mean(small_frame, mask)

        # cv.polylines(trig_frame, [triangle], isClosed=True, color=(255, 255, 255), thickness=2)
        cv.fillPoly(trig_frame, [triangle], mean_color)

    return trig_frame
