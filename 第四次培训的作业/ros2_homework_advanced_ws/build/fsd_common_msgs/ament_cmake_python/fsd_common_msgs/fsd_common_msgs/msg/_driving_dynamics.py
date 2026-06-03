# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/DrivingDynamics.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
import os
import typing

import rosidl_pycommon.interface_base_classes

if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DrivingDynamics(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DrivingDynamics'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DrivingDynamicsConstants(typing.TypedDict):
        pass

    __constants: DrivingDynamicsConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('fsd_common_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fsd_common_msgs.msg.DrivingDynamics')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__driving_dynamics
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__driving_dynamics
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__driving_dynamics
            cls._TYPE_SUPPORT = module.type_support_msg__msg__driving_dynamics
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__driving_dynamics

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DrivingDynamics(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DrivingDynamics):
    """Message class 'DrivingDynamics'."""

    __slots__ = [
        '_header',
        '_speed_target',
        '_speed_actual',
        '_steering_angle_target',
        '_steering_angle_actual',
        '_brake_hydr_target',
        '_brake_hydr_actual',
        '_motor_moment_target',
        '_motor_moment_actual',
        '_acceleration_longitudinal',
        '_acceleration_lateral',
        '_yaw_rate',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'speed_target': 'float',
        'speed_actual': 'float',
        'steering_angle_target': 'float',
        'steering_angle_actual': 'float',
        'brake_hydr_target': 'float',
        'brake_hydr_actual': 'float',
        'motor_moment_target': 'float',
        'motor_moment_actual': 'float',
        'acceleration_longitudinal': 'float',
        'acceleration_lateral': 'float',
        'yaw_rate': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 speed_target: typing.Optional[float] = None,  # noqa: E501
                 speed_actual: typing.Optional[float] = None,  # noqa: E501
                 steering_angle_target: typing.Optional[float] = None,  # noqa: E501
                 steering_angle_actual: typing.Optional[float] = None,  # noqa: E501
                 brake_hydr_target: typing.Optional[float] = None,  # noqa: E501
                 brake_hydr_actual: typing.Optional[float] = None,  # noqa: E501
                 motor_moment_target: typing.Optional[float] = None,  # noqa: E501
                 motor_moment_actual: typing.Optional[float] = None,  # noqa: E501
                 acceleration_longitudinal: typing.Optional[float] = None,  # noqa: E501
                 acceleration_lateral: typing.Optional[float] = None,  # noqa: E501
                 yaw_rate: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.speed_target = speed_target if speed_target is not None else float()
        self.speed_actual = speed_actual if speed_actual is not None else float()
        self.steering_angle_target = steering_angle_target if steering_angle_target is not None else float()
        self.steering_angle_actual = steering_angle_actual if steering_angle_actual is not None else float()
        self.brake_hydr_target = brake_hydr_target if brake_hydr_target is not None else float()
        self.brake_hydr_actual = brake_hydr_actual if brake_hydr_actual is not None else float()
        self.motor_moment_target = motor_moment_target if motor_moment_target is not None else float()
        self.motor_moment_actual = motor_moment_actual if motor_moment_actual is not None else float()
        self.acceleration_longitudinal = acceleration_longitudinal if acceleration_longitudinal is not None else float()
        self.acceleration_lateral = acceleration_lateral if acceleration_lateral is not None else float()
        self.yaw_rate = yaw_rate if yaw_rate is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    from rosidl_buffer import Buffer as _RosidlBuffer
                    if not isinstance(field, _RosidlBuffer):
                        if self._check_fields:
                            assert fieldstr.startswith('array(')
                        prefix = "array('X', "
                        suffix = ')'
                        fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DrivingDynamics):
            return False
        if self.header != other.header:
            return False
        if self.speed_target != other.speed_target:
            return False
        if self.speed_actual != other.speed_actual:
            return False
        if self.steering_angle_target != other.steering_angle_target:
            return False
        if self.steering_angle_actual != other.steering_angle_actual:
            return False
        if self.brake_hydr_target != other.brake_hydr_target:
            return False
        if self.brake_hydr_actual != other.brake_hydr_actual:
            return False
        if self.motor_moment_target != other.motor_moment_target:
            return False
        if self.motor_moment_actual != other.motor_moment_actual:
            return False
        if self.acceleration_longitudinal != other.acceleration_longitudinal:
            return False
        if self.acceleration_lateral != other.acceleration_lateral:
            return False
        if self.yaw_rate != other.yaw_rate:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self) -> std_msgs.msg.Header:
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None:
        from std_msgs.msg import Header

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Header), \
                    "The 'header' field must be a sub message of type 'Header'"

        self._header = value

    @builtins.property
    def speed_target(self) -> float:
        """Message field 'speed_target'."""
        return self._speed_target

    @speed_target.setter
    def speed_target(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'speed_target' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'speed_target' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._speed_target = value

    @builtins.property
    def speed_actual(self) -> float:
        """Message field 'speed_actual'."""
        return self._speed_actual

    @speed_actual.setter
    def speed_actual(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'speed_actual' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'speed_actual' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._speed_actual = value

    @builtins.property
    def steering_angle_target(self) -> float:
        """Message field 'steering_angle_target'."""
        return self._steering_angle_target

    @steering_angle_target.setter
    def steering_angle_target(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'steering_angle_target' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'steering_angle_target' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._steering_angle_target = value

    @builtins.property
    def steering_angle_actual(self) -> float:
        """Message field 'steering_angle_actual'."""
        return self._steering_angle_actual

    @steering_angle_actual.setter
    def steering_angle_actual(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'steering_angle_actual' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'steering_angle_actual' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._steering_angle_actual = value

    @builtins.property
    def brake_hydr_target(self) -> float:
        """Message field 'brake_hydr_target'."""
        return self._brake_hydr_target

    @brake_hydr_target.setter
    def brake_hydr_target(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'brake_hydr_target' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'brake_hydr_target' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._brake_hydr_target = value

    @builtins.property
    def brake_hydr_actual(self) -> float:
        """Message field 'brake_hydr_actual'."""
        return self._brake_hydr_actual

    @brake_hydr_actual.setter
    def brake_hydr_actual(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'brake_hydr_actual' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'brake_hydr_actual' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._brake_hydr_actual = value

    @builtins.property
    def motor_moment_target(self) -> float:
        """Message field 'motor_moment_target'."""
        return self._motor_moment_target

    @motor_moment_target.setter
    def motor_moment_target(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_moment_target' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_moment_target' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_moment_target = value

    @builtins.property
    def motor_moment_actual(self) -> float:
        """Message field 'motor_moment_actual'."""
        return self._motor_moment_actual

    @motor_moment_actual.setter
    def motor_moment_actual(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_moment_actual' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_moment_actual' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_moment_actual = value

    @builtins.property
    def acceleration_longitudinal(self) -> float:
        """Message field 'acceleration_longitudinal'."""
        return self._acceleration_longitudinal

    @acceleration_longitudinal.setter
    def acceleration_longitudinal(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'acceleration_longitudinal' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'acceleration_longitudinal' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._acceleration_longitudinal = value

    @builtins.property
    def acceleration_lateral(self) -> float:
        """Message field 'acceleration_lateral'."""
        return self._acceleration_lateral

    @acceleration_lateral.setter
    def acceleration_lateral(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'acceleration_lateral' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'acceleration_lateral' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._acceleration_lateral = value

    @builtins.property
    def yaw_rate(self) -> float:
        """Message field 'yaw_rate'."""
        return self._yaw_rate

    @yaw_rate.setter
    def yaw_rate(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'yaw_rate' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'yaw_rate' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._yaw_rate = value
