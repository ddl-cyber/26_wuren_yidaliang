// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/ConeDbscan.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/cone_dbscan.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__CONE_DBSCAN__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__CONE_DBSCAN__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/cone_dbscan__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/point__traits.hpp"
// Member 'color'
#include "std_msgs/msg/detail/string__traits.hpp"
// Member 'pose_confidence'
// Member 'color_confidence'
#include "std_msgs/msg/detail/float32__traits.hpp"

namespace fsd_common_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ConeDbscan & msg,
  std::ostream & out)
{
  out << "{";
  // member: position
  {
    out << "position: ";
    to_flow_style_yaml(msg.position, out);
    out << ", ";
  }

  // member: color
  {
    out << "color: ";
    to_flow_style_yaml(msg.color, out);
    out << ", ";
  }

  // member: pose_confidence
  {
    out << "pose_confidence: ";
    to_flow_style_yaml(msg.pose_confidence, out);
    out << ", ";
  }

  // member: color_confidence
  {
    out << "color_confidence: ";
    to_flow_style_yaml(msg.color_confidence, out);
    out << ", ";
  }

  // member: cluster
  {
    out << "cluster: ";
    rosidl_generator_traits::value_to_yaml(msg.cluster, out);
    out << ", ";
  }

  // member: point_type
  {
    out << "point_type: ";
    rosidl_generator_traits::value_to_yaml(msg.point_type, out);
    out << ", ";
  }

  // member: pts
  {
    out << "pts: ";
    rosidl_generator_traits::value_to_yaml(msg.pts, out);
    out << ", ";
  }

  // member: visited
  {
    out << "visited: ";
    rosidl_generator_traits::value_to_yaml(msg.visited, out);
    out << ", ";
  }

  // member: corepts
  {
    if (msg.corepts.size() == 0) {
      out << "corepts: []";
    } else {
      out << "corepts: [";
      size_t pending_items = msg.corepts.size();
      for (auto item : msg.corepts) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const ConeDbscan & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position:\n";
    to_block_style_yaml(msg.position, out, indentation + 2);
  }

  // member: color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color:\n";
    to_block_style_yaml(msg.color, out, indentation + 2);
  }

  // member: pose_confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose_confidence:\n";
    to_block_style_yaml(msg.pose_confidence, out, indentation + 2);
  }

  // member: color_confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color_confidence:\n";
    to_block_style_yaml(msg.color_confidence, out, indentation + 2);
  }

  // member: cluster
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cluster: ";
    rosidl_generator_traits::value_to_yaml(msg.cluster, out);
    out << "\n";
  }

  // member: point_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "point_type: ";
    rosidl_generator_traits::value_to_yaml(msg.point_type, out);
    out << "\n";
  }

  // member: pts
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pts: ";
    rosidl_generator_traits::value_to_yaml(msg.pts, out);
    out << "\n";
  }

  // member: visited
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "visited: ";
    rosidl_generator_traits::value_to_yaml(msg.visited, out);
    out << "\n";
  }

  // member: corepts
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.corepts.size() == 0) {
      out << "corepts: []\n";
    } else {
      out << "corepts:\n";
      for (auto item : msg.corepts) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ConeDbscan & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::ConeDbscan>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).position,
    std::forward<T>(msg).color,
    std::forward<T>(msg).pose_confidence,
    std::forward<T>(msg).color_confidence,
    std::forward<T>(msg).cluster,
    std::forward<T>(msg).point_type,
    std::forward<T>(msg).pts,
    std::forward<T>(msg).visited,
    std::forward<T>(msg).corepts);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::ConeDbscan>()
{
  return "fsd_common_msgs::msg::ConeDbscan";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::ConeDbscan>()
{
  return "fsd_common_msgs/msg/ConeDbscan";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::ConeDbscan>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::ConeDbscan>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fsd_common_msgs::msg::ConeDbscan>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::ConeDbscan>
{
  static constexpr std::size_t member_count = 9;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "position",
    "color",
    "pose_confidence",
    "color_confidence",
    "cluster",
    "point_type",
    "pts",
    "visited",
    "corepts",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__CONE_DBSCAN__TRAITS_HPP_
