# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/Map.idl
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
    import fsd_common_msgs.msg  # noqa: E402, I100, I201, I300
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Map(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Map'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class MapConstants(typing.TypedDict):
        pass

    __constants: MapConstants = {
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
                'fsd_common_msgs.msg.Map')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__map
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__map
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__map
            cls._TYPE_SUPPORT = module.type_support_msg__msg__map
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__map

            from fsd_common_msgs.msg import Cone
            if Cone._TYPE_SUPPORT is None:
                Cone.__import_type_support__()

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


class Map(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Map):
    """Message class 'Map'."""

    __slots__ = [
        '_header',
        '_cone_yellow',
        '_cone_blue',
        '_cone_red',
        '_cone_unknown',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'cone_yellow': 'sequence<fsd_common_msgs/Cone>',
        'cone_blue': 'sequence<fsd_common_msgs/Cone>',
        'cone_red': 'sequence<fsd_common_msgs/Cone>',
        'cone_unknown': 'sequence<fsd_common_msgs/Cone>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['fsd_common_msgs', 'msg'], 'Cone')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['fsd_common_msgs', 'msg'], 'Cone')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['fsd_common_msgs', 'msg'], 'Cone')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['fsd_common_msgs', 'msg'], 'Cone')),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 cone_yellow: typing.Optional[collections.abc.Sequence[fsd_common_msgs.msg.Cone]] = None,  # noqa: E501
                 cone_blue: typing.Optional[collections.abc.Sequence[fsd_common_msgs.msg.Cone]] = None,  # noqa: E501
                 cone_red: typing.Optional[collections.abc.Sequence[fsd_common_msgs.msg.Cone]] = None,  # noqa: E501
                 cone_unknown: typing.Optional[collections.abc.Sequence[fsd_common_msgs.msg.Cone]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.cone_yellow = cone_yellow if cone_yellow is not None else []
        self.cone_blue = cone_blue if cone_blue is not None else []
        self.cone_red = cone_red if cone_red is not None else []
        self.cone_unknown = cone_unknown if cone_unknown is not None else []

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
        if not isinstance(other, Map):
            return False
        if self.header != other.header:
            return False
        if self.cone_yellow != other.cone_yellow:
            return False
        if self.cone_blue != other.cone_blue:
            return False
        if self.cone_red != other.cone_red:
            return False
        if self.cone_unknown != other.cone_unknown:
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
    def cone_yellow(self) -> typing.Annotated[typing.Any, list[fsd_common_msgs.msg.Cone]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cone_yellow'."""
        return self._cone_yellow

    @cone_yellow.setter
    def cone_yellow(self, value: collections.abc.Sequence[fsd_common_msgs.msg.Cone]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from fsd_common_msgs.msg import Cone

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Cone) for v in value) and
                     True), \
                    "The 'cone_yellow' field must be sequence and each value of type 'Cone'"

        if isinstance(value, list):
            self._cone_yellow = value
            return
        self._cone_yellow = list(value)

    @builtins.property
    def cone_blue(self) -> typing.Annotated[typing.Any, list[fsd_common_msgs.msg.Cone]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cone_blue'."""
        return self._cone_blue

    @cone_blue.setter
    def cone_blue(self, value: collections.abc.Sequence[fsd_common_msgs.msg.Cone]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from fsd_common_msgs.msg import Cone

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Cone) for v in value) and
                     True), \
                    "The 'cone_blue' field must be sequence and each value of type 'Cone'"

        if isinstance(value, list):
            self._cone_blue = value
            return
        self._cone_blue = list(value)

    @builtins.property
    def cone_red(self) -> typing.Annotated[typing.Any, list[fsd_common_msgs.msg.Cone]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cone_red'."""
        return self._cone_red

    @cone_red.setter
    def cone_red(self, value: collections.abc.Sequence[fsd_common_msgs.msg.Cone]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from fsd_common_msgs.msg import Cone

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Cone) for v in value) and
                     True), \
                    "The 'cone_red' field must be sequence and each value of type 'Cone'"

        if isinstance(value, list):
            self._cone_red = value
            return
        self._cone_red = list(value)

    @builtins.property
    def cone_unknown(self) -> typing.Annotated[typing.Any, list[fsd_common_msgs.msg.Cone]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cone_unknown'."""
        return self._cone_unknown

    @cone_unknown.setter
    def cone_unknown(self, value: collections.abc.Sequence[fsd_common_msgs.msg.Cone]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from fsd_common_msgs.msg import Cone

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Cone) for v in value) and
                     True), \
                    "The 'cone_unknown' field must be sequence and each value of type 'Cone'"

        if isinstance(value, list):
            self._cone_unknown = value
            return
        self._cone_unknown = list(value)
