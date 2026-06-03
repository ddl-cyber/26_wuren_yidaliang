# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/SkidpadGlobalCenterLine.idl
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
    import nav_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SkidpadGlobalCenterLine(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SkidpadGlobalCenterLine'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SkidpadGlobalCenterLineConstants(typing.TypedDict):
        pass

    __constants: SkidpadGlobalCenterLineConstants = {
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
                'fsd_common_msgs.msg.SkidpadGlobalCenterLine')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__skidpad_global_center_line
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__skidpad_global_center_line
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__skidpad_global_center_line
            cls._TYPE_SUPPORT = module.type_support_msg__msg__skidpad_global_center_line
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__skidpad_global_center_line

            from nav_msgs.msg import Path
            if Path._TYPE_SUPPORT is None:
                Path.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SkidpadGlobalCenterLine(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SkidpadGlobalCenterLine):
    """Message class 'SkidpadGlobalCenterLine'."""

    __slots__ = [
        '_global_path',
        '_is_reach_mid',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'global_path': 'nav_msgs/Path',
        'is_reach_mid': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'Path'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, *,
                 global_path: typing.Optional[nav_msgs.msg.Path] = None,  # noqa: E501
                 is_reach_mid: typing.Optional[bool] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav_msgs.msg import Path
        self.global_path = global_path if global_path is not None else Path()
        self.is_reach_mid = is_reach_mid if is_reach_mid is not None else bool()

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
        if not isinstance(other, SkidpadGlobalCenterLine):
            return False
        if self.global_path != other.global_path:
            return False
        if self.is_reach_mid != other.is_reach_mid:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def global_path(self) -> nav_msgs.msg.Path:
        """Message field 'global_path'."""
        return self._global_path

    @global_path.setter
    def global_path(self, value: nav_msgs.msg.Path) -> None:
        from nav_msgs.msg import Path

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Path), \
                    "The 'global_path' field must be a sub message of type 'Path'"

        self._global_path = value

    @builtins.property
    def is_reach_mid(self) -> bool:
        """Message field 'is_reach_mid'."""
        return self._is_reach_mid

    @is_reach_mid.setter
    def is_reach_mid(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'is_reach_mid' field must be of type 'bool'"

        self._is_reach_mid = value
