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
    packages=["DelaunayDream", "DelaunayDream.testee", "DelaunayDream.gui", "DelaunayDream.triangulation",
              "DelaunayDream.videopipe", "DelaunayDream.testee.deep"],
    url="https://github.com/chensation/Delaunay-Dream.git",
    author="princess",
    include_package_data=True,
    ext_modules=cythonize(extensions),
    # Make sure to add the libraries we use here.
    install_requires=["Cython", "numpy", "opencv-python-headless", "PyQt5"],
    entry_points={
        "console_scripts": [
            "delaunaydream = DelaunayDream.main:main",
            "plzrun = DelaunayDream.testee.deep.gem:main",
            "plzrun1 = DelaunayDream.testee.test:main",
            "trigtest = DelaunayDream.driver:main",
            "filtertest = DelaunayDream.webCamFilterDemo:main"
        ]
    }

)
