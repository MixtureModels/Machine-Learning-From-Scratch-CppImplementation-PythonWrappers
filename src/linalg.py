import ctypes
import pathlib
import subprocess
from stopwatch import Stopwatch


# helper to compile cpp library submodule
def cpp_compile_library(file_path):
    compile_script_path = pathlib.Path().absolute() / file_path
    subprocess.run([compile_script_path], shell=True)
    print('script ran!')

# python wrapper with cpp-implementation: add vectors
def add_vectors(vec_one, vec_two, size):
    array_type = ctypes.c_double * 3
    int_type = ctypes.c_int
    linalg.addVectors(array_type(*vec_one), array_type(*vec_two), int_type(size))

# helper to benchmark speed-comparison between python-native and cpp-compiled library function
def speed_test_helper(vec_one, vec_two, size, iterations, cpp):
    if cpp == True:
        array_type = ctypes.c_double * size
        int_type = ctypes.c_int
        linalg.speedTestHelper(array_type(*vec_one), array_type(*vec_two), int_type(iterations), int_type(size))
    else:
        for i in range(iterations):
            for j in range(sz):
                computedVal = vec_one[j] + vec_two[j]


if __name__ == "__main__":

    # run script to compile cpp files
    compile_script_path = "../Scripts/startup.sh"
    cpp_compile_library(compile_script_path)

    # import custom Linear Algebra C-library from shared file produced
    linalg_lib = pathlib.Path().absolute() / "Shared/linalg.so"
    linalg = ctypes.CDLL(linalg_lib)

    # cpp function export message from cpp-library
    #linalg.healthCheck()


    '''Benchmarking vector operation cpp-loaded vs python-native'''
    stopwatch = Stopwatch(2)
    sz = 1000
    vec_one = [1 for i in range(sz)]
    vec_two = [1 for i in range(sz)]

    print('... beginning C++ speed test')
    stopwatch.restart()
    speed_test_helper(vec_one, vec_two, sz, iterations = 10000, cpp = True)
    stopwatch.stop()


    cpp_time = str(stopwatch)
    print(f'... C++ seconds: {stopwatch}')
    stopwatch.reset()

    print('... beginning Python speed test')
    stopwatch.restart()
    speed_test_helper(vec_one, vec_two, sz, iterations = 10000, cpp = False)
    stopwatch.stop()
    python_time = str(stopwatch)
    print(f'... Python seconds: {python_time}')
