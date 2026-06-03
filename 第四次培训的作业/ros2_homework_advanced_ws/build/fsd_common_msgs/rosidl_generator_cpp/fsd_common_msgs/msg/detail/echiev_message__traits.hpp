// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/EchievMessage.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/echiev_message.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__ECHIEV_MESSAGE__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__ECHIEV_MESSAGE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/echiev_message__struct.hpp"
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
  const EchievMessage & msg,
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

  // member: ull_timestamp
  {
    out << "ull_timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.ull_timestamp, out);
    out << ", ";
  }

  // member: lat
  {
    out << "lat: ";
    rosidl_generator_traits::value_to_yaml(msg.lat, out);
    out << ", ";
  }

  // member: lon
  {
    out << "lon: ";
    rosidl_generator_traits::value_to_yaml(msg.lon, out);
    out << ", ";
  }

  // member: h
  {
    out << "h: ";
    rosidl_generator_traits::value_to_yaml(msg.h, out);
    out << ", ";
  }

  // member: vn
  {
    out << "vn: ";
    rosidl_generator_traits::value_to_yaml(msg.vn, out);
    out << ", ";
  }

  // member: ve
  {
    out << "ve: ";
    rosidl_generator_traits::value_to_yaml(msg.ve, out);
    out << ", ";
  }

  // member: vh
  {
    out << "vh: ";
    rosidl_generator_traits::value_to_yaml(msg.vh, out);
    out << ", ";
  }

  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << ", ";
  }

  // member: acc_x
  {
    out << "acc_x: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_x, out);
    out << ", ";
  }

  // member: acc_y
  {
    out << "acc_y: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_y, out);
    out << ", ";
  }

  // member: acc_z
  {
    out << "acc_z: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_z, out);
    out << ", ";
  }

  // member: gyro_x
  {
    out << "gyro_x: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_x, out);
    out << ", ";
  }

  // member: gyro_y
  {
    out << "gyro_y: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_y, out);
    out << ", ";
  }

  // member: gyro_z
  {
    out << "gyro_z: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_z, out);
    out << ", ";
  }

  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: gps_state
  {
    out << "gps_state: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const EchievMessage & msg,
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

  // member: ull_timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ull_timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.ull_timestamp, out);
    out << "\n";
  }

  // member: lat
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lat: ";
    rosidl_generator_traits::value_to_yaml(msg.lat, out);
    out << "\n";
  }

  // member: lon
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lon: ";
    rosidl_generator_traits::value_to_yaml(msg.lon, out);
    out << "\n";
  }

  // member: h
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "h: ";
    rosidl_generator_traits::value_to_yaml(msg.h, out);
    out << "\n";
  }

  // member: vn
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vn: ";
    rosidl_generator_traits::value_to_yaml(msg.vn, out);
    out << "\n";
  }

  // member: ve
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ve: ";
    rosidl_generator_traits::value_to_yaml(msg.ve, out);
    out << "\n";
  }

  // member: vh
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vh: ";
    rosidl_generator_traits::value_to_yaml(msg.vh, out);
    out << "\n";
  }

  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
  }

  // member: acc_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_x: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_x, out);
    out << "\n";
  }

  // member: acc_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_y: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_y, out);
    out << "\n";
  }

  // member: acc_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_z: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_z, out);
    out << "\n";
  }

  // member: gyro_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyro_x: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_x, out);
    out << "\n";
  }

  // member: gyro_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyro_y: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_y, out);
    out << "\n";
  }

  // member: gyro_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyro_z: ";
    rosidl_generator_traits::value_to_yaml(msg.gyro_z, out);
    out << "\n";
  }

  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: gps_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gps_state: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const EchievMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::EchievMessage>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).frame_id_num,
    std::forward<T>(msg).ull_timestamp,
    std::forward<T>(msg).lat,
    std::forward<T>(msg).lon,
    std::forward<T>(msg).h,
    std::forward<T>(msg).vn,
    std::forward<T>(msg).ve,
    std::forward<T>(msg).vh,
    std::forward<T>(msg).roll,
    std::forward<T>(msg).pitch,
    std::forward<T>(msg).yaw,
    std::forward<T>(msg).acc_x,
    std::forward<T>(msg).acc_y,
    std::forward<T>(msg).acc_z,
    std::forward<T>(msg).gyro_x,
    std::forward<T>(msg).gyro_y,
    std::forward<T>(msg).gyro_z,
    std::forward<T>(msg).state,
    std::forward<T>(msg).gps_state);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::EchievMessage>()
{
  return "fsd_common_msgs::msg::EchievMessage";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::EchievMessage>()
{
  return "fsd_common_msgs/msg/EchievMessage";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::EchievMessage>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::EchievMessage>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::EchievMessage>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::EchievMessage>
{
  static constexpr std::size_t member_count = 20;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "frame_id_num",
    "ull_timestamp",
    "lat",
    "lon",
    "h",
    "vn",
    "ve",
    "vh",
    "roll",
    "pitch",
    "yaw",
    "acc_x",
    "acc_y",
    "acc_z",
    "gyro_x",
    "gyro_y",
    "gyro_z",
    "state",
    "gps_state",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__ECHIEV_MESSAGE__TRAITS_HPP_
