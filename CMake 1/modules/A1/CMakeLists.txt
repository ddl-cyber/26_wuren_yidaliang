set(A1_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_library(A1
    ${A1_DIR}/src/A11.cpp
    ${A1_DIR}/src/A12.cpp
    ${A1_DIR}/src/A13.cpp
)
target_include_directories(A1 PUBLIC ${A1_DIR}/include)