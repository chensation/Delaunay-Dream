cmake_minimum_required(VERSION 3.16)
project(triangulation)

set(CMAKE_CXX_STANDARD 14)

set(EXTERNAL_LIB_HEADERS lib/delaunator-cpp/include)

add_executable(triangulation main.cpp)

target_include_directories(
        triangulation PRIVATE
        ${EXTERNAL_LIB_HEADERS}
)

