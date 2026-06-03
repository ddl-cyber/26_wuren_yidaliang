# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/DecisionFlag.idl
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


class Metaclass_DecisionFlag(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DecisionFlag'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DecisionFlagConstants(typing.TypedDict):
        pass

    __constants: DecisionFlagConstants = {
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
                'fsd_common_msgs.msg.DecisionFlag')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__decision_flag
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__decision_flag
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__decision_flag
            cls._TYPE_SUPPORT = module.type_support_msg__msg__decision_flag
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__decision_flag

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


class DecisionFlag(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DecisionFlag):
    """Message class 'DecisionFlag'."""

    __slots__ = [
        '_header',
        '_lap1_state',
        '_lap2_state',
        '_map_state',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'lap1_state': 'uint8',
        'lap2_state': 'uint8',
        'map_state': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 lap1_state: typing.Optional[int] = None,  # noqa: E501
                 lap2_state: typing.Optional[int] = None,  # noqa: E501
                 map_state: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.lap1_state = lap1_state if lap1_state is not None else int()
        self.lap2_state = lap2_state if lap2_state is not None else int()
        self.map_state = map_state if map_state is not None else int()

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
        if not isinstance(other, DecisionFlag):
            return False
        if self.header != other.header:
            return False
        if self.lap1_state != other.lap1_state:
            return False
        if self.lap2_state != other.lap2_state:
            return False
        if self.map_state != other.map_state:
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
    def lap1_state(self) -> int:
        """Message field 'lap1_state'."""
        return self._lap1_state

    @lap1_state.setter
    def lap1_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'lap1_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'lap1_state' field must be an unsigned integer in [0, 255]"

        self._lap1_state = value

    @builtins.property
    def lap2_state(self) -> int:
        """Message field 'lap2_state'."""
        return self._lap2_state

    @lap2_state.setter
    def lap2_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'lap2_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'lap2_state' field must be an unsigned integer in [0, 255]"

        self._lap2_state = value

    @builtins.property
    def map_state(self) -> int:
        """Message field 'map_state'."""
        return self._map_state

    @map_state.setter
    def map_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'map_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'map_state' field must be an unsigned integer in [0, 255]"

        self._map_state = value
