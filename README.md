# Delaunay-Dream

## Installation
Navigate to root dir and run `pip install -U .`. (It's no longer necessary to have Cython/numpy pre-installed).

## Commands
*   To run the program, type `delaunaydream` in your terminal.
    - There is a sample video to try in the videopipe/Samples folder
*   To create a new terminal command, use `plzrun` and `plzrun1` inside setup.py as examples. First make sure that the path to the directory of the desirred file is in the list of packages in setup.py.
*   <s>To test triangulation, run `trigtest` from the root dir.
    -  To test the triangulation function by itself, run `python3 setup.py build_ext --inplace` to build the library file to be used.</s>
    - trigtest no longer works since we switched to headless opencv

Remember to not commit your built library file to the repo.  

