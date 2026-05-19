set(A2_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_library(A2
    ${A2_DIR}/src/A2.cpp
)
target_include_directories(A2 PUBLIC ${A2_DIR}/include)