# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/YoloCone.idl
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

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_YoloCone(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'YoloCone'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class YoloConeConstants(typing.TypedDict):
        pass

    __constants: YoloConeConstants = {
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
                'fsd_common_msgs.msg.YoloCone')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__yolo_cone
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__yolo_cone
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__yolo_cone
            cls._TYPE_SUPPORT = module.type_support_msg__msg__yolo_cone
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__yolo_cone

            from std_msgs.msg import Float32
            if Float32._TYPE_SUPPORT is None:
                Float32.__import_type_support__()

            from std_msgs.msg import String
            if String._TYPE_SUPPORT is None:
                String.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class YoloCone(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_YoloCone):
    """Message class 'YoloCone'."""

    __slots__ = [
        '_x',
        '_y',
        '_width',
        '_height',
        '_color',
        '_color_confidence',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'x': 'std_msgs/Float32',
        'y': 'std_msgs/Float32',
        'width': 'std_msgs/Float32',
        'height': 'std_msgs/Float32',
        'color': 'std_msgs/String',
        'color_confidence': 'std_msgs/Float32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'String'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
    )

    def __init__(self, *,
                 x: typing.Optional[std_msgs.msg.Float32] = None,  # noqa: E501
                 y: typing.Optional[std_msgs.msg.Float32] = None,  # noqa: E501
                 width: typing.Optional[std_msgs.msg.Float32] = None,  # noqa: E501
                 height: typing.Optional[std_msgs.msg.Float32] = None,  # noqa: E501
                 color: typing.Optional[std_msgs.msg.String] = None,  # noqa: E501
                 color_confidence: typing.Optional[std_msgs.msg.Float32] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Float32
        self.x = x if x is not None else Float32()
        from std_msgs.msg import Float32
        self.y = y if y is not None else Float32()
        from std_msgs.msg import Float32
        self.width = width if width is not None else Float32()
        from std_msgs.msg import Float32
        self.height = height if height is not None else Float32()
        from std_msgs.msg import String
        self.color = color if color is not None else String()
        from std_msgs.msg import Float32
        self.color_confidence = color_confidence if color_confidence is not None else Float32()

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
        if not isinstance(other, YoloCone):
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.width != other.width:
            return False
        if self.height != other.height:
            return False
        if self.color != other.color:
            return False
        if self.color_confidence != other.color_confidence:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x(self) -> std_msgs.msg.Float32:
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value: std_msgs.msg.Float32) -> None:
        from std_msgs.msg import Float32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Float32), \
                    "The 'x' field must be a sub message of type 'Float32'"

        self._x = value

    @builtins.property
    def y(self) -> std_msgs.msg.Float32:
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value: std_msgs.msg.Float32) -> None:
        from std_msgs.msg import Float32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Float32), \
                    "The 'y' field must be a sub message of type 'Float32'"

        self._y = value

    @builtins.property
    def width(self) -> std_msgs.msg.Float32:
        """Message field 'width'."""
        return self._width

    @width.setter
    def width(self, value: std_msgs.msg.Float32) -> None:
        from std_msgs.msg import Float32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Float32), \
                    "The 'width' field must be a sub message of type 'Float32'"

        self._width = value

    @builtins.property
    def height(self) -> std_msgs.msg.Float32:
        """Message field 'height'."""
        return self._height

    @height.setter
    def height(self, value: std_msgs.msg.Float32) -> None:
        from std_msgs.msg import Float32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Float32), \
                    "The 'height' field must be a sub message of type 'Float32'"

        self._height = value

    @builtins.property
    def color(self) -> std_msgs.msg.String:
        """Message field 'color'."""
        return self._color

    @color.setter
    def color(self, value: std_msgs.msg.String) -> None:
        from std_msgs.msg import String

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, String), \
                    "The 'color' field must be a sub message of type 'String'"

        self._color = value

    @builtins.property
    def color_confidence(self) -> std_msgs.msg.Float32:
        """Message field 'color_confidence'."""
        return self._color_confidence

    @color_confidence.setter
    def color_confidence(self, value: std_msgs.msg.Float32) -> None:
        from std_msgs.msg import Float32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Float32), \
                    "The 'color_confidence' field must be a sub message of type 'Float32'"

        self._color_confidence = value
