// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/DecisionFlag.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/decision_flag.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__DECISION_FLAG__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__DECISION_FLAG__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/decision_flag__struct.hpp"
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
  const DecisionFlag & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: lap1_state
  {
    out << "lap1_state: ";
    rosidl_generator_traits::value_to_yaml(msg.lap1_state, out);
    out << ", ";
  }

  // member: lap2_state
  {
    out << "lap2_state: ";
    rosidl_generator_traits::value_to_yaml(msg.lap2_state, out);
    out << ", ";
  }

  // member: map_state
  {
    out << "map_state: ";
    rosidl_generator_traits::value_to_yaml(msg.map_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DecisionFlag & msg,
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

  // member: lap1_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lap1_state: ";
    rosidl_generator_traits::value_to_yaml(msg.lap1_state, out);
    out << "\n";
  }

  // member: lap2_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lap2_state: ";
    rosidl_generator_traits::value_to_yaml(msg.lap2_state, out);
    out << "\n";
  }

  // member: map_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_state: ";
    rosidl_generator_traits::value_to_yaml(msg.map_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DecisionFlag & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::DecisionFlag>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).lap1_state,
    std::forward<T>(msg).lap2_state,
    std::forward<T>(msg).map_state);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::DecisionFlag>()
{
  return "fsd_common_msgs::msg::DecisionFlag";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::DecisionFlag>()
{
  return "fsd_common_msgs/msg/DecisionFlag";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::DecisionFlag>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::DecisionFlag>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::DecisionFlag>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::DecisionFlag>
{
  static constexpr std::size_t member_count = 4;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "lap1_state",
    "lap2_state",
    "map_state",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__DECISION_FLAG__TRAITS_HPP_
