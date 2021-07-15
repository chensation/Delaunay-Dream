# distutils: language = c++
# cython: language_level=3
# if profiling, add the comment: "cython: profile = True"

import cv2 as cv
import numpy as np
cimport numpy as np
from libcpp.vector cimport vector
# add the import for profiling
# cimport cython

cdef extern from "lib/delaunator.hpp" namespace "delaunator":
    cdef cppclass Delaunator:
        Delaunator(vector[double]& in_coords) except +
        vector[double]& coords
        vector[size_t] triangles

# add function for profiling
# @cython.profile(True)
# def mean(trig_frame, mask):
#     return cv.mean(trig_frame, mask)


# little to no impact on performance
# @cython.profile(True)
cdef delaunator_triangulate(np.ndarray[np.int_t] coords):

    # cast to cpp vector
    cdef long[::1] coords_arr = coords
    cdef vector[double] coords_vec

    cdef int size = coords_arr.shape[0]
    for i in range(size):
        coords_vec.push_back(coords_arr[i])

    cdef Delaunator* d = new Delaunator(coords_vec)

    # convert triangle to a numpy array
    cdef size_t[::1] arr_triangles = <size_t [:d.triangles.size()]>d.triangles.data()
    cdef np.ndarray np_triangles = np.asarray(arr_triangles)

    # group the x and y coordinates together
    cdef np.ndarray tri_coords = coords.reshape((-1, 2))


    # cdef np.ndarray testh = np.zeros([xmax, ymax], dtype=DTYPE)

    # print(lent(tri_coords.shape), len(np_triangles.shape))
    
    tri_coords = tri_coords[np_triangles]
    del d


    # sort then return the coordinates
    return tri_coords


def triangulate_frame(frame, coordinates, scale_factor=1, draw_line=False, thickness=1):

    """ triangulate a given frame with the coordinates, return the triangulated frame

    :param frame: numpy array from openCV, a frame from the video
    :param coordinates: the coordinates to triangulate with
    :type coordinates: np.ndarray
    :param scale_factor: scale the frame in order to speed up color selection, should be less than 1
    :param draw_line: draw lines between each triangle
    :param thickness: thickness of the lines
    :return: numpy array from openCV, newly triangulated frame
    """

    trig_frame = frame.copy()
    height, width = frame.shape[:2]

    # downscale frame for faster color selection
    small_frame = cv.resize(frame,(int(width*scale_factor), int(height*scale_factor)), interpolation = cv.INTER_AREA)

    # use trig lib here to get triangle pts
    trig_pts = delaunator_triangulate(coordinates)

    # reshape 2D array to be array of triangles, each contain 3 xy pairs
    trig_pts = trig_pts.reshape((-1, 3, 1, 2))

    for triangle in trig_pts:
        # downscale the triangle to work on the downscaled frame
        small_triangle = np.multiply(triangle, scale_factor).astype(int)
        mask = np.zeros(small_frame.shape[:2], np.uint8)
        cv.fillPoly(mask, [small_triangle], (255, 255, 255))

        # the bottleneck point:
        # 3 second for 4000 triangles, 80-90% of runtime pre downscale
        # 0.03 second after downscale by 0.1
        # use this line for profiling
        # mean_color = mean(small_frame, mask)
        mean_color = cv.mean(small_frame, mask)

        cv.fillPoly(trig_frame, [triangle], mean_color, lineType=cv.LINE_AA)

        if draw_line:
            cv.polylines(trig_frame, [triangle], isClosed=True, color=(255, 255, 255),
                         thickness=thickness, lineType=cv.LINE_AA)

    return trig_frame
