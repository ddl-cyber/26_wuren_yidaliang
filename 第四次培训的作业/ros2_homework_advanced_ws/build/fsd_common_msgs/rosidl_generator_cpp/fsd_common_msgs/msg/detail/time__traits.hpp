// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/Time.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/time.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__TIME__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__TIME__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/time__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Time & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: frame_id_num
  {
    out << "frame_id_num: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_id_num, out);
    out << ", ";
  }

  // member: sum_compute_time
  {
    out << "sum_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.sum_compute_time, out);
    out << ", ";
  }

  // member: control_compute_time
  {
    out << "control_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.control_compute_time, out);
    out << ", ";
  }

  // member: boundary_detector_compute_time
  {
    out << "boundary_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.boundary_detector_compute_time, out);
    out << ", ";
  }

  // member: line_detector_compute_time
  {
    out << "line_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.line_detector_compute_time, out);
    out << ", ";
  }

  // member: skidpad_detector_compute_time
  {
    out << "skidpad_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.skidpad_detector_compute_time, out);
    out << ", ";
  }

  // member: lidar_detection_compute_time
  {
    out << "lidar_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.lidar_detection_compute_time, out);
    out << ", ";
  }

  // member: camera_detection_compute_time
  {
    out << "camera_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_detection_compute_time, out);
    out << ", ";
  }

  // member: fusion_detection_compute_time
  {
    out << "fusion_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.fusion_detection_compute_time, out);
    out << ", ";
  }

  // member: time2
  {
    out << "time2: ";
    rosidl_generator_traits::value_to_yaml(msg.time2, out);
    out << ", ";
  }

  // member: time3
  {
    out << "time3: ";
    rosidl_generator_traits::value_to_yaml(msg.time3, out);
    out << ", ";
  }

  // member: time4
  {
    out << "time4: ";
    rosidl_generator_traits::value_to_yaml(msg.time4, out);
    out << ", ";
  }

  // member: time5
  {
    out << "time5: ";
    rosidl_generator_traits::value_to_yaml(msg.time5, out);
    out << ", ";
  }

  // member: time6
  {
    out << "time6: ";
    rosidl_generator_traits::value_to_yaml(msg.time6, out);
    out << ", ";
  }

  // member: time7
  {
    out << "time7: ";
    rosidl_generator_traits::value_to_yaml(msg.time7, out);
    out << ", ";
  }

  // member: time8
  {
    out << "time8: ";
    rosidl_generator_traits::value_to_yaml(msg.time8, out);
    out << ", ";
  }

  // member: time9
  {
    out << "time9: ";
    rosidl_generator_traits::value_to_yaml(msg.time9, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Time & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: frame_id_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "frame_id_num: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_id_num, out);
    out << "\n";
  }

  // member: sum_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sum_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.sum_compute_time, out);
    out << "\n";
  }

  // member: control_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "control_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.control_compute_time, out);
    out << "\n";
  }

  // member: boundary_detector_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "boundary_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.boundary_detector_compute_time, out);
    out << "\n";
  }

  // member: line_detector_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "line_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.line_detector_compute_time, out);
    out << "\n";
  }

  // member: skidpad_detector_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "skidpad_detector_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.skidpad_detector_compute_time, out);
    out << "\n";
  }

  // member: lidar_detection_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lidar_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.lidar_detection_compute_time, out);
    out << "\n";
  }

  // member: camera_detection_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "camera_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_detection_compute_time, out);
    out << "\n";
  }

  // member: fusion_detection_compute_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fusion_detection_compute_time: ";
    rosidl_generator_traits::value_to_yaml(msg.fusion_detection_compute_time, out);
    out << "\n";
  }

  // member: time2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time2: ";
    rosidl_generator_traits::value_to_yaml(msg.time2, out);
    out << "\n";
  }

  // member: time3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time3: ";
    rosidl_generator_traits::value_to_yaml(msg.time3, out);
    out << "\n";
  }

  // member: time4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time4: ";
    rosidl_generator_traits::value_to_yaml(msg.time4, out);
    out << "\n";
  }

  // member: time5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time5: ";
    rosidl_generator_traits::value_to_yaml(msg.time5, out);
    out << "\n";
  }

  // member: time6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time6: ";
    rosidl_generator_traits::value_to_yaml(msg.time6, out);
    out << "\n";
  }

  // member: time7
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time7: ";
    rosidl_generator_traits::value_to_yaml(msg.time7, out);
    out << "\n";
  }

  // member: time8
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time8: ";
    rosidl_generator_traits::value_to_yaml(msg.time8, out);
    out << "\n";
  }

  // member: time9
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time9: ";
    rosidl_generator_traits::value_to_yaml(msg.time9, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Time & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::Time>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).frame_id_num,
    std::forward<T>(msg).sum_compute_time,
    std::forward<T>(msg).control_compute_time,
    std::forward<T>(msg).boundary_detector_compute_time,
    std::forward<T>(msg).line_detector_compute_time,
    std::forward<T>(msg).skidpad_detector_compute_time,
    std::forward<T>(msg).lidar_detection_compute_time,
    std::forward<T>(msg).camera_detection_compute_time,
    std::forward<T>(msg).fusion_detection_compute_time,
    std::forward<T>(msg).time2,
    std::forward<T>(msg).time3,
    std::forward<T>(msg).time4,
    std::forward<T>(msg).time5,
    std::forward<T>(msg).time6,
    std::forward<T>(msg).time7,
    std::forward<T>(msg).time8,
    std::forward<T>(msg).time9);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::Time>()
{
  return "fsd_common_msgs::msg::Time";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::Time>()
{
  return "fsd_common_msgs/msg/Time";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::Time>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::Time>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::Time>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::Time>
{
  static constexpr std::size_t member_count = 18;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "frame_id_num",
    "sum_compute_time",
    "control_compute_time",
    "boundary_detector_compute_time",
    "line_detector_compute_time",
    "skidpad_detector_compute_time",
    "lidar_detection_compute_time",
    "camera_detection_compute_time",
    "fusion_detection_compute_time",
    "time2",
    "time3",
    "time4",
    "time5",
    "time6",
    "time7",
    "time8",
    "time9",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__TIME__TRAITS_HPP_
