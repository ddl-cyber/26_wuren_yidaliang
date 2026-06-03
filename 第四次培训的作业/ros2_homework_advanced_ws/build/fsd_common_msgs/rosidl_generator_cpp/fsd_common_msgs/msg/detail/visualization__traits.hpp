// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsd_common_msgs:msg/Visualization.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/visualization.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__VISUALIZATION__TRAITS_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__VISUALIZATION__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fsd_common_msgs/msg/detail/visualization__struct.hpp"
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
  const Visualization & msg,
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

  // member: lat_error_front_axis
  {
    out << "lat_error_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_front_axis, out);
    out << ", ";
  }

  // member: lat_error_cog
  {
    out << "lat_error_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_cog, out);
    out << ", ";
  }

  // member: lat_error_rear_axis
  {
    out << "lat_error_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_rear_axis, out);
    out << ", ";
  }

  // member: yaw_error_front_axis
  {
    out << "yaw_error_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_front_axis, out);
    out << ", ";
  }

  // member: yaw_error_cog
  {
    out << "yaw_error_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_cog, out);
    out << ", ";
  }

  // member: yaw_error_rear_axis
  {
    out << "yaw_error_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_rear_axis, out);
    out << ", ";
  }

  // member: yaw_rate_error
  {
    out << "yaw_rate_error: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate_error, out);
    out << ", ";
  }

  // member: steering_error
  {
    out << "steering_error: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_error, out);
    out << ", ";
  }

  // member: vx_error
  {
    out << "vx_error: ";
    rosidl_generator_traits::value_to_yaml(msg.vx_error, out);
    out << ", ";
  }

  // member: vy_error
  {
    out << "vy_error: ";
    rosidl_generator_traits::value_to_yaml(msg.vy_error, out);
    out << ", ";
  }

  // member: sideslip_error
  {
    out << "sideslip_error: ";
    rosidl_generator_traits::value_to_yaml(msg.sideslip_error, out);
    out << ", ";
  }

  // member: motor_torq_error_lr
  {
    out << "motor_torq_error_lr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_torq_error_lr, out);
    out << ", ";
  }

  // member: motor_torq_error_rr
  {
    out << "motor_torq_error_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_torq_error_rr, out);
    out << ", ";
  }

  // member: motor_speed_error_lr
  {
    out << "motor_speed_error_lr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_speed_error_lr, out);
    out << ", ";
  }

  // member: motor_speed_error_rr
  {
    out << "motor_speed_error_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_speed_error_rr, out);
    out << ", ";
  }

  // member: error1
  {
    out << "error1: ";
    rosidl_generator_traits::value_to_yaml(msg.error1, out);
    out << ", ";
  }

  // member: error2
  {
    out << "error2: ";
    rosidl_generator_traits::value_to_yaml(msg.error2, out);
    out << ", ";
  }

  // member: error3
  {
    out << "error3: ";
    rosidl_generator_traits::value_to_yaml(msg.error3, out);
    out << ", ";
  }

  // member: error4
  {
    out << "error4: ";
    rosidl_generator_traits::value_to_yaml(msg.error4, out);
    out << ", ";
  }

  // member: yaw_ref
  {
    out << "yaw_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref, out);
    out << ", ";
  }

  // member: yaw_ref_front_axis
  {
    out << "yaw_ref_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_front_axis, out);
    out << ", ";
  }

  // member: yaw_ref_cog
  {
    out << "yaw_ref_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_cog, out);
    out << ", ";
  }

  // member: yaw_ref_rear_axis
  {
    out << "yaw_ref_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_rear_axis, out);
    out << ", ";
  }

  // member: curvature_ref
  {
    out << "curvature_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref, out);
    out << ", ";
  }

  // member: curvature_ref_front_axis
  {
    out << "curvature_ref_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_front_axis, out);
    out << ", ";
  }

  // member: curvature_ref_cog
  {
    out << "curvature_ref_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_cog, out);
    out << ", ";
  }

  // member: curvature_ref_rear_axis
  {
    out << "curvature_ref_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_rear_axis, out);
    out << ", ";
  }

  // member: vx_ref
  {
    out << "vx_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.vx_ref, out);
    out << ", ";
  }

  // member: vy_ref
  {
    out << "vy_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.vy_ref, out);
    out << ", ";
  }

  // member: ax_ref
  {
    out << "ax_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.ax_ref, out);
    out << ", ";
  }

  // member: ay_ref
  {
    out << "ay_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.ay_ref, out);
    out << ", ";
  }

  // member: ref1
  {
    out << "ref1: ";
    rosidl_generator_traits::value_to_yaml(msg.ref1, out);
    out << ", ";
  }

  // member: ref2
  {
    out << "ref2: ";
    rosidl_generator_traits::value_to_yaml(msg.ref2, out);
    out << ", ";
  }

  // member: ref3
  {
    out << "ref3: ";
    rosidl_generator_traits::value_to_yaml(msg.ref3, out);
    out << ", ";
  }

  // member: ref4
  {
    out << "ref4: ";
    rosidl_generator_traits::value_to_yaml(msg.ref4, out);
    out << ", ";
  }

  // member: steering_without_compensation
  {
    out << "steering_without_compensation: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_without_compensation, out);
    out << ", ";
  }

  // member: steering_feedback
  {
    out << "steering_feedback: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_feedback, out);
    out << ", ";
  }

  // member: steering_feedforward
  {
    out << "steering_feedforward: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_feedforward, out);
    out << ", ";
  }

  // member: lookforward_length
  {
    out << "lookforward_length: ";
    rosidl_generator_traits::value_to_yaml(msg.lookforward_length, out);
    out << ", ";
  }

  // member: yaw_rate_pre
  {
    out << "yaw_rate_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate_pre, out);
    out << ", ";
  }

  // member: turning_radius
  {
    out << "turning_radius: ";
    rosidl_generator_traits::value_to_yaml(msg.turning_radius, out);
    out << ", ";
  }

  // member: adhesion_coefficient_pre
  {
    out << "adhesion_coefficient_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.adhesion_coefficient_pre, out);
    out << ", ";
  }

  // member: sideslip_pre
  {
    out << "sideslip_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.sideslip_pre, out);
    out << ", ";
  }

  // member: slip_angle_pre_fl
  {
    out << "slip_angle_pre_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_fl, out);
    out << ", ";
  }

  // member: slip_angle_pre_fr
  {
    out << "slip_angle_pre_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_fr, out);
    out << ", ";
  }

  // member: slip_angle_pre_rl
  {
    out << "slip_angle_pre_rl: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_rl, out);
    out << ", ";
  }

  // member: slip_angle_pre_rr
  {
    out << "slip_angle_pre_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_rr, out);
    out << ", ";
  }

  // member: norm_force_pre_fl
  {
    out << "norm_force_pre_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_fl, out);
    out << ", ";
  }

  // member: norm_force_pre_fr
  {
    out << "norm_force_pre_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_fr, out);
    out << ", ";
  }

  // member: norm_force_pre_rl
  {
    out << "norm_force_pre_rl: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_rl, out);
    out << ", ";
  }

  // member: norm_force_pre_rr
  {
    out << "norm_force_pre_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_rr, out);
    out << ", ";
  }

  // member: algorithm1
  {
    out << "algorithm1: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm1, out);
    out << ", ";
  }

  // member: algorithm2
  {
    out << "algorithm2: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm2, out);
    out << ", ";
  }

  // member: algorithm3
  {
    out << "algorithm3: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm3, out);
    out << ", ";
  }

  // member: algorithm4
  {
    out << "algorithm4: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm4, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Visualization & msg,
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

  // member: lat_error_front_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lat_error_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_front_axis, out);
    out << "\n";
  }

  // member: lat_error_cog
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lat_error_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_cog, out);
    out << "\n";
  }

  // member: lat_error_rear_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lat_error_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_error_rear_axis, out);
    out << "\n";
  }

  // member: yaw_error_front_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_error_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_front_axis, out);
    out << "\n";
  }

  // member: yaw_error_cog
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_error_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_cog, out);
    out << "\n";
  }

  // member: yaw_error_rear_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_error_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_error_rear_axis, out);
    out << "\n";
  }

  // member: yaw_rate_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_rate_error: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate_error, out);
    out << "\n";
  }

  // member: steering_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_error: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_error, out);
    out << "\n";
  }

  // member: vx_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vx_error: ";
    rosidl_generator_traits::value_to_yaml(msg.vx_error, out);
    out << "\n";
  }

  // member: vy_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vy_error: ";
    rosidl_generator_traits::value_to_yaml(msg.vy_error, out);
    out << "\n";
  }

  // member: sideslip_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sideslip_error: ";
    rosidl_generator_traits::value_to_yaml(msg.sideslip_error, out);
    out << "\n";
  }

  // member: motor_torq_error_lr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_torq_error_lr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_torq_error_lr, out);
    out << "\n";
  }

  // member: motor_torq_error_rr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_torq_error_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_torq_error_rr, out);
    out << "\n";
  }

  // member: motor_speed_error_lr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_speed_error_lr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_speed_error_lr, out);
    out << "\n";
  }

  // member: motor_speed_error_rr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_speed_error_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_speed_error_rr, out);
    out << "\n";
  }

  // member: error1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error1: ";
    rosidl_generator_traits::value_to_yaml(msg.error1, out);
    out << "\n";
  }

  // member: error2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error2: ";
    rosidl_generator_traits::value_to_yaml(msg.error2, out);
    out << "\n";
  }

  // member: error3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error3: ";
    rosidl_generator_traits::value_to_yaml(msg.error3, out);
    out << "\n";
  }

  // member: error4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error4: ";
    rosidl_generator_traits::value_to_yaml(msg.error4, out);
    out << "\n";
  }

  // member: yaw_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref, out);
    out << "\n";
  }

  // member: yaw_ref_front_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_ref_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_front_axis, out);
    out << "\n";
  }

  // member: yaw_ref_cog
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_ref_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_cog, out);
    out << "\n";
  }

  // member: yaw_ref_rear_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_ref_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_ref_rear_axis, out);
    out << "\n";
  }

  // member: curvature_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "curvature_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref, out);
    out << "\n";
  }

  // member: curvature_ref_front_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "curvature_ref_front_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_front_axis, out);
    out << "\n";
  }

  // member: curvature_ref_cog
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "curvature_ref_cog: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_cog, out);
    out << "\n";
  }

  // member: curvature_ref_rear_axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "curvature_ref_rear_axis: ";
    rosidl_generator_traits::value_to_yaml(msg.curvature_ref_rear_axis, out);
    out << "\n";
  }

  // member: vx_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vx_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.vx_ref, out);
    out << "\n";
  }

  // member: vy_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vy_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.vy_ref, out);
    out << "\n";
  }

  // member: ax_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ax_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.ax_ref, out);
    out << "\n";
  }

  // member: ay_ref
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ay_ref: ";
    rosidl_generator_traits::value_to_yaml(msg.ay_ref, out);
    out << "\n";
  }

  // member: ref1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ref1: ";
    rosidl_generator_traits::value_to_yaml(msg.ref1, out);
    out << "\n";
  }

  // member: ref2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ref2: ";
    rosidl_generator_traits::value_to_yaml(msg.ref2, out);
    out << "\n";
  }

  // member: ref3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ref3: ";
    rosidl_generator_traits::value_to_yaml(msg.ref3, out);
    out << "\n";
  }

  // member: ref4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ref4: ";
    rosidl_generator_traits::value_to_yaml(msg.ref4, out);
    out << "\n";
  }

  // member: steering_without_compensation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_without_compensation: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_without_compensation, out);
    out << "\n";
  }

  // member: steering_feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_feedback: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_feedback, out);
    out << "\n";
  }

  // member: steering_feedforward
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_feedforward: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_feedforward, out);
    out << "\n";
  }

  // member: lookforward_length
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lookforward_length: ";
    rosidl_generator_traits::value_to_yaml(msg.lookforward_length, out);
    out << "\n";
  }

  // member: yaw_rate_pre
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_rate_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_rate_pre, out);
    out << "\n";
  }

  // member: turning_radius
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "turning_radius: ";
    rosidl_generator_traits::value_to_yaml(msg.turning_radius, out);
    out << "\n";
  }

  // member: adhesion_coefficient_pre
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "adhesion_coefficient_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.adhesion_coefficient_pre, out);
    out << "\n";
  }

  // member: sideslip_pre
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sideslip_pre: ";
    rosidl_generator_traits::value_to_yaml(msg.sideslip_pre, out);
    out << "\n";
  }

  // member: slip_angle_pre_fl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slip_angle_pre_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_fl, out);
    out << "\n";
  }

  // member: slip_angle_pre_fr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slip_angle_pre_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_fr, out);
    out << "\n";
  }

  // member: slip_angle_pre_rl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slip_angle_pre_rl: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_rl, out);
    out << "\n";
  }

  // member: slip_angle_pre_rr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slip_angle_pre_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.slip_angle_pre_rr, out);
    out << "\n";
  }

  // member: norm_force_pre_fl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "norm_force_pre_fl: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_fl, out);
    out << "\n";
  }

  // member: norm_force_pre_fr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "norm_force_pre_fr: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_fr, out);
    out << "\n";
  }

  // member: norm_force_pre_rl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "norm_force_pre_rl: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_rl, out);
    out << "\n";
  }

  // member: norm_force_pre_rr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "norm_force_pre_rr: ";
    rosidl_generator_traits::value_to_yaml(msg.norm_force_pre_rr, out);
    out << "\n";
  }

  // member: algorithm1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "algorithm1: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm1, out);
    out << "\n";
  }

  // member: algorithm2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "algorithm2: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm2, out);
    out << "\n";
  }

  // member: algorithm3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "algorithm3: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm3, out);
    out << "\n";
  }

  // member: algorithm4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "algorithm4: ";
    rosidl_generator_traits::value_to_yaml(msg.algorithm4, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Visualization & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fsd_common_msgs::msg::Visualization>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).frame_id_num,
    std::forward<T>(msg).lat_error_front_axis,
    std::forward<T>(msg).lat_error_cog,
    std::forward<T>(msg).lat_error_rear_axis,
    std::forward<T>(msg).yaw_error_front_axis,
    std::forward<T>(msg).yaw_error_cog,
    std::forward<T>(msg).yaw_error_rear_axis,
    std::forward<T>(msg).yaw_rate_error,
    std::forward<T>(msg).steering_error,
    std::forward<T>(msg).vx_error,
    std::forward<T>(msg).vy_error,
    std::forward<T>(msg).sideslip_error,
    std::forward<T>(msg).motor_torq_error_lr,
    std::forward<T>(msg).motor_torq_error_rr,
    std::forward<T>(msg).motor_speed_error_lr,
    std::forward<T>(msg).motor_speed_error_rr,
    std::forward<T>(msg).error1,
    std::forward<T>(msg).error2,
    std::forward<T>(msg).error3,
    std::forward<T>(msg).error4,
    std::forward<T>(msg).yaw_ref,
    std::forward<T>(msg).yaw_ref_front_axis,
    std::forward<T>(msg).yaw_ref_cog,
    std::forward<T>(msg).yaw_ref_rear_axis,
    std::forward<T>(msg).curvature_ref,
    std::forward<T>(msg).curvature_ref_front_axis,
    std::forward<T>(msg).curvature_ref_cog,
    std::forward<T>(msg).curvature_ref_rear_axis,
    std::forward<T>(msg).vx_ref,
    std::forward<T>(msg).vy_ref,
    std::forward<T>(msg).ax_ref,
    std::forward<T>(msg).ay_ref,
    std::forward<T>(msg).ref1,
    std::forward<T>(msg).ref2,
    std::forward<T>(msg).ref3,
    std::forward<T>(msg).ref4,
    std::forward<T>(msg).steering_without_compensation,
    std::forward<T>(msg).steering_feedback,
    std::forward<T>(msg).steering_feedforward,
    std::forward<T>(msg).lookforward_length,
    std::forward<T>(msg).yaw_rate_pre,
    std::forward<T>(msg).turning_radius,
    std::forward<T>(msg).adhesion_coefficient_pre,
    std::forward<T>(msg).sideslip_pre,
    std::forward<T>(msg).slip_angle_pre_fl,
    std::forward<T>(msg).slip_angle_pre_fr,
    std::forward<T>(msg).slip_angle_pre_rl,
    std::forward<T>(msg).slip_angle_pre_rr,
    std::forward<T>(msg).norm_force_pre_fl,
    std::forward<T>(msg).norm_force_pre_fr,
    std::forward<T>(msg).norm_force_pre_rl,
    std::forward<T>(msg).norm_force_pre_rr,
    std::forward<T>(msg).algorithm1,
    std::forward<T>(msg).algorithm2,
    std::forward<T>(msg).algorithm3,
    std::forward<T>(msg).algorithm4);
}

}  // namespace msg

}  // namespace fsd_common_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fsd_common_msgs::msg::Visualization>()
{
  return "fsd_common_msgs::msg::Visualization";
}

template<>
constexpr const char * name<fsd_common_msgs::msg::Visualization>()
{
  return "fsd_common_msgs/msg/Visualization";
}

template<>
struct has_fixed_size<fsd_common_msgs::msg::Visualization>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsd_common_msgs::msg::Visualization>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsd_common_msgs::msg::Visualization>
  : std::true_type {};

template<>
struct MessageTraits<fsd_common_msgs::msg::Visualization>
{
  static constexpr std::size_t member_count = 57;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "frame_id_num",
    "lat_error_front_axis",
    "lat_error_cog",
    "lat_error_rear_axis",
    "yaw_error_front_axis",
    "yaw_error_cog",
    "yaw_error_rear_axis",
    "yaw_rate_error",
    "steering_error",
    "vx_error",
    "vy_error",
    "sideslip_error",
    "motor_torq_error_lr",
    "motor_torq_error_rr",
    "motor_speed_error_lr",
    "motor_speed_error_rr",
    "error1",
    "error2",
    "error3",
    "error4",
    "yaw_ref",
    "yaw_ref_front_axis",
    "yaw_ref_cog",
    "yaw_ref_rear_axis",
    "curvature_ref",
    "curvature_ref_front_axis",
    "curvature_ref_cog",
    "curvature_ref_rear_axis",
    "vx_ref",
    "vy_ref",
    "ax_ref",
    "ay_ref",
    "ref1",
    "ref2",
    "ref3",
    "ref4",
    "steering_without_compensation",
    "steering_feedback",
    "steering_feedforward",
    "lookforward_length",
    "yaw_rate_pre",
    "turning_radius",
    "adhesion_coefficient_pre",
    "sideslip_pre",
    "slip_angle_pre_fl",
    "slip_angle_pre_fr",
    "slip_angle_pre_rl",
    "slip_angle_pre_rr",
    "norm_force_pre_fl",
    "norm_force_pre_fr",
    "norm_force_pre_rl",
    "norm_force_pre_rr",
    "algorithm1",
    "algorithm2",
    "algorithm3",
    "algorithm4",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__VISUALIZATION__TRAITS_HPP_
