# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/Track.idl
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
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Track(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Track'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class TrackConstants(typing.TypedDict):
        pass

    __constants: TrackConstants = {
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
                'fsd_common_msgs.msg.Track')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__track
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__track
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__track
            cls._TYPE_SUPPORT = module.type_support_msg__msg__track
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__track

            from geometry_msgs.msg import Point
            if Point._TYPE_SUPPORT is None:
                Point.__import_type_support__()

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


class Track(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Track):
    """Message class 'Track'."""

    __slots__ = [
        '_header',
        '_cones_left',
        '_cones_right',
        '_cones_orange',
        '_cones_orange_big',
        '_tk_device_start',
        '_tk_device_end',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'cones_left': 'sequence<geometry_msgs/Point>',
        'cones_right': 'sequence<geometry_msgs/Point>',
        'cones_orange': 'sequence<geometry_msgs/Point>',
        'cones_orange_big': 'sequence<geometry_msgs/Point>',
        'tk_device_start': 'sequence<geometry_msgs/Point>',
        'tk_device_end': 'sequence<geometry_msgs/Point>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 cones_left: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 cones_right: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 cones_orange: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 cones_orange_big: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 tk_device_start: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 tk_device_end: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.cones_left = cones_left if cones_left is not None else []
        self.cones_right = cones_right if cones_right is not None else []
        self.cones_orange = cones_orange if cones_orange is not None else []
        self.cones_orange_big = cones_orange_big if cones_orange_big is not None else []
        self.tk_device_start = tk_device_start if tk_device_start is not None else []
        self.tk_device_end = tk_device_end if tk_device_end is not None else []

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
        if not isinstance(other, Track):
            return False
        if self.header != other.header:
            return False
        if self.cones_left != other.cones_left:
            return False
        if self.cones_right != other.cones_right:
            return False
        if self.cones_orange != other.cones_orange:
            return False
        if self.cones_orange_big != other.cones_orange_big:
            return False
        if self.tk_device_start != other.tk_device_start:
            return False
        if self.tk_device_end != other.tk_device_end:
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
    def cones_left(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cones_left'."""
        return self._cones_left

    @cones_left.setter
    def cones_left(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'cones_left' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._cones_left = value
            return
        self._cones_left = list(value)

    @builtins.property
    def cones_right(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cones_right'."""
        return self._cones_right

    @cones_right.setter
    def cones_right(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'cones_right' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._cones_right = value
            return
        self._cones_right = list(value)

    @builtins.property
    def cones_orange(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cones_orange'."""
        return self._cones_orange

    @cones_orange.setter
    def cones_orange(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'cones_orange' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._cones_orange = value
            return
        self._cones_orange = list(value)

    @builtins.property
    def cones_orange_big(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'cones_orange_big'."""
        return self._cones_orange_big

    @cones_orange_big.setter
    def cones_orange_big(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'cones_orange_big' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._cones_orange_big = value
            return
        self._cones_orange_big = list(value)

    @builtins.property
    def tk_device_start(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'tk_device_start'."""
        return self._tk_device_start

    @tk_device_start.setter
    def tk_device_start(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'tk_device_start' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._tk_device_start = value
            return
        self._tk_device_start = list(value)

    @builtins.property
    def tk_device_end(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'tk_device_end'."""
        return self._tk_device_end

    @tk_device_end.setter
    def tk_device_end(self, value: collections.abc.Sequence[geometry_msgs.msg.Point]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point) for v in value) and
                     True), \
                    "The 'tk_device_end' field must be sequence and each value of type 'Point'"

        if isinstance(value, list):
            self._tk_device_end = value
            return
        self._tk_device_end = list(value)
