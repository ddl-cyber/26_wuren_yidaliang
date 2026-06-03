// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/Track.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/track.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/track__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'cones_left'
// Member 'cones_right'
// Member 'cones_orange'
// Member 'cones_orange_big'
// Member 'tk_device_start'
// Member 'tk_device_end'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Track & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: cones_left
  {
    if (msg.cones_left.size() == 0) {
      out << "cones_left: []";
    } else {
      out << "cones_left: [";
      size_t pending_items = msg.cones_left.size();
      for (auto item : msg.cones_left) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: cones_right
  {
    if (msg.cones_right.size() == 0) {
      out << "cones_right: []";
    } else {
      out << "cones_right: [";
      size_t pending_items = msg.cones_right.size();
      for (auto item : msg.cones_right) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: cones_orange
  {
    if (msg.cones_orange.size() == 0) {
      out << "cones_orange: []";
    } else {
      out << "cones_orange: [";
      size_t pending_items = msg.cones_orange.size();
      for (auto item : msg.cones_orange) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: cones_orange_big
  {
    if (msg.cones_orange_big.size() == 0) {
      out << "cones_orange_big: []";
    } else {
      out << "cones_orange_big: [";
      size_t pending_items = msg.cones_orange_big.size();
      for (auto item : msg.cones_orange_big) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: tk_device_start
  {
    if (msg.tk_device_start.size() == 0) {
      out << "tk_device_start: []";
    } else {
      out << "tk_device_start: [";
      size_t pending_items = msg.tk_device_start.size();
      for (auto item : msg.tk_device_start) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: tk_device_end
  {
    if (msg.tk_device_end.size() == 0) {
      out << "tk_device_end: []";
    } else {
      out << "tk_device_end: [";
      size_t pending_items = msg.tk_device_end.size();
      for (auto item : msg.tk_device_end) {
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
  const Track & msg,
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

  // member: cones_left
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cones_left.size() == 0) {
      out << "cones_left: []\n";
    } else {
      out << "cones_left:\n";
      for (auto item : msg.cones_left) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: cones_right
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cones_right.size() == 0) {
      out << "cones_right: []\n";
    } else {
      out << "cones_right:\n";
      for (auto item : msg.cones_right) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: cones_orange
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cones_orange.size() == 0) {
      out << "cones_orange: []\n";
    } else {
      out << "cones_orange:\n";
      for (auto item : msg.cones_orange) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: cones_orange_big
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cones_orange_big.size() == 0) {
      out << "cones_orange_big: []\n";
    } else {
      out << "cones_orange_big:\n";
      for (auto item : msg.cones_orange_big) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: tk_device_start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.tk_device_start.size() == 0) {
      out << "tk_device_start: []\n";
    } else {
      out << "tk_device_start:\n";
      for (auto item : msg.tk_device_start) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: tk_device_end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.tk_device_end.size() == 0) {
      out << "tk_device_end: []\n";
    } else {
      out << "tk_device_end:\n";
      for (auto item : msg.tk_device_end) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Track & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::Track>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).cones_left,
    std::forward<T>(msg).cones_right,
    std::forward<T>(msg).cones_orange,
    std::forward<T>(msg).cones_orange_big,
    std::forward<T>(msg).tk_device_start,
    std::forward<T>(msg).tk_device_end);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::Track>()
{
  return "fsd_common_msgs::msg::Track";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::Track>()
{
  return "fsd_common_msgs/msg/Track";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::Track>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::Track>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fsd_common_msgs::msg::Track>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::Track>
{
  static constexpr std::size_t member_count = 7;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "cones_left",
    "cones_right",
    "cones_orange",
    "cones_orange_big",
    "tk_device_start",
    "tk_device_end",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__TRACK__TRAITS_HPP_
