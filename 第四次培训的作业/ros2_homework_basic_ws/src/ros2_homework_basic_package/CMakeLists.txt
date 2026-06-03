cmake_minimum_required(VERSION 3.20)
project(ros2_homework_basic_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 查找依赖
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

### 编译与链接
# add_executable(目标名 源文件) -- 定义一个可执行文件目标
# 将 src/eight_figure_node.cpp 编译为名为 eight_figure_node 的可执行文件
add_executable(eight_figure_node src/eight_figure_node.cpp)

# target_include_directories(目标名 范围 路径...) -- 为目标添加头文件搜索路径
# PRIVATE 表示这些路径仅用于编译此目标，不会传递给依赖此目标的其他目标
# ${rclcpp_INCLUDE_DIRS} 和 ${geometry_msgs_INCLUDE_DIRS} 是 find_package 后自动设置的变量
target_include_directories(eight_figure_node PRIVATE
  ${rclcpp_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS}
)

# target_link_libraries(目标名 依赖库...) -- 为目标添加链接库
# 在较新的ROS2版本中，使用标准CMake方式链接依赖
# rclcpp::rclcpp 是rclcpp包导出的CMake target，包含头文件路径和库文件
# geometry_msgs::geometry_msgs__rosidl_typesupport_cpp 是消息包的类型支持target，包含消息序列化所需实现
target_link_libraries(eight_figure_node
  rclcpp::rclcpp
  geometry_msgs::geometry_msgs__rosidl_typesupport_cpp
)

### 安装
# install(TARGETS ...) -- 安装编译生成的可执行文件
# DESTINATION lib/${PROJECT_NAME} 表示安装到 <install_prefix>/lib/<package_name> 目录
# ROS2的节点可执行文件通常安装到此目录
install(TARGETS
  eight_figure_node
  DESTINATION lib/${PROJECT_NAME}
)

# install(DIRECTORY ...) -- 安装目录中的文件
# DIRECTORY config launch 表示安装 config 和 launch 目录下的所有文件
# DESTINATION share/${PROJECT_NAME} 表示安装到 <install_prefix>/share/<package_name> 目录
# ROS2的launch文件和配置文件通常安装到此目录
install(DIRECTORY
  config
  launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # 跳过版权检查
  set(ament_cmake_copyright_FOUND TRUE)
  # 跳过cpplint检查
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
