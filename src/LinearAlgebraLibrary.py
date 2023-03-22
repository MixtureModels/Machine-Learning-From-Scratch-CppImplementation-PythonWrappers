import ctypes
import pathlib
import subprocess
from stopwatch import Stopwatch

class LinearAlgebraLibraryCpp:
    def __init__(self):
        self.compile_script_path = "../Scripts/startup.sh"
        self.cpp_compile_library(self.compile_script_path)
        self.linalg_lib_path = pathlib.Path().absolute() / "Shared/linalg.so"
        self.linalg = ctypes.CDLL(self.linalg_lib_path)

    def cpp_compile_library(self, file_path):
        compile_script_path = pathlib.Path().absolute() / file_path
        subprocess.run([compile_script_path], shell=True)
        print('<< script to compile cpp-files ran')

    # python wrapper with cpp-implementation: add vectors
    def add_vectors(self, vec_one, vec_two, size):
        array_type = ctypes.c_double * 3
        int_type = ctypes.c_int
        self.linalg.addVectors(array_type(*vec_one), array_type(*vec_two), int_type(size))

    # helper to benchmark speed-comparison between python-native and cpp-compiled library function
    def speed_test_helper(self, vec_one, vec_two, size, iterations):
        array_type = ctypes.c_double * size
        int_type = ctypes.c_int
        self.linalg.speedTestHelper(array_type(*vec_one), array_type(*vec_two), int_type(iterations), int_type(size))


class LinearAlgebraLibraryPython:
    
    def speed_test_helper(self, vec_one, vec_two, size, iterations):
        for i in range(iterations):
            for j in range(size):
                computedVal = vec_one[j] + vec_two[j]

class LinearAlgebraLibraryRust:
    def __init__(self):
        self.compile_script_path = "../Scripts/startup.sh"
        self.cpp_compile_library(self.compile_script_path)
        self.linalg_lib_path = pathlib.Path().absolute() / "Shared/linalg.so"
        self.linalg = ctypes.CDLL(self.linalg_lib_path)
