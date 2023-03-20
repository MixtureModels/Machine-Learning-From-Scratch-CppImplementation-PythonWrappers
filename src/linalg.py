import ctypes
import pathlib
import subprocess

# helper to compile cpp library submodule
def cpp_compile_library(file_path):
    compile_script_path = pathlib.Path().absolute() / file_path
    print(subprocess.run([compile_script_path], shell=True))

def add_vectors(vec_one, vec_two, size):
    array_type = ctypes.c_double * 3
    linalg.addVectors(array_type(*vec_one), array_type(*vec_two))
    return array_type

if __name__ == "__main__":

    # run script to compile cpp files
    compile_script_path = "Scripts/startup.sh"
    cpp_compile_library(compile_script_path)

    # import custom Linear Algebra C-library from shared file produced
    linalg_lib = pathlib.Path().absolute() / "Shared/linalg.so"
    linalg = ctypes.CDLL(linalg_lib)

    # cpp function export message from cpp-library
    linalg.healthCheck()

    add_vectors([0, 1, 2], [1, 1, 1], 3)
