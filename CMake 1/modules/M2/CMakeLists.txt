set(M2_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_library(M2
    ${M2_DIR}/src/M2.cpp
)
target_include_directories(M2 PUBLIC ${M2_DIR}/include)

# M2 可能依赖 A2（camera）
target_link_libraries(M2 PUBLIC A1 A2 kalman)