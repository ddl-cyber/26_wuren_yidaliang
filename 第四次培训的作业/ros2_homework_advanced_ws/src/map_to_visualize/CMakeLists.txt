cmake_minimum_required(VERSION 3.8)
project(map_to_visualize)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(fsd_common_msgs REQUIRED)

add_executable(map_visualizer src/map_visualizer.cpp)
target_include_directories(map_visualizer PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(map_visualizer PUBLIC c_std_99 cxx_std_17)

target_link_libraries(map_visualizer
  rclcpp::rclcpp
  visualization_msgs::visualization_msgs__rosidl_typesupport_cpp
  fsd_common_msgs::fsd_common_msgs__rosidl_typesupport_cpp
)

install(TARGETS map_visualizer
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME})

# 安装 bag 文件及其元数据，使 launch 文件在 install 空间也能找到 bag
install(FILES map_to_visualize_0.db3 metadata.yaml
  DESTINATION share/${PROJECT_NAME})

ament_package()
