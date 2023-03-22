import ctypes
import pathlib
import subprocess
from stopwatch import Stopwatch
from LinearAlgebraLibrary import *

if __name__ == "__main__":

    library_list = [LinearAlgebraLibraryCpp(), LinearAlgebraLibraryPython()]

    '''Benchmarking vector operation cpp-loaded vs python-native libraries'''
    stopwatch = Stopwatch(2)
    sz = 1000
    vec_one = [1 for i in range(sz)]
    vec_two = [1 for i in range(sz)]

    for library in library_list:
        stopwatch.restart()

        library.speed_test_helper(
        vec_one,
        vec_two,
        sz,
        iterations = 10000)

        stopwatch.stop()
        time_elapsed = str(stopwatch)
        print(f'... seconds: {time_elapsed}')



