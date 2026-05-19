cmake_minimum_required(VERSION 3.10)
project(Test)

# 查找 OpenCV
find_package(OpenCV REQUIRED)

# 添加子目录
add_subdirectory("CMake 1")