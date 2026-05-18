set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
# 添加 common 和 modules 子目录
add_subdirectory(common)
add_subdirectory(modules)

# 主可执行文件
add_executable(test main.cpp)

# 链接库
target_link_libraries(test PRIVATE
    M1
    M2
    math
    A1
    A2
    kalman
    ${OpenCV_LIBS}
)