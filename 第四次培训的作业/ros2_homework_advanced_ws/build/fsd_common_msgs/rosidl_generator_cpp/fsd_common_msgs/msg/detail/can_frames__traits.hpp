// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/CanFrames.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/can_frames.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__CAN_FRAMES__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__CAN_FRAMES__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/can_frames__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'frames'
#include "can_msgs/msg/detail/frame__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CanFrames & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: frames
  {
    if (msg.frames.size() == 0) {
      out << "frames: []";
    } else {
      out << "frames: [";
      size_t pending_items = msg.frames.size();
      for (auto item : msg.frames) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CanFrames & msg,
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

  // member: frames
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.frames.size() == 0) {
      out << "frames: []\n";
    } else {
      out << "frames:\n";
      for (auto item : msg.frames) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CanFrames & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::CanFrames>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).frames);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::CanFrames>()
{
  return "fsd_common_msgs::msg::CanFrames";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::CanFrames>()
{
  return "fsd_common_msgs/msg/CanFrames";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::CanFrames>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::CanFrames>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fsd_common_msgs::msg::CanFrames>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::CanFrames>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "frames",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__CAN_FRAMES__TRAITS_HPP_
