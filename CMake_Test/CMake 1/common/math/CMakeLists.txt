set(math_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_library(math
    ${math_DIR}/src/Math.cpp
)
target_include_directories(math PUBLIC ${math_DIR}/include)

# 链接 OpenCV（Math.cpp 可能用到 cv::Point2f）
target_link_libraries(math PUBLIC ${OpenCV_LIBS})