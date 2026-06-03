// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/RemoteControlCommand.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/remote_control_command.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__REMOTE_CONTROL_COMMAND__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__REMOTE_CONTROL_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/remote_control_command__struct.hpp"
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
  const RemoteControlCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: throttle
  {
    out << "throttle: ";
    rosidl_generator_traits::value_to_yaml(msg.throttle, out);
    out << ", ";
  }

  // member: steering_angle
  {
    out << "steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle, out);
    out << ", ";
  }

  // member: go
  {
    out << "go: ";
    rosidl_generator_traits::value_to_yaml(msg.go, out);
    out << ", ";
  }

  // member: stop
  {
    out << "stop: ";
    rosidl_generator_traits::value_to_yaml(msg.stop, out);
    out << ", ";
  }

  // member: test1
  {
    out << "test1: ";
    rosidl_generator_traits::value_to_yaml(msg.test1, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RemoteControlCommand & msg,
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

  // member: throttle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "throttle: ";
    rosidl_generator_traits::value_to_yaml(msg.throttle, out);
    out << "\n";
  }

  // member: steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle, out);
    out << "\n";
  }

  // member: go
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "go: ";
    rosidl_generator_traits::value_to_yaml(msg.go, out);
    out << "\n";
  }

  // member: stop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stop: ";
    rosidl_generator_traits::value_to_yaml(msg.stop, out);
    out << "\n";
  }

  // member: test1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "test1: ";
    rosidl_generator_traits::value_to_yaml(msg.test1, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RemoteControlCommand & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::RemoteControlCommand>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).throttle,
    std::forward<T>(msg).steering_angle,
    std::forward<T>(msg).go,
    std::forward<T>(msg).stop,
    std::forward<T>(msg).test1);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::RemoteControlCommand>()
{
  return "fsd_common_msgs::msg::RemoteControlCommand";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::RemoteControlCommand>()
{
  return "fsd_common_msgs/msg/RemoteControlCommand";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::RemoteControlCommand>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::RemoteControlCommand>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::RemoteControlCommand>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::RemoteControlCommand>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "throttle",
    "steering_angle",
    "go",
    "stop",
    "test1",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__REMOTE_CONTROL_COMMAND__TRAITS_HPP_
