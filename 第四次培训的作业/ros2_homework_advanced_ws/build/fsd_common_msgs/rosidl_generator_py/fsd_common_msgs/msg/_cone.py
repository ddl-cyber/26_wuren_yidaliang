# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/Cone.idl
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
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Cone(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Cone'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ConeConstants(typing.TypedDict):
        pass

    __constants: ConeConstants = {
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
                'fsd_common_msgs.msg.Cone')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__cone
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__cone
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__cone
            cls._TYPE_SUPPORT = module.type_support_msg__msg__cone
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__cone

            from geometry_msgs.msg import Point
            if Point._TYPE_SUPPORT is None:
                Point.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Cone(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Cone):
    """Message class 'Cone'."""

    __slots__ = [
        '_position',
        '_color',
        '_pose_confidence',
        '_color_confidence',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'position': 'geometry_msgs/Point',
        'color': 'string',
        'pose_confidence': 'double',
        'color_confidence': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 position: typing.Optional[geometry_msgs.msg.Point] = None,  # noqa: E501
                 color: typing.Optional[str] = None,  # noqa: E501
                 pose_confidence: typing.Optional[float] = None,  # noqa: E501
                 color_confidence: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from geometry_msgs.msg import Point
        self.position = position if position is not None else Point()
        self.color = color if color is not None else str()
        self.pose_confidence = pose_confidence if pose_confidence is not None else float()
        self.color_confidence = color_confidence if color_confidence is not None else float()

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
        if not isinstance(other, Cone):
            return False
        if self.position != other.position:
            return False
        if self.color != other.color:
            return False
        if self.pose_confidence != other.pose_confidence:
            return False
        if self.color_confidence != other.color_confidence:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def position(self) -> geometry_msgs.msg.Point:
        """Message field 'position'."""
        return self._position

    @position.setter
    def position(self, value: geometry_msgs.msg.Point) -> None:
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Point), \
                    "The 'position' field must be a sub message of type 'Point'"

        self._position = value

    @builtins.property
    def color(self) -> str:
        """Message field 'color'."""
        return self._color

    @color.setter
    def color(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'color' field must be of type 'str'"

        self._color = value

    @builtins.property
    def pose_confidence(self) -> float:
        """Message field 'pose_confidence'."""
        return self._pose_confidence

    @pose_confidence.setter
    def pose_confidence(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'pose_confidence' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'pose_confidence' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._pose_confidence = value

    @builtins.property
    def color_confidence(self) -> float:
        """Message field 'color_confidence'."""
        return self._color_confidence

    @color_confidence.setter
    def color_confidence(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'color_confidence' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'color_confidence' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._color_confidence = value
