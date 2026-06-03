// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from fsd_common_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#include "fsd_common_msgs/msg/detail/trajectory_point__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_fsd_common_msgs
const rosidl_type_hash_t *
fsd_common_msgs__msg__TrajectoryPoint__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x6b, 0xef, 0xe0, 0x4d, 0x53, 0x96, 0xd0, 0x25,
      0xb2, 0x71, 0xe2, 0xf8, 0x16, 0x6a, 0x81, 0x96,
      0xf3, 0x9a, 0x66, 0xd6, 0xd4, 0x05, 0x07, 0x52,
      0xf6, 0x42, 0xf8, 0xb0, 0xa1, 0x1b, 0xc0, 0x82,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "fsd_common_msgs/msg/detail/car_state__functions.h"
#include "fsd_common_msgs/msg/detail/car_state_dt__functions.h"
#include "fsd_common_msgs/msg/detail/pose2_d__functions.h"
#include "std_msgs/msg/detail/header__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t fsd_common_msgs__msg__CarState__EXPECTED_HASH = {1, {
    0xdd, 0xd5, 0xb5, 0x3a, 0x68, 0x63, 0x43, 0x38,
    0x02, 0x7d, 0xcb, 0xda, 0x3a, 0xb8, 0x93, 0xb5,
    0x85, 0xc1, 0xd3, 0x43, 0x23, 0x32, 0x19, 0x45,
    0x9f, 0x3d, 0x81, 0x09, 0x3a, 0xec, 0x08, 0xcb,
  }};
static const rosidl_type_hash_t fsd_common_msgs__msg__CarStateDt__EXPECTED_HASH = {1, {
    0xbe, 0xbb, 0x61, 0x61, 0xef, 0x87, 0x69, 0x71,
    0x57, 0xd4, 0x4e, 0x79, 0xe0, 0x83, 0xae, 0x1b,
    0x98, 0x1b, 0xa8, 0x64, 0x39, 0x48, 0xa3, 0x45,
    0x89, 0x53, 0xd9, 0x08, 0xba, 0x68, 0xbf, 0x87,
  }};
static const rosidl_type_hash_t fsd_common_msgs__msg__Pose2D__EXPECTED_HASH = {1, {
    0x01, 0x41, 0xdf, 0xf3, 0x28, 0xbe, 0x36, 0x52,
    0x76, 0x46, 0x85, 0x2a, 0xcc, 0xa0, 0x6a, 0x70,
    0x2d, 0xe1, 0x3c, 0x80, 0xbd, 0x5c, 0x92, 0x52,
    0xf0, 0x2e, 0x55, 0x84, 0xae, 0xa9, 0xc4, 0xdb,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char fsd_common_msgs__msg__TrajectoryPoint__TYPE_NAME[] = "fsd_common_msgs/msg/TrajectoryPoint";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char fsd_common_msgs__msg__CarState__TYPE_NAME[] = "fsd_common_msgs/msg/CarState";
static char fsd_common_msgs__msg__CarStateDt__TYPE_NAME[] = "fsd_common_msgs/msg/CarStateDt";
static char fsd_common_msgs__msg__Pose2D__TYPE_NAME[] = "fsd_common_msgs/msg/Pose2D";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char fsd_common_msgs__msg__TrajectoryPoint__FIELD_NAME__header[] = "header";
static char fsd_common_msgs__msg__TrajectoryPoint__FIELD_NAME__trajectory_point[] = "trajectory_point";

static rosidl_runtime_c__type_description__Field fsd_common_msgs__msg__TrajectoryPoint__FIELDS[] = {
  {
    {fsd_common_msgs__msg__TrajectoryPoint__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    },
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__TrajectoryPoint__FIELD_NAME__trajectory_point, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_UNBOUNDED_SEQUENCE,
      0,
      0,
      {fsd_common_msgs__msg__CarState__TYPE_NAME, 28, 28},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription fsd_common_msgs__msg__TrajectoryPoint__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__CarState__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__CarStateDt__TYPE_NAME, 30, 30},
    {NULL, 0, 0},
  },
  {
    {fsd_common_msgs__msg__Pose2D__TYPE_NAME, 26, 26},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
fsd_common_msgs__msg__TrajectoryPoint__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {fsd_common_msgs__msg__TrajectoryPoint__TYPE_NAME, 35, 35},
      {fsd_common_msgs__msg__TrajectoryPoint__FIELDS, 2, 2},
    },
    {fsd_common_msgs__msg__TrajectoryPoint__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&fsd_common_msgs__msg__CarState__EXPECTED_HASH, fsd_common_msgs__msg__CarState__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = fsd_common_msgs__msg__CarState__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&fsd_common_msgs__msg__CarStateDt__EXPECTED_HASH, fsd_common_msgs__msg__CarStateDt__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = fsd_common_msgs__msg__CarStateDt__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&fsd_common_msgs__msg__Pose2D__EXPECTED_HASH, fsd_common_msgs__msg__Pose2D__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = fsd_common_msgs__msg__Pose2D__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "std_msgs/Header header\n"
  "\n"
  "fsd_common_msgs/CarState[] trajectory_point # Velocities";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
fsd_common_msgs__msg__TrajectoryPoint__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {fsd_common_msgs__msg__TrajectoryPoint__TYPE_NAME, 35, 35},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 81, 81},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
fsd_common_msgs__msg__TrajectoryPoint__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *fsd_common_msgs__msg__TrajectoryPoint__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *fsd_common_msgs__msg__CarState__get_individual_type_description_source(NULL);
    sources[3] = *fsd_common_msgs__msg__CarStateDt__get_individual_type_description_source(NULL);
    sources[4] = *fsd_common_msgs__msg__Pose2D__get_individual_type_description_source(NULL);
    sources[5] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
