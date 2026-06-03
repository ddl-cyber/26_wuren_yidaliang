// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/DrivingDynamics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/driving_dynamics.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__DRIVING_DYNAMICS__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__DRIVING_DYNAMICS__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/driving_dynamics__struct.hpp"
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
  const DrivingDynamics & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: speed_target
  {
    out << "speed_target: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_target, out);
    out << ", ";
  }

  // member: speed_actual
  {
    out << "speed_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_actual, out);
    out << ", ";
  }

  // member: steering_angle_target
  {
    out << "steering_angle_target: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle_target, out);
    out << ", ";
  }

  // member: steering_angle_actual
  {
    out << "steering_angle_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle_actual, out);
    out << ", ";
  }

  // member: brake_hydr_target
  {
    out << "brake_hydr_target: ";
    rosidl_generator_traits::value_to_yaml(msg.brake_hydr_target, out);
    out << ", ";
  }

  // member: brake_hydr_actual
  {
    out << "brake_hydr_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.brake_hydr_actual, out);
    out << ", ";
  }

  // member: motor_moment_target
  {
    out << "motor_moment_target: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_moment_target, out);
    out << ", ";
  }

  // member: motor_moment_actual
  {
    out << "motor_moment_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_moment_actual, out);
    out << ", ";
  }

  // member: acceleration_longitudinal
  {
    out << "acceleration_longitudinal: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration_longitudinal, out);
    out << ", ";
  }

  // member: acceleration_lateral
  {
    out << "acceleration_lateral: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration_lateral, out);
    out << ", ";
  }

  // member: yaw_rate
  {
    out << "yaw_rate: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DrivingDynamics & msg,
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

  // member: speed_target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed_target: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_target, out);
    out << "\n";
  }

  // member: speed_actual
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.speed_actual, out);
    out << "\n";
  }

  // member: steering_angle_target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle_target: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle_target, out);
    out << "\n";
  }

  // member: steering_angle_actual
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle_actual, out);
    out << "\n";
  }

  // member: brake_hydr_target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "brake_hydr_target: ";
    rosidl_generator_traits::value_to_yaml(msg.brake_hydr_target, out);
    out << "\n";
  }

  // member: brake_hydr_actual
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "brake_hydr_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.brake_hydr_actual, out);
    out << "\n";
  }

  // member: motor_moment_target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_moment_target: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_moment_target, out);
    out << "\n";
  }

  // member: motor_moment_actual
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_moment_actual: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_moment_actual, out);
    out << "\n";
  }

  // member: acceleration_longitudinal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration_longitudinal: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration_longitudinal, out);
    out << "\n";
  }

  // member: acceleration_lateral
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration_lateral: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration_lateral, out);
    out << "\n";
  }

  // member: yaw_rate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_rate: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DrivingDynamics & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::DrivingDynamics>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).speed_target,
    std::forward<T>(msg).speed_actual,
    std::forward<T>(msg).steering_angle_target,
    std::forward<T>(msg).steering_angle_actual,
    std::forward<T>(msg).brake_hydr_target,
    std::forward<T>(msg).brake_hydr_actual,
    std::forward<T>(msg).motor_moment_target,
    std::forward<T>(msg).motor_moment_actual,
    std::forward<T>(msg).acceleration_longitudinal,
    std::forward<T>(msg).acceleration_lateral,
    std::forward<T>(msg).yaw_rate);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::DrivingDynamics>()
{
  return "fsd_common_msgs::msg::DrivingDynamics";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::DrivingDynamics>()
{
  return "fsd_common_msgs/msg/DrivingDynamics";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::DrivingDynamics>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::DrivingDynamics>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::DrivingDynamics>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::DrivingDynamics>
{
  static constexpr std::size_t member_count = 12;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "speed_target",
    "speed_actual",
    "steering_angle_target",
    "steering_angle_actual",
    "brake_hydr_target",
    "brake_hydr_actual",
    "motor_moment_target",
    "motor_moment_actual",
    "acceleration_longitudinal",
    "acceleration_lateral",
    "yaw_rate",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__DRIVING_DYNAMICS__TRAITS_HPP_
