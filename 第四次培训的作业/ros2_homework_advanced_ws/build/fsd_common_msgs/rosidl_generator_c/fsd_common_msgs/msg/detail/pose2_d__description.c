// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from fsd_common_msgs:msg/Pose2D.idl
// generated code does not contain a copyright notice

#include "fsd_common_msgs/msg/detail/pose2_d__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_fsd_common_msgs
const rosidl_type_hash_t *
fsd_common_msgs__msg__Pose2D__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x01, 0x41, 0xdf, 0xf3, 0x28, 0xbe, 0x36, 0x52,
      0x76, 0x46, 0x85, 0x2a, 0xcc, 0xa0, 0x6a, 0x70,
      0x2d, 0xe1, 0x3c, 0x80, 0xbd, 0x5c, 0x92, 0x52,
      0xf0, 0x2e, 0x55, 0x84, 0xae, 0xa9, 0xc4, 0xdb,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char fsd_common_msgs__msg__Pose2D__TYPE_NAME[] = "fsd_common_msgs/msg/Pose2D";

// Define type names, field names, and default values
static char fsd_common_msgs__msg__Pose2D__FIELD_NAME__x[] = "x";
static char fsd_common_msgs__msg__Pose2D__FIELD_NAME__y[] = "y";
static char fsd_common_msgs__msg__Pose2D__FIELD_NAME__theta[] = "theta";

static rosidl_runtime_c__type_description__Field fsd_common_msgs__msg__Pose2D__FIELDS[] = {
  {
    {fsd_common_msgs__msg__Pose2D__FIELD_NAME__x, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__Pose2D__FIELD_NAME__y, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__Pose2D__FIELD_NAME__theta, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
fsd_common_msgs__msg__Pose2D__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {fsd_common_msgs__msg__Pose2D__TYPE_NAME, 26, 26},
      {fsd_common_msgs__msg__Pose2D__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 x\n"
  "float64 y\n"
  "float64 theta";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
fsd_common_msgs__msg__Pose2D__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {fsd_common_msgs__msg__Pose2D__TYPE_NAME, 26, 26},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 34, 34},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
fsd_common_msgs__msg__Pose2D__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *fsd_common_msgs__msg__Pose2D__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
