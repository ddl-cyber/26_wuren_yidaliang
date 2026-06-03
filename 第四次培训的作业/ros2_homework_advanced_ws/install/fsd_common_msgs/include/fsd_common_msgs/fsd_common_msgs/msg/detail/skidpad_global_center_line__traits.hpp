// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/SkidpadGlobalCenterLine.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/skidpad_global_center_line.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__SKIDPAD_GLOBAL_CENTER_LINE__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__SKIDPAD_GLOBAL_CENTER_LINE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/skidpad_global_center_line__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'global_path'
#include "nav_msgs/msg/detail/path__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const SkidpadGlobalCenterLine & msg,
  std::ostream & out)
{
  out << "{";
  // member: global_path
  {
    out << "global_path: ";
    to_flow_style_yaml(msg.global_path, out);
    out << ", ";
  }

  // member: is_reach_mid
  {
    out << "is_reach_mid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_reach_mid, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SkidpadGlobalCenterLine & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: global_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "global_path:\n";
    to_block_style_yaml(msg.global_path, out, indentation + 2);
  }

  // member: is_reach_mid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_reach_mid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_reach_mid, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SkidpadGlobalCenterLine & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::SkidpadGlobalCenterLine>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).global_path,
    std::forward<T>(msg).is_reach_mid);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::SkidpadGlobalCenterLine>()
{
  return "fsd_common_msgs::msg::SkidpadGlobalCenterLine";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::SkidpadGlobalCenterLine>()
{
  return "fsd_common_msgs/msg/SkidpadGlobalCenterLine";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::SkidpadGlobalCenterLine>
  : std::integral_constant<bool, has_fixed_size<nav_msgs::msg::Path>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::SkidpadGlobalCenterLine>
  : std::integral_constant<bool, has_bounded_size<nav_msgs::msg::Path>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::SkidpadGlobalCenterLine>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::SkidpadGlobalCenterLine>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "global_path",
    "is_reach_mid",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__SKIDPAD_GLOBAL_CENTER_LINE__TRAITS_HPP_
