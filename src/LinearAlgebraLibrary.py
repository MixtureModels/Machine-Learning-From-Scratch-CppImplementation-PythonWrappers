import ctypes
import pathlib
import subprocess
from stopwatch import Stopwatch

class LinearAlgebraLibraryCpp:
    """
    Class for C++ implementation of Linear Algebra Library Python wrapper
    """
    def __init__(self):
        self.compile_script_path = "../Scripts/startupCpp.sh"
        self.cpp_compile_library(self.compile_script_path)
        self.linalg_lib_path = pathlib.Path().absolute() / "Shared/linalgCpp.so"
        self.linalg = ctypes.CDLL(self.linalg_lib_path)

    def cpp_compile_library(self, file_path):
        compile_script_path = pathlib.Path().absolute() / file_path
        subprocess.run([compile_script_path], shell=True)
        print('<< script to compile cpp-files ran')

    # Python wrapper with cpp-implementation: add vectors
    def add_vectors(self, vec_one, vec_two, size):
        array_type = ctypes.c_double * 3
        int_type = ctypes.c_int
        self.linalg.addVectors(array_type(*vec_one), array_type(*vec_two), int_type(size))

    # Helper to benchmark speed-comparison between python-native and cpp-compiled library function
    def speed_test_helper(self, vec_one, vec_two, size, iterations):
        array_type = ctypes.c_double * size
        int_type = ctypes.c_int
        self.linalg.speedTestHelper(array_type(*vec_one), array_type(*vec_two), int_type(iterations), int_type(size))

class LinearAlgebraLibraryC:
    """
    Class for vanilla C-language implementation of Linear Algebra Library python wrapper
    """
    def __init__(self):
        self.compile_script_path = "../Scripts/startupC.sh"
        self.cpp_compile_library(self.compile_script_path)
        self.linalg_lib_path = pathlib.Path().absolute() / "Shared/linalgC.so"
        self.linalg = ctypes.CDLL(self.linalg_lib_path)

class LinearAlgebraLibraryPython:
    """
    Class for Python implementation of Linear Algebra Library Python wrapper
    """   
    def speed_test_helper(self, vec_one, vec_two, size, iterations):
        for i in range(iterations):
            for j in range(size):
                computedVal = vec_one[j] + vec_two[j]

class LinearAlgebraLibraryRust:
    """
    Class for Rust implementation of Linear Algebra Library Python wrapper
    """   
    def __init__(self):
        self.compile_script_path = "../Scripts/startup.sh"
        self.cpp_compile_library(self.compile_script_path)
        self.linalg_lib_path = pathlib.Path().absolute() / "Shared/linalg.so"
        self.linalg = ctypes.CDLL(self.linalg_lib_path)
