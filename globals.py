import os

# -d directory of project
# -o build directory
# -b binary output dir
# -id ignore directory
# -if ignore file

PROJECT_DIRECTORY = "."
PROJECT_DIRECTORY = os.path.abspath(PROJECT_DIRECTORY) + '/'
BUILD_DIRECTORY   = PROJECT_DIRECTORY + "/build"

IGNORED_FOLDERS = {
    PROJECT_DIRECTORY + ".git",
    PROJECT_DIRECTORY + "build",
}

print(IGNORED_FOLDERS)

CPP_COMPILER = "g++"
C98_COMPILER = "gcc"

C_FLAGS = ["-g", "-Wall", "-Wextra"]

CPP_FLAGS = []
C98_FLAGS = []

LINKER_FLAGS = ["-lraylib"]

POSIX_MAX_FILENAME_LENGTH:int = 255

class FAILURE_CODE:
    DEPENDENCY_NOT_FOUND = 1
    FAILED_TO_COMPILE = 2
    FAILED_TO_LINK = 3