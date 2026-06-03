// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/CarStateDt.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/car_state_dt.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__CAR_STATE_DT__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__CAR_STATE_DT__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/car_state_dt__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'car_state_dt'
#include "fsd_common_msgs/msg/detail/pose2_d__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CarStateDt & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: car_state_dt
  {
    out << "car_state_dt: ";
    to_flow_style_yaml(msg.car_state_dt, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CarStateDt & msg,
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

  // member: car_state_dt
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "car_state_dt:\n";
    to_block_style_yaml(msg.car_state_dt, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CarStateDt & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::CarStateDt>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).car_state_dt);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::CarStateDt>()
{
  return "fsd_common_msgs::msg::CarStateDt";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::CarStateDt>()
{
  return "fsd_common_msgs/msg/CarStateDt";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::CarStateDt>
  : std::integral_constant<bool, has_fixed_size<fsd_common_msgs::msg::Pose2D>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::CarStateDt>
  : std::integral_constant<bool, has_bounded_size<fsd_common_msgs::msg::Pose2D>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::CarStateDt>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::CarStateDt>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "car_state_dt",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__CAR_STATE_DT__TRAITS_HPP_
