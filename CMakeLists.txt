cmake_minimum_required(VERSION 3.12)
project(Lab2)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_EXECUTABLE_OUTPUT_PATH "./.." )
set(CMAKE_CXX_FLAGS_RELEASE "-DNDEBUG -Wall -O2")

include_directories(./..)
add_executable(Lab2 main.cpp)