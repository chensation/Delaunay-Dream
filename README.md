# Delaunay-Dream

## Installation
Navigate to root dir and run `pip install --upgrade .`. (It's no longer necessary to have Cython/numpy pre-installed).

## Commands
*   To create a new terminal command, use `plzrun` and `plzrun1` inside setup.py as examples. First make sure that the path to the directory of the desirred file is in the list of packages in setup.py.
*   To test triangulation, run `trigtest` from the root dir.
    -  <s>To test the triangulation function, run `python3 setup.py build_ext --inplace` to build the library file to be used.</s>(<-- I don't think this is necessary anymore)

Remember to not commit your built library file to the repo.  

