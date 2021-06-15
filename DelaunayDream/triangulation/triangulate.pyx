# distutils: language = c++
# cython: language_level=3

import cv2 as cv
import numpy as np
cimport numpy as np
from libcpp.vector cimport vector


cdef extern from "lib/delaunator.hpp" namespace "delaunator":
    cdef cppclass Delaunator:
        Delaunator(vector[double]& in_coords) except +
        vector[double]& coords
        vector[size_t] triangles


cdef delaunator_triangulate(coords):
    cdef vector[double] coords_vec = coords
    cdef Delaunator* d = new Delaunator(coords_vec)

    cdef size_t[::1] arr_triangles = <size_t [:d.triangles.size()]>d.triangles.data()

    np_coords = np.asarray(coords)
    np_triangles = np.asarray(arr_triangles)

    np_coords = np_coords.reshape((-1, 2))

    return np_coords[np_triangles]


def triangulate_frame(frame, coordinates):

    trig_frame = frame.copy()

    # use trig lib here to get triangle pts
    trig_pts = delaunator_triangulate(coordinates)
    trig_pts = trig_pts.reshape((-1, 3, 1, 2))
    for triangle in trig_pts:  # let's parallelize this for loop
        mask = np.zeros(trig_frame.shape[:2], np.uint8)
        cv.fillPoly(mask, [triangle], (255, 255, 255))

        # the bottleneck point: 1.6 second for 2000 triangles, 50%-60% of runtime without the cpp lib
        mean_color = cv.mean(trig_frame, mask)

        # cv.polylines(trig_frame, [triangle], isClosed=True, color=(255, 255, 255), thickness=2)
        cv.fillPoly(trig_frame, [triangle], mean_color)

    return trig_frame
