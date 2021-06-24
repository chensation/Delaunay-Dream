from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "DelaunayDream.triangulation.triangulate",
        ["DelaunayDream/triangulation/triangulate.pyx"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    name="DelaunayDream",
    version="0.0.1",
    packages=["DelaunayDream", "DelaunayDream.gui", "DelaunayDream.triangulation", "DelaunayDream.videopipe"],
    url="https://github.com/chensation/Delaunay-Dream.git",
    author="drowning_princesses",
    include_package_data=True,
    ext_modules=cythonize(extensions),
    # Make sure to add the libraries we use here.
    install_requires=["numpy", "opencv-python-headless", "pyqt5==5.14"],
    entry_points={
        "console_scripts": [
            "delaunaydream = DelaunayDream.main:main",
        ]
    }

)
