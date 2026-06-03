# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target fsd_common_msgs::fsd_common_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${fsd_common_msgs_TARGETS}.
if(fsd_common_msgs_TARGETS AND NOT TARGET fsd_common_msgs::fsd_common_msgs)
  add_library(fsd_common_msgs::fsd_common_msgs INTERFACE IMPORTED)
  set_target_properties(fsd_common_msgs::fsd_common_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${fsd_common_msgs_TARGETS}")
endif()
