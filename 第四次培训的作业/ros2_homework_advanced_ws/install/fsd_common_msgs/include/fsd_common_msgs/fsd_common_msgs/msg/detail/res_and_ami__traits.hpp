// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/ResAndAmi.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/res_and_ami.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__RES_AND_AMI__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__RES_AND_AMI__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/res_and_ami__struct.hpp"
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
  const ResAndAmi & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: res_state
  {
    out << "res_state: ";
    rosidl_generator_traits::value_to_yaml(msg.res_state, out);
    out << ", ";
  }

  // member: mission
  {
    out << "mission: ";
    rosidl_generator_traits::value_to_yaml(msg.mission, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ResAndAmi & msg,
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

  // member: res_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "res_state: ";
    rosidl_generator_traits::value_to_yaml(msg.res_state, out);
    out << "\n";
  }

  // member: mission
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mission: ";
    rosidl_generator_traits::value_to_yaml(msg.mission, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ResAndAmi & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::ResAndAmi>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).res_state,
    std::forward<T>(msg).mission);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::ResAndAmi>()
{
  return "fsd_common_msgs::msg::ResAndAmi";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::ResAndAmi>()
{
  return "fsd_common_msgs/msg/ResAndAmi";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::ResAndAmi>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::ResAndAmi>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fsd_common_msgs::msg::ResAndAmi>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::ResAndAmi>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "res_state",
    "mission",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__RES_AND_AMI__TRAITS_HPP_
