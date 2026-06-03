// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fsd_common_msgs:msg/Pose2D.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fsd_common_msgs/msg/pose2_d.h"


#ifndef FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__STRUCT_H_
#define FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Pose2D in the package fsd_common_msgs.
typedef struct fsd_common_msgs__msg__Pose2D
{
  double x;
  double y;
  double theta;
} fsd_common_msgs__msg__Pose2D;

// Struct for a sequence of fsd_common_msgs__msg__Pose2D.
typedef struct fsd_common_msgs__msg__Pose2D__Sequence
{
  fsd_common_msgs__msg__Pose2D * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fsd_common_msgs__msg__Pose2D__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FSD_COMMON_MSGS__MSG__DETAIL__POSE2_D__STRUCT_H_
