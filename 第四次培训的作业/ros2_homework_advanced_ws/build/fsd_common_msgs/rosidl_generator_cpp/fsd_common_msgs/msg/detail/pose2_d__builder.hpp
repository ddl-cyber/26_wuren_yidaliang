// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fsd_common_msgs:msg/Pose2D.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/pose2_d.hpp"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__BUILDER_HPP_
#define FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fsd_common_msgs/msg/detail/pose2_d__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fsd_common_msgs
{

namespace msg
{

namespace builder
{

class Init_Pose2D_theta
{
public:
  explicit Init_Pose2D_theta(::fsd_common_msgs::msg::Pose2D & msg)
  : msg_(msg)
  {}
  ::fsd_common_msgs::msg::Pose2D theta(::fsd_common_msgs::msg::Pose2D::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fsd_common_msgs::msg::Pose2D msg_;
};

class Init_Pose2D_y
{
public:
  explicit Init_Pose2D_y(::fsd_common_msgs::msg::Pose2D & msg)
  : msg_(msg)
  {}
  Init_Pose2D_theta y(::fsd_common_msgs::msg::Pose2D::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Pose2D_theta(msg_);
  }

private:
  ::fsd_common_msgs::msg::Pose2D msg_;
};

class Init_Pose2D_x
{
public:
  Init_Pose2D_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pose2D_y x(::fsd_common_msgs::msg::Pose2D::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Pose2D_y(msg_);
  }

private:
  ::fsd_common_msgs::msg::Pose2D msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fsd_common_msgs::msg::Pose2D>()
{
  return fsd_common_msgs::msg::builder::Init_Pose2D_x();
}

}  // namespace fsd_common_msgs

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__BUILDER_HPP_
