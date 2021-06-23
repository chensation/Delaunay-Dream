# Delaunay-Dream

## Installation
Navigate to root dir and run `pip install --upgrade .`. (It's no longer necessary to have Cython/numpy pre-installed).

## Commands
*   To run the program, type `delaunaydream` in your terminal.
*   To create a new terminal command, use `plzrun` and `plzrun1` inside setup.py as examples. First make sure that the path to the directory of the desirred file is in the list of packages in setup.py.
*   To test triangulation, run `trigtest` from the root dir.
    -  To test the triangulation function by itself, run `python3 setup.py build_ext --inplace` to build the library file to be used.

Remember to not commit your built library file to the repo.  

