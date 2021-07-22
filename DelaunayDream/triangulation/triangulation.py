import DelaunayDream.triangulation.get_points as sampling
from DelaunayDream.triangulation.triangulate import triangulate_frame


class Triangulation:

    def __init__(self, num_points=2000, threshold=0.33, image_scale=1, draw_line=False, line_thickness=1, pds=False):
        self._num_points = num_points
        self._threshold = threshold
        self._image_scale = image_scale
        self._draw_line = draw_line
        self._line_thickness = line_thickness
        self._coordinates = None
        self._pds = pds

    @property
    def num_points(self):
        return self._num_points

    @num_points.setter
    def num_points(self, num):
        self._num_points = num

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        self._threshold = threshold

    @property
    def image_scale(self):
        return self._image_scale * 100

    @image_scale.setter
    def image_scale(self, scale):
        self._image_scale = scale / 100

    @property
    def draw_line(self):
        return self._draw_line

    @draw_line.setter
    def draw_line(self, draw_line):
        self._draw_line = draw_line

    @property
    def line_thickness(self):
        return self._line_thickness

    @line_thickness.setter
    def line_thickness(self, thickness):
        self._line_thickness = thickness

    @property
    def pds(self):
        return self._pds

    @pds.setter
    def pds(self, pds):
        self._pds = pds

    def apply_triangulation(self, frame):
        # change this depending on which sampling method we want to use
        if self._pds:
            self._coordinates = sampling.generate_sample_points(frame, self._num_points, self._threshold)
        else:
            self._coordinates = sampling.generate_threshold_points(frame, self._num_points, self._threshold)

        tri_frame = triangulate_frame(frame, self._coordinates, self._image_scale, self._draw_line, self._line_thickness)
        return tri_frame
